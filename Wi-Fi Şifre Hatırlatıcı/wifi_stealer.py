import subprocess
import re

def get_wifi_passwords():
    print("🔍 Kayıtlı Wi-Fi ağları taranıyor...\n")
    
    try:
        # 1. Tüm profilleri listele
        # Türkçe karakter sorunu olmaması için encoding='cp857' (Windows Türkçe Terminal kodlaması) kullanıyoruz
        profiles_data = subprocess.check_output(["netsh", "wlan", "show", "profiles"], encoding='cp857', errors='ignore')
        
        # Profil isimlerini regex ile bul
        profile_names = re.findall(r"All User Profile\s*:\s*(.*)", profiles_data)
        
        # İngilizce Windows kullanıyorsan yukarıdaki satır çalışmazsa şunu dene:
        if not profile_names:
             profile_names = re.findall(r"Tüm Kullanıcı Profilleri\s*:\s*(.*)", profiles_data)

        wifi_list = []

        if len(profile_names) == 0:
            print("⚠️ Hiçbir kayıtlı ağ bulunamadı.")
            return

        for name in profile_names:
            name = name.strip() # Boşlukları temizle
            
            try:
                # Her profil için şifreyi (key=clear) iste
                results = subprocess.check_output(
                    ["netsh", "wlan", "show", "profile", name, "key=clear"], 
                    encoding='cp857', errors='ignore'
                )
                
                # Şifre satırını bul (Türkçe Windows için "Anahtar İçeriği", İngilizce için "Key Content")
                password_match = re.search(r"(Key Content|Anahtar İçeriği)\s*:\s*(.*)", results)
                
                if password_match:
                    wifi_password = password_match.group(2)
                else:
                    wifi_password = "(Şifre Yok veya Okunamadı)"
                
                wifi_list.append({"SSID": name, "Password": wifi_password})
                
            except subprocess.CalledProcessError:
                print(f"❌ {name} ağına erişilemedi.")

        # Sonuçları Yazdır
        print(f"{'Wi-Fi Ağı (SSID)':<30} | {'Şifre'}")
        print("-" * 50)
        
        for wifi in wifi_list:
            print(f"{wifi['SSID']:<30} | {wifi['Password']}")
            
        input("\nÇıkmak için Enter'a bas...")

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    get_wifi_passwords()