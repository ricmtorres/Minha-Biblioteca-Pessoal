from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('adicionar_livro/', views.adicionar_livro, name='adicionar_livro'),
    path('personalizar/', views.personalizar, name='personalizar'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
]