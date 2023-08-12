import sqlite3
import time

db = sqlite3.connect('ogrenci.db')
cursor = db.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS ogrenci (ad TEXT, soyad TEXT, numara INTEGER)')
    db.commit()

# create_table()
    
def ogr_ekle():
    ad = input("Öğrenci Adını giriniz: ")
    soyad = input("Öğrencinin soyadını giriniz: ")
    no = int(input("Öğrenci numarasını giriniz: "))
    cursor.execute("INSERT INTO ogrenci VALUES(?,?,?)",(ad,soyad,no))
    db.commit()   

def ogr_sil():
    no = int(input("Bilgilerini Silmek istediğiniz öğrencinin numarasını giriniz: "))
    cursor.execute("DELETE FROM ogrenci WHERE numara = ?",(no,)) 
    db.commit()

def ogr_ara():
    no = int(input("aramak istediğiniz öğrencinin numarasını giriniz: "))
    cursor.execute("SELECT * FROM ogrenci WHERE numara = ?",(no,))
    liste = cursor.fetchall()
    for i in liste:
        print(i)
    
def ogr_lis():
    cursor.execute("SELECT * FROM ogrenci")
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def main():
    print("Öğrenci Otomasyonuna Hoşgeldiniz") 
    time.sleep(1)
    print("Menü Yükleniyor...")
    time.sleep(1)
    time.sleep(1)
    while True:
        print(
        """
           Öğrenci Kayıt Otomasyonu
       
           1 - Öğrenci ekle
           2 - Öğrenci ara
           3 - Öğrenci sil
           4 - Öğrenci listesi
           5 - Çıkış Yap
           """)
        secim = int(input("Yapmak istediğiniz işlem: "))
        if secim == 1:
            ogr_ekle()
            print("Öğrenci Eklendi")
            print("Lütfen Bekleyiniz...")
            time.sleep(2)    
        
        if secim == 2:
            ogr_ara()
            print("Öğrenci Bilgileri")
            time.sleep(2)
            print("Ana menüye yönlendiriliyorsunuz")
            print("Lütfen Bekleyiniz...")
            time.sleep(2)
               
        if secim == 3:
            ogr_sil()
            print("Öğrenci Bilgileri Silindi")
            print("Lütfen Bekleyiniz...")
            time.sleep(1)
            time.sleep(1)
             
        if secim == 4:
            ogr_lis()
            print("Öğrenci Listesi")
            time.sleep(2)
            print("Ana menüye yönlendiriliyorsunuz")
            print("Lütfen Bekleyiniz...")
            time.sleep(2)
        
        if secim == 5:
            print("Çıkış Yapılıyor...")
            time.sleep(2)
            print("İyi Günler...")
            break


if __name__ == '__main__':
    main()