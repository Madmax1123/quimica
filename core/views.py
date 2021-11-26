from django.views.generic import ListView
from django.shortcuts import render
from .filters import ProdutoFilter
from .models import Produto
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
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
    if request.method == 'POST':
        form = ProdutoModelForm(request.method)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
        else:
            form = ProdutoModelForm

    return render(request, 'core/cadastrar_produto.html', {"form":form})

class BuscaListView(LoginRequiredMixin, ListView):
    template_name = "core/busca.html"
    paginate_by = 10
    model = Produto
    ordering = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProdutoFilter(self.request.GET, queryset=self.get_queryset())
        return context

def test(request):
    return render(request, 'registration/test.html')

def criarconta(response):


    return render(response, 'registration/criarconta.html')


def raiz(request):
    return redirect('/produtos')

def criarconta(request):
    return render(request, 'registration/criarconta.html')

def logout_view(request):
    logout(request)
    return redirect('/')


def contato(request):
    return render(request, 'core/contato.html')