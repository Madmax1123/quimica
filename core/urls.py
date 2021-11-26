from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('contas/', include('django.contrib.auth.urls')),
    path('produtos', views.ProdutoListView.as_view(), name='produtos'),
    path('contato', views.contato, name='contato'),
    path('test', views.test, name='test'),
    path('produto/<int:id>', views.produto, name='produto'),
    path('criarconta', views.criarconta, name='criarconta'),
    path('busca', views.BuscaListView.as_view(), name='busca'),
    path('', views.raiz, name='raiz'),
    path('criarconta', views.criarconta, name='criarconta'),
    path('sair', views.logout_view, name='sair'),
]