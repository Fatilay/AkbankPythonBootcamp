import datetime
import csv
import locale
locale.setlocale(locale.LC_ALL, '')

class Pizza:
    def __init__(self,description,cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    
class Klasik(Pizza):
    def __init__(self):
        super().__init__('klasik',60.00)

class Margherita(Pizza):
    def __init__(self):
        super().__init__('margherita',84.99)

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__('Turk pizza',90.00)

class DominosPizza(Pizza):
    def __init__(self):
        super().__init__('Dominos Pizza',60.00)


class Decorator(Pizza):
     def __init__(self,component):
         self.component = component

     def get_cost(self):
       return self.component.get_cost() + Pizza.get_cost(self)

     def get_description(self):
       return self.component.get_description() + ' ' + Pizza.get_description(self)
     
class Zeytin(Decorator):
    def __init__(self,Pizza):
        super().__init__(Pizza)
        self.description = 'Zeytin'
        self.cost = 10.00

class Mantar(Decorator):
    def __init__(self,Pizza):
        super().__init__(Pizza)
        self.description = 'Mantar'
        self.cost = 10.00

class keciPeyniri(Decorator):
    def __init__(self,Pizza):
        super().__init__(Pizza)
        self.description = 'Keci Peyniri'
        self.cost = 12.00

class Et(Decorator):
    def __init__(self,Pizza):
        super().__init__(Pizza)
        self.description = 'Et'
        self.cost = 30.00

class Sogan(Decorator):
    def __init__(self,Pizza):
        super().__init__(Pizza)
        self.description = 'Sogan'
        self.cost = 10.00

class Misir(Decorator):
    def __init__(self,Pizza):
        super().__init__(Pizza)
        self.description = 'Misir'
        self.cost = 14.00



def Create_menu():
    dosya = open('Menu.txt','w',encoding='Utf-8')
    dosya.write('* Lutfen Bir Pizza Tabani Seciniz:\n 1: Klasik\n 2: Margarita\n 3: TurkPizza\n 4: Sade Pizza\n * ve sececeginiz sos:\n 11: Zeytin\n 12: Mantarlar\n 13: Keci Peyniri 14: Et\n 15: Sogan\n 16: Misir\n * Tesekkur ederiz!\n')
    dosya.close()

def main():
    dosyad = open('Menu.txt','r',encoding='Utf-8')
    file_contents = dosyad.read()
    dosyad.close()
    print(file_contents)
    
    print('Menu')
    print('1. Klasik Pizza')
    print('2. Margherita Pizza')
    print('3. Türk Pizza')
    print('4. Dominos Pizza')
    print('5. Cikis')

    pizza_secim = input('bir pizza cesidi secin(1-5): ')
    if pizza_secim == '5':
        print('Cikis Yapildi...')
        return
    elif pizza_secim == '1':
        pizza = Klasik()
    elif pizza_secim == '2':
        pizza = Margherita()
    elif pizza_secim == '3':
        pizza = TurkPizza()    
    elif pizza_secim == '4':
        pizza = DominosPizza()
    else:
        print('lütfen gecerli bir deger secin!')
        return

    # sos secimlerini alma
    print('Sos Menusu')
    print('1. zeytin')
    print('2. mantar')
    print('3. keci peyniri')
    print('4. et')
    print('5. sogan')
    print('6. misir')
    print('7. cikis')

    sos_secimleri = []
    while True:
        sos_secim = input('bir sos secin: ')
        
        if sos_secim == '1' :
            pizza = Zeytin(pizza)
        elif sos_secim == '2' :
            pizza = Mantar(pizza)
        elif sos_secim == '3' :
            pizza = keciPeyniri(pizza)
        elif sos_secim == '4' :
            pizza = Et(pizza)
        elif sos_secim == '5' :
            pizza = Sogan(pizza)
        elif sos_secim == '6' :
            pizza = Misir(pizza)
        elif sos_secim == '7':
            break
        else:
            print("Lutfen gecerli bir sos girin!")
            return
        
        sos_secimleri.append(int(sos_secim))


# #toplam fiyat
    toplam_fiyat = pizza.get_cost()
    print('Toplam Fiyat: ',toplam_fiyat)

#pizza ve sos seçimi belirleme
    order_description = pizza.get_description()
    print('detaylar: ', order_description)

#kullanıcı bilgilerinin alınması 
    Ad = input('Ad: ')
    TcKNo = input('Tc Kimlik No: ')
    Kredi_Kart_No = input('Kredi Karti Numarasi: ')
    Kredi_Kart_Sifre = input('Kredi Kart Sifresi: ')
    siparis_zamani = datetime.datetime.now().strftime('%c')#tam tarihi alabilmek için strftime hazır fonksiyonu kullanıldı.
#bilgilerin veritabanına kaydedilmesi
    with open("Orders_Database.csv","a",newline='',encoding='Utf-8') as dosyaad:
        write = csv.writer(dosyaad)
        write.writerow([Ad, TcKNo, Kredi_Kart_No, Kredi_Kart_Sifre, siparis_zamani, order_description])
    print("Siparisiniz basariyla kaydedilmistir!")
    print(siparis_zamani)
if __name__ == '__main__':
    main()

    