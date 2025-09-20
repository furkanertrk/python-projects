import requests
from email.message import EmailMessage
import smtplib
import time
from lxml import html

def get_fiyat_ve_gonder():
    url = "https://www.getmidas.com/canli-borsa/tuprs-hisse/"
    result = requests.get(url,timeout=10)
    result.raise_for_status()
    tree = html.fromstring(result.content)
    endeks = tree.xpath("/html/body/div[1]/div/div/div/div[4]/div[1]/div/p")
    return endeks[0].text

def mailgonder():
    giris = "testm5844@gmail.com"
    şifre = "vlyk wrpy peay kpuj"
    gonderilecekhesap = "furkanerturk789@protonmail.com"
    subject = "Tüpraş Fiyat Güncellemesi!!!"
    mailtext ="Fiyat değişti!!! => " + get_fiyat_ve_gonder()

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = giris
    msg['To'] = gonderilecekhesap
    msg.set_content(mailtext)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(giris, şifre)
    server.send_message(msg)
    server.quit()



while True:
    para_degeri = get_fiyat_ve_gonder()
    # Para birimi simgesini ve virgülü temizleyin
    para_degeri = para_degeri.replace("₺", "").replace(",", ".")
    # String'i float'a dönüştürün
    float_deger = float(para_degeri)

    if float_deger < 155 or float_deger > 175:
        mailgonder()
    time.sleep(600)
