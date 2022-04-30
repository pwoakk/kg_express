from django.contrib import admin
from django.urls import path, include

from backend.apps.accounts.views import LoginView, UserRegisterView, RegisterDoneView, user_logout

urlpatterns = [
    path('login/', LoginView.as_view(), name='sign_in'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('logout/', user_logout, name='logout')
]