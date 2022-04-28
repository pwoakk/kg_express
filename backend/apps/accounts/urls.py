from django.contrib import admin
from django.urls import path, include

from backend.apps.accounts.views import LoginView, UserRegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='sign_in'),
    path('register/', UserRegisterView.as_view(), name='register'),

]