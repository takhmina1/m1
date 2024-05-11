from rest_framework import serializers
from .models import CarAd

class CarAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAd
        fields = '__all__'
# serializers.py

from rest_framework import serializers

class RegistrationSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

# serializers.py

from rest_framework import serializers
from .models import *  # Замените на актуальную модель пользователя

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourUserModel  # Замените на актуальную модель пользователя
        fields = ['phone_number']  # Замените на актуальные поля модели

    def create(self, validated_data):
        """
        Создает и возвращает новый объект пользователя на основе валидированных данных.
        """
        # Пример: Создание нового пользователя, используя модель YourUserModel
        user = YourUserModel.objects.create(**validated_data)

        return user
