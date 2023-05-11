from django.urls import path
from mainapp.views import RegistrationView, AuthenticationVeiw

urlpatterns = [
    path('reg/', RegistrationView.as_view()),
    path('auth/', AuthenticationVeiw.as_view()),
]