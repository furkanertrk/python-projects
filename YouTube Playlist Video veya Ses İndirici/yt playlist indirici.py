from pytubefix import Playlist, YouTube
import sys

def ilerleme_takibi(stream, chunk, bytes_remaining):
    toplam_boyut = stream.filesize
    indirilen = toplam_boyut - bytes_remaining
    yuzde = (indirilen / toplam_boyut) * 100
    
    sys.stdout.write("\rIndirme Durumu: %{:.2f}".format(yuzde))
    sys.stdout.flush()

def main():
    link = input("Playlist Linkini yapistir: ")
    
    try:
        pl = Playlist(link)
        try:
            baslik = pl.title
        except:
            baslik = "Oynatma Listesi"

        print("\nPlaylist Adi: {}".format(baslik))
        print("Toplam Video Sayisi: {}".format(len(pl.video_urls)))
        print("-" * 40)
        
        print("1- Tum videolari indir (Izlenebilir En Yuksek Kalite)")
        print("2- Tum sesleri indir (MP3/M4A)")
        
        secim = input("Seciminiz (1-2): ")
        
        print("\nIslem basliyor... Bu biraz zaman alabilir.")
        
        sayac = 1
        for video_url in pl.video_urls:
            try:
                yt = YouTube(video_url, on_progress_callback=ilerleme_takibi)
                
                print("\n\n[{}/{}] Islenen: {}".format(sayac, len(pl.video_urls), yt.title))
                
                if secim == "1":
                    yayin = yt.streams.get_highest_resolution()
                    yayin.download()
                    
                elif secim == "2":
                    yayin = yt.streams.get_audio_only()
                    yayin.download(filename_prefix="ses_")
                
                print("\nTamamlandi!")
                sayac += 1
                
            except Exception as hata:
                print("\nBu video indirilemedi: {}".format(hata))
                sayac += 1
                continue
        
        print("\n" + "="*40)
        print("Tum playlist indirme islemi bitti!")

    except Exception as e:
        print("Playlist baglantisinda sorun var: {}".format(e))

if __name__ == "__main__":
    main()