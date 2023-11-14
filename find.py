import os
import json
from termcolor import colored

json_dosyasi = open("/home/a/Desktop/kodlar/yeni/dosya.json","w",encoding='utf-8')
gönder = {}

mesaj = '''
[+]---TURK------HACK-----TEAM---[+]
[+]-----------yuathay-----------[+]
[+]-----------------------------[+]
'''
dizin = []
os.system("clear")
print(mesaj)
print(
"""
hangi işlemi yapmak istersiniz :

1) sadece belirttiğim dizinin altındaki dosyaların içeriğini istiyorum
2) belirttiğim dizinden itibaren varolan bütün dosyaların içeriğini istiyorum
""")
while True:
    try:
        secim = int(input())
        if secim == 1 or secim == 2:
            break
        else:
            print("1 veya 2 seçeneğini seçin")
    except:
        print("1 veya 2 seçeneğini seçin")
        pass
def başla(baslangic_dizini):
    ayrintili_ls_çıktısı = os.popen(f"ls -l '{baslangic_dizini}'").read().split("\n") #ayrıntılı liste değ,ştir
    ls_çıktısı = os.popen(f"ls '{baslangic_dizini}'").read().split("\n") #liste 
    
    def dizin_bul(ayrintili_ls_çıktısı,ls_çıktısı): #bir site aç siteye post işlemi ile bu verileri gönder
        
        for i in range(len(ayrintili_ls_çıktısı)):
                
            #===================================
            if i == 0: # ls -l çıktısında ilk satırda total adında bir değer var onu geçiyoruz
                continue
            #===================================

            #====================================
            if i == len(ayrintili_ls_çıktısı)-1: #dizin bulmada hata yaşarsan bu döngüyü çalıştır bu if blogunu sona koy
                
                #gönder.clear() #tekrar eden değerler göndermemesi için sözlüğü temizliyoruz
                break            
            #====================================
            else:
                if ayrintili_ls_çıktısı[i].startswith("d"):

                    yol = baslangic_dizini+"/"+ls_çıktısı[i-1]
                    dizin.append(yol)

                    #ayrintili = os.popen(f"ls -l {yeni_deger}").read().split("\n")
                    #dizin_dosya = os.popen(f"ls {yeni_deger}").read().split("\n") 
                    #dizin_bul(ayrintili,dizin_dosya)
                    continue
                #===================================
                else:
                    yol = baslangic_dizini+"/"+ls_çıktısı[i-1] #dosya yolunu alıyoruz
                    try:
                        #===================================
                        if os.popen(f"cat '{yol}' 2>/dev/null").read(): #bazen permission denied hatası verebiliyor ve biz bu hatayı yazdırmasak bile kendiliginden rahatsız edici bir cıktı oluşuyor bunu engelliyoruz
                            içerik = os.popen(f"cat '{yol}'").read()
                        #===================================
                        else:
                            if not os.popen(f"cat '{yol}' 2>/dev/null").read(): #dosyanın içi boşsa geç
                                continue
                            print(colored(f"permission denied ---> {yol}","red")) 
                            continue
                        #===================================
                    except UnicodeDecodeError: # okunamayan dosyalar bize UnicodeDecodeError adlı hatayı döndürecektir eğer bu hata varsa hata mesajı verme bunun yerine
                        print(colored(f"okunamayan dosyalar ---> {yol}","blue")) #bu mesajı yazdır diyoruz
                        continue 
                    gönder[yol] = içerik
                #===================================                       
    dizin_bul(ayrintili_ls_çıktısı,ls_çıktısı)

başla("/home/a/Desktop")
#=========================
if secim == 1:
    json.dump(gönder,json_dosyasi,ensure_ascii=False)
#=========================
elif secim == 2:
    for i in dizin:
        başla(i)
    json.dump(gönder,json_dosyasi,ensure_ascii=False)
#=========================
json_dosyasi.close() #json dosyasına içeriklerimizi gönderdikten sonra dosyayı kapatıyoruz
#=========================
print("\nbu keyler ile dosya içeriğini çekebilirsiniz :\n")
with open("/home/a/Desktop/kodlar/yeni/dosya.json","r") as dosya:
    veriler = json.load(dosya)
anahtarlar = list(veriler.keys())
[print(i) for i in anahtarlar]
#=========================
