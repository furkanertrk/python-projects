import subprocess
import re

print("🔍 Kayıtlı Wi-Fi ağları taranıyor...\n")

try:
    profiles_data = subprocess.check_output(["netsh", "wlan", "show", "profiles"], encoding='cp857', errors='ignore')
    
    profile_names = re.findall(r"All User Profile\s*:\s*(.*)", profiles_data)
    
    if not profile_names:
            profile_names = re.findall(r"Tüm Kullanıcı Profilleri\s*:\s*(.*)", profiles_data)

    wifi_list = []

    if len(profile_names) == 0:
        print("⚠️ Hiçbir kayıtlı ağ bulunamadı.")
        exit(0)

    for name in profile_names:
        name = name.strip()
        
        try:
            results = subprocess.check_output(
                ["netsh", "wlan", "show", "profile", name, "key=clear"], 
                encoding='cp857', errors='ignore'
            )
            
            password_match = re.search(r"(Key Content|Anahtar İçeriği)\s*:\s*(.*)", results)
            
            if password_match:
                wifi_password = password_match.group(2)
            else:
                wifi_password = "(Şifre Yok veya Okunamadı)"
            
            wifi_list.append({"SSID": name, "Password": wifi_password})
            
        except subprocess.CalledProcessError:
            print(f"❌ {name} ağına erişilemedi.")

    print(f"{'Wi-Fi Ağı (SSID)':<30} | {'Şifre'}")
    print("-" * 50)
    
    for wifi in wifi_list:
        print(f"{wifi['SSID']:<30} | {wifi['Password']}")
        
    input("\nÇıkmak için Enter'a bas...")

except Exception as e:
    print(f"Bir hata oluştu: {e}")
