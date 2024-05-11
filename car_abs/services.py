# services.py

import requests
from django.conf import settings

def send_sms_custom(phone, message, code):
    new_phone = "".join(filter(str.isdigit, phone))
    xml_data = f"""<?xml version="1.0" encoding="UTF-8"?>
                 <message>
                     <login>{settings.NIKITA_LOGIN}</login>
                     <pwd>{settings.NIKITA_PASSWORD}</pwd>
                     <sender>{settings.NIKITA_SENDER}</sender>
                     <text>{message} {code}</text>
                     <phones>
                         <phone>{new_phone}</phone>
                     </phones>
                 </message>"""

    headers = {"Content-Type": "application/xml"}
    url = "https://smspro.nikita.kg/api/message"

    try:
        response = requests.post(url, data=xml_data.encode("utf-8"), headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False
