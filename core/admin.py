from django.contrib import admin

from .models import Produto, ClasseDePerigo, LocalArmazenamento, SimboloGHS, SubClassesDePerigo

admin.site.register(Produto)
admin.site.register(ClasseDePerigo)
admin.site.register(LocalArmazenamento)
admin.site.register(SimboloGHS)

class SubClasseName(admin.ModelAdmin):
    List_display=['Nome']
admin.site.register(SubClassesDePerigo)