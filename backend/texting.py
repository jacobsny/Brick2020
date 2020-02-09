import smtplib


def send_ingredients(ingredients, provider, phone_number):
    msg = "\nConstellation Cocktails -- Your Ingredients:\n"
    for i in ingredients:
        msg += i + ",\n"
    msg += "Thank you for choosing Constellation Cocktails!"
    provider_to_address = {"Verizon": "@vtext.com", "Alltel": "@message.alltel.com",
                           "ATT": "@txt.att.net", "Tmobile": "@tmomail.net",
                           "Virgin": "@vmobl.com", "Sprint": "@messaging.sprintpcs.com",
                           "Nextel": "@messaging.nextel.com", "UsCell": "@mms.uscc.net"}
    to_addr = phone_number + provider_to_address[provider]
    from_addr = "constellationcocktails@gmail.com"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(from_addr, "JacobIsAnAlcoholic")
    # print(msg)
    s.sendmail(from_addr, to_addr, msg)
    s.close()


if __name__ == '__main__':
    send_ingredients(["Hello", "John", "Yeet"], "Verizon", "7162204247")