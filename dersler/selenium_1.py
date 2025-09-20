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
# options.add_argument("--incognito")  # İsteğe bağlı
# options.add_argument("--headless")   # İsteğe bağlı

# ChromeDriver servis nesnesi oluşturuyoruz
service = Service(driver_path)

# WebDriver'ı başlatıyoruz
browser = webdriver.Chrome(service=service, options=options)

# URL'yi açıyoruz
url = "https://www.stealmylogin.com/demo"
browser.get(url)
username = "admin"
password = "ruhi123"

# Sayfa başlığını kontrol edelim
print(browser.title)

browser.find_element(By.XPATH,"/html/body/form/input[1]").send_keys(username)
browser.find_element(By.XPATH,"/html/body/form/input[2]").send_keys(password)
browser.find_element(By.XPATH,"/html/body/form/input[3]").click()
time.sleep(50)
# İşlem bittikten sonra tarayıcıyı kapatın
browser.quit()

