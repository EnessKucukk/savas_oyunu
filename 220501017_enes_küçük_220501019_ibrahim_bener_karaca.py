import tkinter as tk
import tkinter.simpledialog as sd

class Savaşçı:
    def __init__(self, ad, maliyet, sağlık, saldırı_mesafesi):
        self.ad = ad
        self.maliyet = maliyet
        self.sağlık = sağlık
        self.saldırı_mesafesi = saldırı_mesafesi
        self.kaynak = maliyet

    def saldır(self, düşman):
        hasar = min(self.kaynak, düşman.sağlık)
        düşman.sağlık -= hasar
        print(f"{self.ad} {düşman.ad} hedefine {hasar} hasar verdi!")
        self.kaynak -= self.maliyet


class Muhafız(Savaşçı):
    def __init__(self):
        super().__init__("Muhafız", 10, 80, 1)
        self.kaynak = 10

class Okçu(Savaşçı):
    def __init__(self):
        super().__init__("Okçu", 20, 30, 2)
        self.kaynak = 20

class Topçu(Savaşçı):
    def __init__(self):
        super().__init__("Topçu", 50, 30, 2)
        self.kaynak = 50

class Atlı(Savaşçı):
    def __init__(self):
        super().__init__("Atlı", 30, 40, 3)
        self.kaynak = 30

class Sağlıkçı(Savaşçı):
    def __init__(self):
        super().__init__("Sağlıkçı", 10, 100, 2)
        self.kaynak = 10

class Dünya:
    def __init__(self, boyut):
        self.boyut = boyut
        self.grid = [[None for _ in range(boyut)] for _ in range(boyut)]
        self.mevcut_oyuncu = 1  # İlk oyuncu
        self.oyuncular = [Oyuncu("Oyuncu 1"), Oyuncu("Oyuncu 2")]
        self.seçili_savaşçı = None
        self.kaynaklar = [200, 200]
    def dünyayı_yazdır(self):
        for satır in self.grid:
            print(' '.join(['.' if hücre is None else hücre.ad[0] for hücre in satır]))

    def savaşçı_yerleştir(self, savaşçı, x, y):
        if 1 <= x <= self.boyut and 1 <= y <= self.boyut and self.grid[x - 1][y - 1] is None:
            savaşçı.x, savaşçı.y = x, y
            self.grid[x - 1][y - 1] = savaşçı
            mevcut_oyuncu_index = self.mevcut_oyuncu - 1
            self.oyuncular[mevcut_oyuncu_index].savaşçı_ekle(savaşçı)
            self.kaynaklar[mevcut_oyuncu_index] -= savaşçı.maliyet
            self.mevcut_oyuncu = 3 - self.mevcut_oyuncu
        else:
            print("Geçersiz konum!")

    def savaşçı_al(self, x, y):
        if 1 <= x <= self.boyut and 1 <= y <= self.boyut:
            return self.grid[x - 1][y - 1]
        else:
            return None

    def savaşçı_seç(self, savaşçı):
        self.seçili_savaşçı = savaşçı


class Oyuncu:
    def __init__(self, ad):
        self.ad = ad
        self.savaşçılar = []

    def savaşçı_ekle(self, savaşçı):
        self.savaşçılar.append(savaşçı)


class OyunUygulaması:
    def __init__(self, ana_pencere):
        self.ana_pencere = ana_pencere
        ana_pencere.title("Savaş Oyunu")

        self.canvas = tk.Canvas(ana_pencere, width=400, height=400)
        self.canvas.pack()

        self.etiket = tk.Label(ana_pencere, text="Savaş başlıyor! Oyuncular, kendi savaşçılarınızı seçin.")
        self.etiket.pack()

        self.boyut_seçenekleri = [16, 24, 32]
        self.boyut_değişkeni = tk.IntVar()
        self.boyut_değişkeni.set(self.boyut_seçenekleri[0])

        self.boyut_etiketi = tk.Label(ana_pencere, text="Matris Boyutunu Seçin:")
        self.boyut_etiketi.pack()

        for boyut in self.boyut_seçenekleri:
            rb = tk.Radiobutton(ana_pencere, text=f"{boyut}x{boyut}", variable=self.boyut_değişkeni, value=boyut)
            rb.pack()

        self.başlat_düğmesi = tk.Button(ana_pencere, text="Oyunu Başlat", command=self.oyunu_başlat)
        self.başlat_düğmesi.pack()

        self.kapat_düğmesi = tk.Button(ana_pencere, text="Oyunu Kapat", command=ana_pencere.quit)
        self.kapat_düğmesi.pack()

        self.oyuncular = [Oyuncu("Oyuncu 1"), Oyuncu("Oyuncu 2")]

        self.sıra_penceresi = None

    def dünyayı_çiz(self):
        self.canvas.delete("all")
        self.hücre_boyutu = 400 // self.dünya.boyut
        for i in range(self.dünya.boyut):
            for j in range(self.dünya.boyut):
                x0, y0 = j * self.hücre_boyutu, i * self.hücre_boyutu
                x1, y1 = x0 + self.hücre_boyutu, y0 + self.hücre_boyutu
                if self.dünya.grid[i][j] is None:
                    renk = "white"
                else:
                    savaşçı_tipi = self.dünya.grid[i][j].ad
                    if savaşçı_tipi == "Muhafız":
                        renk = "blue"
                    elif savaşçı_tipi == "Okçu":
                        renk = "green"
                    elif savaşçı_tipi == "Topçu":
                        renk = "red"
                    elif savaşçı_tipi == "Atlı":
                        renk = "orange"
                    elif savaşçı_tipi == "Sağlıkçı":
                        renk = "purple"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=renk)
        for i, oyuncu in enumerate(self.dünya.oyuncular):
            self.canvas.create_text(20, 20 + i * 20, anchor=tk.W, text=f"{oyuncu.ad} Kaynak: {self.dünya.kaynaklar[i]}")

    def oyunu_başlat(self):
        boyut = self.boyut_değişkeni.get()
        self.dünya = Dünya(boyut)
        self.dünyayı_çiz()
        self.canvas.bind("<Button-1>", self.tıklamayı_işle)
        self.kapat_düğmesi.pack_forget()
        self.etiket.config(text=f"{self.oyuncular[0].ad}, kendi savaşçılarını seç!")
        self.savaşçı_seç()

    def tıklamayı_işle(self, olay):
        satır = olay.y // self.hücre_boyutu + 1
        sütun = olay.x // self.hücre_boyutu + 1
        print(f"Tıklanan hücre: {satır}, {sütun}")
        self.savaşçı_yerleştir(satır, sütun)

    def savaşçı_yerleştir(self, satır, sütun):
        if self.dünya.seçili_savaşçı is not None:
            savaşçı = self.dünya.seçili_savaşçı
            mevcut_oyuncu_index = self.dünya.mevcut_oyuncu - 1
            if self.dünya.kaynaklar[mevcut_oyuncu_index] >= savaşçı.maliyet:
                self.dünya.savaşçı_yerleştir(savaşçı, satır, sütun)
                self.dünyayı_çiz()
                self.savaşçı_seç()
                self.savaş_çatışmasını_işle(savaşçı, satır, sütun)
            else:
                print("Bu savaşçıyı yerleştirmek için yeterli kaynak yok.")
        else:
            self.savaşçı_seç()

    def savaşçı_seç(self):
        savaşçı_seçenekleri = ["Muhafız", "Okçu", "Topçu", "Atlı", "Sağlıkçı"]
        savaşçı_seçimi = sd.askstring("Savaşçı Seç", "Hangi savaşçıyı seçmek istersiniz?", initialvalue=savaşçı_seçenekleri[0], parent=self.ana_pencere)
        if savaşçı_seçimi:
            if savaşçı_seçimi == "Muhafız":
                savaşçı = Muhafız()
            elif savaşçı_seçimi == "Okçu":
                savaşçı = Okçu()
            elif savaşçı_seçimi == "Topçu":
                savaşçı = Topçu()
            elif savaşçı_seçimi == "Atlı":
                savaşçı = Atlı()
            elif savaşçı_seçimi == "Sağlıkçı":
                savaşçı = Sağlıkçı()
            self.dünya.savaşçı_seç(savaşçı)
            self.etiket.config(text=f"{self.oyuncular[self.dünya.mevcut_oyuncu - 1].ad}, sıradaki savaşçını seç!")
            if self.sıra_penceresi:
                self.sıra_penceresi.destroy()
            self.sıra_penceresi = tk.Toplevel(self.ana_pencere)
            self.sıra_penceresi.title("Oyuncu Sırası")
            oyuncu_etiketi = tk.Label(self.sıra_penceresi, text=f"{self.oyuncular[self.dünya.mevcut_oyuncu - 1].ad}, sıradaki savaşçını seç!")
            oyuncu_etiketi.pack()

    def savaş_çatışmasını_işle(self, savaşçı, satır, sütun):
        for i in range(max(0, satır - savaşçı.saldırı_mesafesi), min(self.dünya.boyut, satır + savaşçı.saldırı_mesafesi + 1)):
            for j in range(max(0, sütun - savaşçı.saldırı_mesafesi), min(self.dünya.boyut, sütun + savaşçı.saldırı_mesafesi + 1)):
                if (i, j) != (satır, sütun):
                    düşman_savaşçı = self.dünya.savaşçı_al(i + 1, j + 1)
                    if düşman_savaşçı is not None:
                        self.saldır(savaşçı, düşman_savaşçı)

    def saldır(self, saldırgan, savunmacı):
        hasar = min(saldırgan.kaynak, savunmacı.sağlık)
        savunmacı.sağlık -= hasar
        print(f"{saldırgan.ad} {savunmacı.ad} hedefine {hasar} hasar verdi!")
        self.dünya.kaynaklar[self.dünya.mevcut_oyuncu - 1] -= saldırgan.saldırı_mesafesi


def main():
    root = tk.Tk()
    app = OyunUygulaması(root)
    root.mainloop()


if __name__ == "__main__":
    main()

