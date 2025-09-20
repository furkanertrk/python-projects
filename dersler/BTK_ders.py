from datetime import datetime

result = dir(datetime)

zaman = datetime.now()
bu_yıl = datetime.now().year
print(zaman)
print(bu_yıl)

bu_gün = datetime.today()
result = datetime.strftime(bu_gün, "%Y")
result = datetime.strftime(bu_gün, "%X")
result = datetime.strftime(bu_gün, "%d")
result = datetime.strftime(bu_gün, "%A")
result = datetime.strftime(bu_gün, "%B")
result = datetime.strftime(bu_gün, "%Y %B %A")
print(result)
custom_zaman = "1 August 2024"
sonuc = datetime.strptime(custom_zaman, '%d %B %Y')
print("Custom zaman: {}".format(sonuc))
