import json
import pandas as pd
from pyvis.network import Network
from collections import defaultdict
import webbrowser
import re

# JSON dosyasını UTF-8 kodlamasıyla yükleyin
with open('veri.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Paket verilerini çıkarın
packets = data  # JSON yapınız farklıysa bunu ayarlayın

# İlgili verileri depolamak için bir DataFrame oluşturun
packet_list = []

for packet in packets:
    layer = packet['_source']['layers']
    frame = layer.get('frame', {})
    ip_layer = layer.get('ip', {})
    row_protocol = frame.get('frame.coloring_rule.name', '')
    length = int(frame.get('frame.len', 0))  # Uzunluğu tamsayıya dönüştürün
    time_str = frame.get('frame.time', '')  # Zamanı biçimlendirilmemiş bir dize olarak alın

    # Zamanı çıkarmak için regex kullanın
    match = re.search(r'\b(\w+ \d+, \d+ \d+:\d+:\d+\.\d+)\b', time_str)
    if match:
        time_str = match.group(1)
        # Zaman biçimini belirtin ve datetime nesnesine dönüştürün
        time_format = "%b %d, %Y %H:%M:%S.%f"
        time = pd.to_datetime(time_str, format=time_format)
    else:
        time = None

    packet_info = {
        'frame_number': frame.get('frame.number', ''),
        'src_ip': ip_layer.get('ip.src', ''),
        'dst_ip': ip_layer.get('ip.dst', ''),
        'protocol': row_protocol,
        'length': length,
        'frame.time': time
    }

    packet_list.append(packet_info)

df = pd.DataFrame(packet_list)

# src_ip ve dst_ip'ye göre paketleri toplayın
edge_dict = defaultdict(lambda: {'count': 0, 'protocols': set(), 'lengths': [], 'times': []})

for _, row in df.iterrows():
    src = row['src_ip']
    dst = row['dst_ip']
    row_protocol = row['protocol']
    length = row['length']
    time = row['frame.time']

    if src and dst:
        edge_dict[(src, dst)]['count'] += 1
        edge_dict[(src, dst)]['protocols'].add(row_protocol)
        edge_dict[(src, dst)]['lengths'].append(length)
        edge_dict[(src, dst)]['times'].append(time)

# Farklı sayı aralıkları için renk eşlemelerini tanımlayın
def get_edge_color(protocol_list):
    protocol_color_map = {
        'HTTP': 'blue',
        'HTTPS': 'green',
        'DNS': 'red',
        'TCP': 'orange',
        'UDP': 'salmon',
        'SMTP': 'purple',
        'FTP': 'brown',
        'SSH': 'pink',
        'ICMP': 'cyan',
        'ARP': 'magenta',
        'TELNET': 'lime',
        'POP3': 'gold',
        'IMAP': 'teal',
        'SNMP': 'olive',
        'NTP': 'navy',
        'DHCP': 'indigo',
        'LDAP': 'violet',
        'SMB': 'coral',
        'RDP': 'yellow',
        'SSL': 'darkred',
        'TLS': 'darkgreen',
        'IKEv2': 'darkblue',
        'IPsec': 'darkorange',
        'GRE': 'sienna',
        'BGP': 'steelblue',
        'MPLS': 'tan',
        'OSPF': 'tomato',
        'RIP': 'wheat',
        'VRRP': 'darkslategray',
        'IGMP': 'cadetblue',
        # İhtiyacınız olan diğer protokol türlerini buraya ekleyebilirsiniz
    }

    default_color = 'gray'  # Belirli bir protokol türüne renk ataması yoksa varsayılan gri renk

    # İlk protokolün rengini alın
    for protocol in protocol_list:
        color = protocol_color_map.get(protocol, default_color)
        if color != default_color:
            return color

    # Renk ataması yapılmadıysa varsayılan rengi döndürün
    return default_color

# Bir PyVis ağı oluşturun
net = Network(height='750px', width='100%', notebook=True, directed=True)

# Toplanmış verilere dayanarak düğümler ve kenarlar ekleyin
nodes = set()
for (src, dst), info in edge_dict.items():
    if src not in nodes:
        net.add_node(src, label=src)
        nodes.add(src)
    if dst not in nodes:
        net.add_node(dst, label=dst)
        nodes.add(dst)

    protocols = info['protocols']
    count = info['count']
    lengths = info['lengths']
    times = info['times']

    # Kenar için protokole göre bir renk seçin
    edge_color = get_edge_color(protocols)

    # Kenar için başlık belirtin ve zamanı biçimlendirin
    title = f"Protocols: {', '.join(protocols)}\nCount: {count}\nMin Length: {min(lengths)}\nMax Length: {max(lengths)}\nTime: {min(times).strftime('%Y-%m-%d %H:%M:%S')} - {max(times).strftime('%Y-%m-%d %H:%M:%S')}"

    # Kalınlığı paket sayısına göre ayarlayın
    thickness = count

    # Belirtilen renk ve kalınlıkla kenarı ekleyin
    net.add_edge(src, dst, title=title, color=edge_color, arrows='to', width=thickness)

# Görselleştirmeyi oluşturun ve HTML dosyası olarak kaydedin
html_file = 'packet_network.html'
net.show(html_file)

# Oluşturulan HTML dosyasını varsayılan web tarayıcısında açın
webbrowser.open(html_file)