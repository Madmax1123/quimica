from django.db import models


class SubClassesDePerigo(models.Model):
    nome = models.CharField('Nome', max_length=500)

    def __str__(self):
        return f'{self.nome}'


class ClasseDePerigo(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return f'{self.nome}'


class SimboloGHS(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return f'{self.nome}'


class LocalArmazenamento(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return f'{self.nome}'


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sinonimo = models.CharField('Sinonimo', max_length=100)
    classe_de_perigo = models.ForeignKey(ClasseDePerigo, on_delete=models.CASCADE)
    sub_classe_de_perigo = models.ForeignKey(SubClassesDePerigo, on_delete=models.CASCADE)
    simbolo_ghs = models.ForeignKey(SimboloGHS, on_delete=models.CASCADE)
    incompatibilidade = models.CharField('Incompatibilidade', max_length=100)
    local_armazenamento = models.ForeignKey(LocalArmazenamento, on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade')
    lote = models.CharField('Lote', max_length=100)
    validate = models.DateTimeField('Data de Validade')
    link_FISPQ = models.CharField('link FISPQ', max_length=100)
    residuo = models.CharField('Residuo', max_length=100)

    def __str__(self):
        return self.nome
