from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from  rest_framework.status import(
    HTTP_201_CREATED, HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN, HTTP_200_OK,
)

from rest_framework.views import APIView

from mainapp.serializers import(
    RegistrationSerializer, 
    AuthenticationSeriallizer
)

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if User.objects.filter(username=username).exists():
            return Response(
                {'message': 'Пользоваетель с таким именем существует'},
                status=HTTP_403_FORBIDDEN
            )
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        token = Token.objects.create(user=user)
        return Response({'token': token.key}, HTTP_201_CREATED)
    
class AuthenticationVeiw(APIView):
    def post(self, request):
        serializer = AuthenticationSeriallizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username).first()

        if user is not None:
            if check_password(password, user.password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, HTTP_200_OK)
            return Response({"error": 'Пароль не верный'}, HTTP_400_BAD_REQUEST)
        return Response({"error": 'Такой пользователь не существует'}, HTTP_400_BAD_REQUEST)