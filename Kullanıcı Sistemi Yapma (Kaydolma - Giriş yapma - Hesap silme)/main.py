from database import *

def print_menu():
    print("""
        1-Giriş
        2-Kaydol
        3-Kapat
        
    """)
create_table()
def login_menu(user):
    print(f"""
        Giriş yapılmış hesap: {user[1]},{user[2]},{user[3]}
        
        1-Hesap Ara
        2-Tüm Hesapları Göster
        3-Hesabımı Sil
        4-Çıkış Yap
        
    """)
while True:
    print_menu()
    secim = input("Seçim: ")

    if secim == "1":
        username = input("Kullanıcı Adı: ")
        password = input("Şifre: ")
        searh = search_user(username)
        if searh == None:
            print("Böyle bir kullanıcı yok!")
            continue
        if password == searh[4]:
            while True:
                login_menu(searh)
                sec = input("Seçim:")
                if sec == "1":
                    u = input("Kullanıcı adı:")
                    birini_arama = search_user(u)
                    if birini_arama == None:
                        print("Böyle bir kullanıcı bulunamadı.")
                        continue
                    print("\nBulunan Hesap ==> " f"{birini_arama[1]},{birini_arama[2]},{birini_arama[3]}")
                if sec == "2":
                    print_all()
                if sec == "3":
                    delete_account(username)
                    print("Çıkış yaptığınızda hesabınız silinmiş olacak!!!")
                if sec == "4":
                    break

    if secim == "2":
        name = input("Adınız: ")
        lastname = input("Soyadınız: ")
        username = input("Kullanıcı adınız: ")
        password = input("Şifreniz: ")
        searh = search_user(username)
        if searh != None:
            print("Bu kullanıcı adı alınmış!")
            continue
        insert(name,lastname,username,password)
        print("Kayıt başarıyla oluşturuldu!")
    if secim == "3":
        quit()
