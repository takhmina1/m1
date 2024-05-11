# # # from django.contrib import admin
# # # from .models import CarAd

# # # @admin.register(CarAd)
# # # class CarAdAdmin(admin.ModelAdmin):
# # #     listdisplay = ['id', 'adtype', 'cartype', 'makeandmodel', 'year', 'bodytype', 'buyingdisplay']
# # #     listfilter = ['adtype', 'cartype', 'year', 'buying']
# # #     searchfields = ['makeandmodel', 'year']

# # #     fieldsets = (
# # #         ('Общая информация', {
# # #             'fields': ('adtype', 'cartype', 'makeandmodel', 'year')
# # #         }),
# # #         ('Детали автомобиля', {
# # #             'fields': ('bodytype', 'generation', 'engine', 'drive', 'transmission', 'modification', 'steeringwheel')
# # #         }),
# # #         ('Детали сделки', {
# # #             'fields': ('buying',)
# # #         }),
# # #     )

# # #     def buyingdisplay(self, obj):
# # #         return obj.getbuyingdisplay()
# # #     buyingdisplay.shortdescription = 'Покупка'

# # #     def getreadonlyfields(self, request, obj=None):
# # #         if obj and obj.adtype == 'Покупка':
# # #             return [
# # #                 'adtype', 'cartype', 'makeandmodel', 'year', 'bodytype',
# # #                 'generation', 'engine', 'drive', 'transmission', 'modification',
# # #                 'steeringwheel'
# # #             ]
# # #         return []



# # from django.contrib import admin
# # from .models import CarAd

# # @admin.register(CarAd)
# # class CarAdAdmin(admin.ModelAdmin):
# #     listdisplay = ['id', 'adtype', 'cartype', 'makeandmodel', 'year', 'bodytype', 'buying']
# #     listfilter = ['adtype', 'cartype', 'year', 'buying']
# #     searchfields = ['makeandmodel', 'year']

# #     fieldsets = (
# #         ('Общая информация', {
# #             'fields': ('adtype', 'cartype', 'makeand_model', 'year')
# #         }),
# #         ('Детали автомобиля', {
# #             'fields': ('body_type', 'generation', 'engine', 'drive', 'transmission', 'modification', 'steering_wheel')
# #         }),
# #         ('Детали сделки', {
# #             'fields': ('buying',)
# #         }),
# #     )

# #     def get_readonly_fields(self, request, obj=None):
# #         if obj and obj.ad_type == 'Покупка':
# #             return [
# #                 'ad_type', 'car_type', 'make_and_model', 'year', 'body_type',
# #                 'generation', 'engine', 'drive', 'transmission', 'modification',
# #                 'steering_wheel'
# #             ]
# #         return []



# # from django.contrib import admin
# # from .models import CarAd

# # class CarAdAdmin(admin.ModelAdmin):
# #     list_display = ['id', 'car_type', 'make_and_model', 'year', 'ad_type', 'buying']
# #     list_filter = ['car_type', 'year', 'ad_type', 'buying']

# # a





# from django.contrib import admin
# from .models import *
# from django.contrib.auth.admin import UserAdmin




# from django.contrib.auth.models import AbstractUser
# from django.db import models


# admin.site.register(User)

# class User(AbstractUser):
#     # ваш код поля и методов здесь
#     REQUIRED_FIELDS = ['email']


# class CarAdAdmin(admin.ModelAdmin):
#     # Другие поля модели
#     list_display = ('get_brand', 'get_model', 'year', 'body_type', 'generation', 'engine', 'wheel_drive', 'transmission', 'modification', 'steering_wheel', 'color', 'condition', 'mileage', 'price', 'contact_region', 'phone_number')
#     search_fields = ('brand', 'model', 'year', 'contact_region', 'phone_number')
#     readonly_fields = ('options_display',)  # Добавляем поле только для чтения для отображения опций

#     def options_display(self, obj):
#         return obj.options  # Отображаем опции в админ-панели

#     options_display.short_description = 'Опции'  # Заголовок для отображения опций

#     def get_brand(self, obj):
#         return obj.brand

#     def get_model(self, obj):
#         return obj.model

# admin.site.register(CarAd, CarAdAdmin)
# class UserAdmin(admin.ModelAdmin):
#     list_filter = ('is_staff', 'is_active', 'groups')


# class UserAdmin(admin.ModelAdmin):
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')


# # в файле admin.py внутри вашего приложения (например, car_abs)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

# # Ваша модель UserAdmin
# class UserAdmin(BaseUserAdmin):
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

# # Регистрация модели User с использованием вашего UserAdmin
# # admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

# # Регистрация вашей пользовательской модели User с использованием вашего UserAdmin
# # admin.site.register(YourCustomUserModel, UserAdmin)






# @admin.register(YourUserModel)
# class UserAdmin(UserAdmin):
#     fieldsets = (
#         (
#             None,
#             {
#                 "fields": (
#                     "roll_request",
#                     "user_roll",
#                     "phone",
#                     "first_name",
#                     "last_name",
#                     "password",
#                     "bonus_id",
#                     "qrimg",
#                 )
#             },
#         ),
#         (
#            ("Детально"),
#             {
#                 "fields": (
#                     "email",
#                     "birthday",
#                     "gender",
#                     "language",
#                     "married",
#                     "status",
#                     "city",
#                     "children",
#                     "animal",
#                     "car",
#                 ),
#             },
#         ),
#         (
#            ("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#         (("Important dates"), {"fields": ("lastlogin", "datejoined")}),
#         (
#            ("Верификация"),
#             {
#                 "fields": (
#                     "activated",
#                     "code",
#                 )
#             },
#         ),
#     )
#     addfieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": (
#                     "phone",
#                     "firstname",
#                     "lastname",
#                     "password1",
#                     "password2",
#                 ),
#             },
#         ),
#     )

#     listdisplay = (
#         "id",
#         "phone",
#         "isstaff",
#     )
#     listdisplaylinks = (
#         "id",
#         "phone",
#     )
#     searchfields = (
#         "firstname",
#         "lastname",
#         "phone",
#         "email"
#     )
#     ordering = ("-id",)




from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import YourUserModel, CarAd

# Ваша модель UserAdmin
class UserAdmin(BaseUserAdmin):
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

# Регистрация модели User с использованием вашего UserAdmin
# admin.site.unregister(User)
admin.site.register(User, UserAdmin)


