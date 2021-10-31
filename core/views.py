from django.views.generic import ListView
from django.shortcuts import render
from .filters import ProdutoFilter
from .models import Produto
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from core.forms import ProdutoModelForm
import datetime


class ProdutoListView(LoginRequiredMixin, ListView):
    template_name = "core/produtos.html"
    paginate_by = 10
    model = Produto
    ordering = 'id'


@login_required
def produto(request, id):
    produto = Produto.objects.get(id=id)
    context = {
        'produto': produto
    }
    return render(request, "core/produto.html", context)


def produto_form(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
    
            form.save(Produto)
            form = ProdutoModelForm()
    context = {
        'form': form
    }


    return render(request, 'core/cadastrar_produto.html', context)

class BuscaListView(LoginRequiredMixin, ListView):
    template_name = "core/busca.html"
    paginate_by = 10
    model = Produto
    ordering = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProdutoFilter(self.request.GET, queryset=self.get_queryset())
        return context


def raiz(request):
    return redirect('/produtos')


def logout_view(request):
    logout(request)
    return redirect('/')
