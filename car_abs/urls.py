# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import *
# from .services import *
# from .views import SendSMSView

# urlpatterns = [
#     path('api/', include(router.urls)),
#     path('send-sms/', SendSMSView.as_view(), name='send_sms'),
#     # Добавьте другие URL-шаблоны, если необходимо
# ]

# # router.register(r'car-ads', CarAdViewSet, basename='carad')




from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
# router.register(r'car-ads', CarAdViewSet, basename='carad')

urlpatterns = [
    path('api/', include(router.urls)),
    # path('send-sms/', SendSMSView.as_view(), name='send_sms'),
    path('send-sms/', SendSMSView.as_view(), name='send_sms'),
    # Добавьте другие URL-шаблоны, если необходимо
]
