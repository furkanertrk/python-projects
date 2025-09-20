from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
# Brave browser'ın yüklü olduğu yol
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

# ChromeDriver'ın yüklü olduğu yol
driver_path = "C:\\Users\\furkan\\Documents\\Python\\pythondersleri\\chromedriver-win64\\chromedriver.exe"

# Brave'i kullanmak için Chrome seçenekleri oluşturuyoruz
options = Options()
options.binary_location = brave_path
options.add_argument("--incognito")  # gizli sekmede açıyor
options.add_argument("--headless")   # bunu biz görmüyoruz

# ChromeDriver servis nesnesi oluşturuyoruz
service = Service(driver_path)

# WebDriver'ı başlatıyoruz
browser = webdriver.Chrome(service=service, options=options)
browser.delete_all_cookies()
browser.get("https://tr.tradingview.com/symbols/BIST-XU100/")
browser.implicitly_wait(10) #sitenin yüklenmesini bekleme
while True:
    fiyat_bilgisi = browser.find_element(By.XPATH,"/html/body/div[3]/div[4]/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]").text
    print(fiyat_bilgisi)
    time.sleep(3)


