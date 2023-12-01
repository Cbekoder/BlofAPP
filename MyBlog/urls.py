from django.contrib import admin
from django.urls import path
from Blogapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('register/', RegisterView.as_view()),
    path('addAuthor/', AddInfoView.as_view()),
    path('newArticle/', addarticleView.as_view()),
    path('maqola/<int:pk>', MaqolaView.as_view()),
    path('bloglar/', BlogView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', logout_view),
]
