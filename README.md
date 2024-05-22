# Ag_Programlama
Ag Paketleri Analizi ve Gorsellestirilmesi
Projenin amacı kullanıcılara wiresharktaki ağ paketlerini okumaları ve anlamaları konusunda kolaylık sağlamaktır.
Ağ trafiği veri dosyalarını okuyarak, iletilen paketler arasındaki ilişkileri analiz etmek ve bu ilişkileri graf
yapısıyla görselleştirerek kullanıcıya sunmaktır. Kullanıcı oluşturulan görselde paketleri kolaylıkla inceleyip analiz
yapabilecektir.
İletilen paketlerin özelliklerini, örneğin protokol türlerini, kaynak ve hedef IP adreslerini, iletilen veri miktarını vb. 
gibi bilgileri görsel olarak gözlemleyebilecektir.
Toplanan verileri kullanarak, ağdaki bağlantıları görselleştirilecek ve farklı protokol türlerine göre paketler renklendirilecektir.
Hangi ip adresinden hangi ip adresine kaç adet paket gönderildiği de paket sayısına göre görselleştirilip kalınlık sağlanacaktır.
Görselleştirmeler aracılığıyla, ağ trafiğinin genel yapısını anlamak ve potansiyel anormallikleri tespit etmek temel amaçtır.

#Kullanılan_Yöntemler

Ağ trafiği veri dosyalarının JSON formatında okunması ve içeriğinin pandas DataFrame'e dönüştürülmesi.
Ağ trafiği veri dosyaları JSON formatında okunur ve içeriği karmaşıklığı azaltmak için veri sözlüğüne dönüştürülür.
Veriler veri sözlüğünden okunarak işlenir.
İlişkilerin görselleştirilmesi için, pyvis kütüphanesinin kullanılması ve paket bağlantılarının ağ grafiği olarak temsil edilmesi.
İlişkiler, kenarlar ve düğümler için pyvis kütüphanesi kullanılır. Paketlerin bağlantıları, renkleri, sayıları ve hareketliliği 
pyvis ile sağlanır. 
Görselleştirmelerde farklı protokol türlerine göre renklendirme yapılır ve paket sayısına göre kalınlıklar ayarlanır.
Paket sayısı fazla olan kenar daha kalın görselleştirilir. Ayrıca her protokol türü farklı renkler ile temsil edilir ve
graf modelinde farklı renklerde görselleştirilir.


#Graphical_Abstract

![Home](https://github.com/karaozan09/Ag_Programlama/assets/95549258/2923b185-ffe8-4f62-999a-d8a5b80dc989)

#Interface_1

![WhatsApp Image 2024-05-20 at 15 17 47 (1)](https://github.com/karaozan09/Ag_Programlama/assets/95549258/578f1e1b-5daf-4476-9bd2-65e98ce9041a)

#Interface_2

![WhatsApp Image 2024-05-20 at 15 45 20](https://github.com/karaozan09/Ag_Programlama/assets/95549258/65d80cee-8fd6-4d3e-8a49-334fb4e53a02)
