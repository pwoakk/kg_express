from abc import ABC

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import LoginForm, UserRegisterForm, UserUpdateForm
from .models import User


class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponse('Ваш аккаунт неактивен')
        return HttpResponse('Такого пользователя не существует')


class UserRegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('register_done')


# generic - готовые классы с готовыми решениями, для стандартных задач
class RegisterDoneView(generic.TemplateView):
    template_name = 'register_done.html'


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        if self.kwargs.get('pk') == self.request.user.pk:
            return True
        return False


# обновление через функцию
# @login_required   # проверка на залогининность
# def update_user_profile(request, pk):
#     if request.user.pk != pk:     # закрыть доступ изменения других пользователей
#         return HttpResponseForbidden()
#     if request.method == "POST":
#         form = UserUpdateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         try:
#             user=User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404
#         form = UserUpdateForm(instance=user)        # если указать instance форма будет заполнена данными user
#     context = {
#         "form": form
#     }
#     return render(request, 'user_update.html', context)
