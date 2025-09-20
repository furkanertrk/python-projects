import requests
from lxml import html

istek = requests.get("https://tr.tradingview.com/symbols/BIST-XU100/")
web_içerik = istek.content

tree = html.fromstring(web_içerik)
fxpath = "/html/body/div[3]/div[4]/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]/span"

sonuç = tree.fxp  