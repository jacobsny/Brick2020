import smtplib

from email.message import EmailMessage

def send_ingredients(ingredients, provider, phone_number):
    msg = EmailMessage()
    str = "Constellation Cocktails -- Your Ingredients\n"
    for i in ingredients:
        str += i + ",\n"
    str += "Thank you for choosing Constellation Cocktails"
    msg.set_content(str)
    provider_to_address = {"Verizon": "@vtext.com"}
    msg['To'] = phone_number + provider_to_address[provider]
    msg["From"] = "brickhacks_Joe@gmail.com"

    s = smtplib.SMTP('localhost', 8080)
    s.send_message(msg)
    s.quit()


if __name__ == '__main__':
    send_ingredients(["sup joe"],"Verizon","7166970452")