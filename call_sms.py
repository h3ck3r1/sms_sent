from twilio.rest import Client
import random
import string


def banner():
    font = """
           
  __  __ _____      _    _          _____ ____  ______ _____ _____ 
 |  \/  |  __ \    | |  | |   /\   / ____/ __ \|  ____|_   _/ ____|
 | \  / | |__) |   | |__| |  /  \ | |   | |  | | |__    | || |     
 | |\/| |  _  /    |  __  | / /\ \| |   | |  | |  __|   | || |     
 | |  | | | \ \ _  | |  | |/ ____ \ |___| |__| | |     _| || |____ 
 |_|  |_|_|  \_(_) |_|  |_/_/    \_\_____\____/|_|    |_____\_____|
                                                                   
                                                                   
"""
    print(font)

if __name__ == "__main__":
    banner()
    

# Twilio hesap bilgilerini girin
account_sid = 'SID'
auth_token = 'TOKEN'
twilio_phone_number = 'NUMBER'


to_phone_number = input("Lütfen hedef telefon numarasını girin (+1234567890 formatında): ")


def generate_random_message():
    message = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    return message


client = Client(account_sid, auth_token)

try:
    message = generate_random_message()

 
    sent_message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=to_phone_number
    )

    print(f"Mesaj gönderildi: {sent_message.sid}")

except Exception as e:
    print(f"Hata: {str(e)}")
