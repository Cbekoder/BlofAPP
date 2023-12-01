from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if password != repassword:
            messages.error(request, 'Passwordlar mos kelmadi.')
            return redirect('/register/')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Foydalanuvchi nomi tizimda mavjud. Boshqa foydalanuvchi nomidan foydalaning.')
            return redirect('/register/')
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, 'Hisob muvaffaqiyatli yaratildi')
        login(request, user)
        return redirect('/addAuthor/')

class AddInfoView(View):
    def get(self, request):
        return render(request, 'register2.html')

    def post(self, request):
        if request.user.is_authenticated:
            Muallif.objects.create(
                ism = request.POST.get('ism'),
                yosh = request.POST.get('yosh'),
                kasb = request.POST.get('kasb'),
                userid = request.user
            )
            return redirect("/")
        return redirect('/addAuthor/')
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is None:
            return redirect("/login/")
        login(request, user)
        return redirect('/')

class HomeView(View):
    def get(self, request):
        content = {
            'user' : request.user
        }
        return render(request, 'index.html')

class addarticleView(View):
    def get(self, request):
        return render(request, "newArticle.html")

    def post(self, request):
        if request.user.is_authenticated:
            Maqola.objects.create(
                sarlavha = request.POST.get('sarlavha'),
                sana = request.POST.get('sana'),
                mavzu = request.POST.get('mavzu'),
                matn = request.POST.get('matn'),
                muallif = request.user
            )
            return redirect("/")
        return redirect('/login/')


def logout_view(request):
    logout(request)
    return redirect("/login")