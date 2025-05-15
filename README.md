# Savaş Oyunu

Bu Python uygulaması, iki oyuncunun savaşçılarını seçip yerleştirerek birbirleriyle savaştığı bir strateji oyununu simüle eder. Oyuncular, savaşçılarını matris üzerinde yerleştirerek düşmanlarına saldırabilir ve kaynaklarını yönetebilir.

## Özellikler

- **Savaşçı Seçimi**: Oyuncular, farklı türde savaşçılar (Muhafız, Okçu, Topçu, Atlı, Sağlıkçı) seçebilir.
- **Kaynak Yönetimi**: Her savaşçının bir maliyeti vardır ve oyuncuların sınırlı kaynakları vardır.
- **Savaş Mekaniği**: Savaşçılar, belirli bir mesafeden düşmanlarına saldırabilir.
- **Görsel Arayüz**: Tkinter kullanılarak oluşturulmuş basit bir grafik arayüz.

## Gereksinimler

- Python 3.x
- `tkinter` (Python ile birlikte gelir)

## Kurulum

1. Python'u bilgisayarınıza indirin ve kurun.
2. Uygulama dosyasını indirin veya kopyalayın.
3. Terminal veya komut istemcisinde uygulama dosyasını çalıştırın:
   ```bash
   python uygulama.py
Kullanım
Matris Boyutunu Seçin: Uygulama açıldığında, 16x16, 24x24 veya 32x32 boyutlarından birini seçin.
Oyunu Başlatın: "Oyunu Başlat" butonuna tıklayın.
Savaşçı Seçimi: Oyuncular sırayla savaşçılarını seçer ve matris üzerinde yerleştirir.
Savaşçılarla Saldırı: Savaşçılar, belirlenen mesafeye göre düşmanlarına saldırabilir.
Kaynak Yönetimi: Oyuncular, kaynaklarını yöneterek savaşçılarını yerleştirmeye devam eder.
Savaşçı Türleri
Muhafız:

Maliyet: 10
Sağlık: 80
Saldırı Mesafesi: 1
Açıklama: Yüksek sağlık değerine sahip, düşük maliyetli bir savaşçı.
Okçu:

Maliyet: 20
Sağlık: 30
Saldırı Mesafesi: 2
Açıklama: Uzaktan saldırı yapabilen, orta sağlık değerine sahip bir savaşçı.
Topçu:

Maliyet: 50
Sağlık: 30
Saldırı Mesafesi: 2
Açıklama: Yüksek maliyetli, ancak güçlü bir uzaktan saldırı birimi.
Atlı:

Maliyet: 30
Sağlık: 40
Saldırı Mesafesi: 3
Açıklama: Yüksek saldırı mesafesine sahip, orta sağlık değerine sahip bir savaşçı.
Sağlıkçı:

Maliyet: 10
Sağlık: 100
Saldırı Mesafesi: 2
Açıklama: Destek birimi olarak görev yapar, yüksek sağlık değerine sahiptir.
Oyun Mekaniği
Kaynak Yönetimi: Her oyuncunun başlangıçta 200 kaynağı vardır. Savaşçı yerleştirildiğinde, o savaşçının maliyeti kadar kaynak düşer.
Savaş: Savaşçılar, belirli bir mesafeden düşman savaşçılarına saldırabilir. Saldırı sırasında, saldıran savaşçı düşmanına hasar verir ve düşmanın sağlığı azalır.
Oyun Sırası: Oyuncular sırayla savaşçılarını seçer ve yerleştirir. Her oyuncunun sırayla hareket etmesi gerekmektedir.
Katkıda Bulunma
Herhangi bir hata veya öneri için lütfen bir sorun açın veya katkıda bulunun. Projeye katkıda bulunmak için aşağıdaki adımları takip edebilirsiniz:


