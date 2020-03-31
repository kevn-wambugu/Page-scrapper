import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = "https://www.jumia.co.ke/usb-type-c-to-usb-adapter-3-port-adapter-with-type-c-hdmi-usb-3.0-for-chromebook-pixel-macbook-pro-macbook-lbq-generic-mpg212085.html"
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
def check_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(attrs={'-fs20 -pts -pbxs'}).get_text()
    price = soup.find(attrs={"-b -ltr -tal -fs24"}).get_text()

    price = price[4:9]
    converted_price = float(price.replace(",", ''))
    print(converted_price)
    print(title.strip())

    if converted_price < 1400:
        send_mail() 
    else:
       mail_2()


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("wambugunjoroge23@gmail.com", "mjko tzeb rpxc ierw")

    subject = "PRICES FOR USB HDMI CONNECTOR JUMIA AND KILLMALL"
    body = 'Check link! https://www.jumia.co.ke/usb-type-c-to-usb-adapter-3-port-adapter-with-type-c-hdmi-usb-3.0-for-chromebook-pixel-macbook-pro-macbook-lbq-generic-mpg212085.html FOR JUMIA.'
    msg = f"SUBJECT {subject}\n\n{body}"
    server.sendmail(
        'wambugunjoroge23@gmail.com',
        'njorogekevn@gmail.com',
        msg
    )
    print("EMAIL HAS BEEN SENT!!!!!")
    server.quit()

def mail_2():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("wambugunjoroge23@gmail.com", "mjko tzeb rpxc ierw")

    subject = "PRICES FOR USB HDMI CONNECTOR IN KILLMALL AND JUMIA"
    body = "The prices for the USB-HDMI cable have not gone down."
    msg = f"{subject}\n\n{body}"
    server.sendmail(
        'wambugunjoroge23@gmail.com',
        'njorogekevn@gmail.com',
        msg
    )
    print("EMAIL HAS BEEN SENT!!!!!")
    server.quit()

while(True):
    check_price()
    time.sleep(604800)
    