class HesapMakinesi():

    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def toplama(self):
        return self.sayi1 + self.sayi2

    def cikarma(self):
        return self.sayi1 - self.sayi2

    def carpma(self):
        if self.sayi2 == 0:
            return "Bir sayi 0 ile carpilamaz"
        else:
            return  self.sayi1 * self.sayi2

    def bolme(self):
        if self.sayi2 == 0:
            return "Bir sayi 0'a bolunemez!"
        else:
            return  self.sayi1 / self.sayi2



if __name__ == '__main__':

    print("---------------")
    print("Hesap Makinesi(NTP)\n\n"
          "Secim Ediniz:"
          "Toplama: {+}\n"
          "Cikarma: {-}\n"
          "Carpma : {*}\n"
          "Bolme  : {/}\n")
    print("---------------")

    while True:

        sayi1 = float(input("Sayi 1 Giriniz:"))
        sayi2 = float(input("Sayi 2 Giriniz:"))
        secim = input("Secim Ediniz: ")

        hesapMakinesi = HesapMakinesi(sayi1,sayi2)

        if secim == "+":
            print(f"*************\n"
                  f"Toplamı: {hesapMakinesi.toplama()}\n"
                  f"*************")
        elif secim == "-":
            print(f"*************\n"
                  f"Farkı: {hesapMakinesi.cikarma()}\n"
                  f"*************")
        elif secim == "*":
            print(f"*************\n"
                  f"Çarpımı: {hesapMakinesi.carpma()}\n"
                  f"*************")
        elif secim == "/":
            print(f"*************\n"
                  f"Bölümü: {hesapMakinesi.bolme()}\n"
                  f"*************")

        else:
            print("Yalnış seçim lütfen doğru seçim ediniz.")

