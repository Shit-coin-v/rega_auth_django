from rest_framework import serializers, exceptions

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    def validated_password(self, value):
        if len(value) < 6:
            raise exceptions.ValidationError('Пароль слишком короткий')                   # Возращает ошибку
        elif len(value) > 20:
            raise exceptions.ValidationError('Пароль слишком длинный')
        return value

class AuthenticationSeriallizer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

{
    "username": "Vasya",
    "password": "123456",
    "email": "diva8688@mail.com"
}

{
    "username": "Vasya",
    "password": "123456"
}