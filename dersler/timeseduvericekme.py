from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# ChromeDriver yolunu belirleyin
driver_path = "C:\\Users\\furkan\\Documents\\chromedriver-win64\\chromedriver.exe"

# Service sınıfı ile ChromeDriver'ı başlatın
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Times Higher Education sıralama sayfasına gidin
url = 'https://www.timeshighereducation.com/world-university-rankings/2024/world-ranking'
driver.get(url)

# Dinamik sayfanın yüklenmesi için biraz bekleyin
time.sleep(5)

# Üniversite isimleri ve sıralamaları gibi verileri toplayın
universities = []
rankings = []

# Verilerin bulunduğu tabloyu locate edelim
rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')

for row in rows:
    try:
        ranking = row.find_element(By.CSS_SELECTOR, 'td.rank').text
        university = row.find_element(By.CSS_SELECTOR, 'td.institution a').text
        universities.append(university)
        rankings.append(ranking)
    except:
        pass  # Her satırda bu veriler olmayabilir

# Sıralama verilerini bir DataFrame'e koyun
df = pd.DataFrame({
    'Rank': rankings,
    'University': universities
})

# Excel'e yazdırın
df.to_excel("times_higher_education_rankings.xlsx", index=False)

# Tarayıcıyı kapatın
driver.quit()

print("Veriler başarıyla Excel dosyasına kaydedildi!")
