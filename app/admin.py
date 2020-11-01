from django.contrib import admin
from app.data_access.models import *

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    model = Contato
    list_display = ('nome', 'email', 'assunto', 'data')
    search_fields = ['nome', 'email', 'assunto', 'data']
    readonly_fields = ('data', 'nome', 'email', 'assunto', 'mensagem')

class PublicacaoAdmin(admin.ModelAdmin):
    model = Publicacao
    list_display = ('titulo', 'publicado_por', 'data_publicacao')


admin.site.register(Sobre)
admin.site.register(Eventos)
admin.site.register(Ladies)
admin.site.register(Publicacao, PublicacaoAdmin)
admin.site.register(Contato, ContatoAdmin)