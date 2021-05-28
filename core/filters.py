import django_filters
from .models import Produto


class ProdutoFilter(django_filters.FilterSet):

    class Meta:
        model = Produto
        fields = {
            'nome': ['icontains'],
        }
