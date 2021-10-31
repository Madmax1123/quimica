from django import forms
from core.models import Produto


class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['nome', 'sinonimo', 'incompatibilidade', 'quantidade', 'lote', 'residuo', 'link_FISPQ', 'validate', 'local_armazenamento', 'simbolo_ghs', 'sub_classe_de_perigo', 'classe_de_perigo']
