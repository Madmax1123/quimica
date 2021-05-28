from django.views.generic import ListView
from django.shortcuts import render
from .filters import ProdutoFilter
from .models import Produto
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import datetime


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, "core/produtos.html")
    else:
        return render(request, "core/produtos.html")


class ProdutoListView(ListView):
    template_name = "core/produtos.html"
    paginate_by = 10
    model = Produto
    ordering = 'id'


def produto(request, id):
    produto = Produto.objects.get(id=id)
    context = {
        'produto': produto
    }
    return render(request, "core/produto.html", context)


class BuscaListView(ListView):
    template_name = "core/busca.html"
    paginate_by = 10
    model = Produto
    ordering = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProdutoFilter(self.request.GET, queryset=self.get_queryset())
        return context
