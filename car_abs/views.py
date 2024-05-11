# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .services import send_sms_custom

# class SendSMSView(APIView):
#     def post(self, request, *args, **kwargs):
#         # Получаем данные из запроса
#         phone = request.data.get('phone')
#         message = request.data.get('message')
#         code = request.data.get('code')

#         # Проверяем, что все данные предоставлены
#         if not all([phone, message, code]):
#             return Response({"error": "Некорректные данные."}, status=status.HTTP_400_BAD_REQUEST)

#         # Отправляем SMS
#         success = send_sms_custom(phone, message, code)

#         if success:
#             return Response({"success": True, "message": "SMS успешно отправлено."}, status=status.HTTP_200_OK)
#         else:
#             return Response({"success": False, "message": "Ошибка при отправке SMS."}, status=status.HTTP_400_BAD_REQUEST)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests

class SendSMSView(APIView):
    def post(self, request, *args, **kwargs):
        # Получаем данные из запроса
        phone = request.data.get('phone')
        message = request.data.get('message')
        code = request.data.get('code')

        # Проверяем, что все данные предоставлены
        if not all([phone, message, code]):
            return Response({"error": "Некорректные данные."}, status=status.HTTP_400_BAD_REQUEST)

        # Отправляем SMS
        success = send_sms(phone, message, code)

        if success:
            return Response({"success": True, "message": "SMS успешно отправлено."}, status=status.HTTP_200_OK)
        else:
            return Response({"success": False, "message": "Ошибка при отправке SMS."}, status=status.HTTP_400_BAD_REQUEST)

def send_sms(phone, message, code):
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


# views.py

# from django.contrib.auth import get_user_model
# from django.shortcuts import render

# def create_user(request):
#     User = get_user_model()
#     user = User.objects.create_user(email='another_user@example.com', password='password')
#     return render(request, 'your_template.html', {'user': user})


# views.py

from django.contrib.auth import get_user_model
from django.shortcuts import render

def create_user(request):
    User = get_user_model()
    user = User.objects.create_user(email='another_user@example.com', password='password')
    return render(request, 'your_template.html', {'user': user})
