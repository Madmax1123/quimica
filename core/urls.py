from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('contas/', include('django.contrib.auth.urls')),
    path('produtos', views.ProdutoListView.as_view(), name='produtos'),
    path('cadastrar_produto', views.produto_form, name='cadastrar_produto'),
    path('produto/<int:id>', views.produto, name='produto'),
    path('busca', views.BuscaListView.as_view(), name='busca'),
    path('', views.raiz, name='raiz'),
    path('sair', views.logout_view, name='sair'),
]