from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('produtos', views.ProdutoListView.as_view(), name='produtos'),
    path('produto/<int:id>', views.produto, name='produto'),
    path('busca', views.BuscaListView.as_view(), name='busca'),
]