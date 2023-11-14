import json

json_dosyasi = open("/home/a/Desktop/dosya.json","r",encoding="utf8")

dosya = json.load(json_dosyasi)

print(dosya["/home/a/Desktop/gizli_dosya"])
