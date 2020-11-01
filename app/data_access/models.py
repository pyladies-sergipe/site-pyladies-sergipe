from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sobre(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=360)

    def __str__(self):
        return self.titulo

class Eventos(models.Model):
    nome = models.CharField(max_length=35)
    descricao = models.CharField(max_length=150)
    local = models.CharField(max_length=35)
    data = models.DateTimeField()
    link = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.nome

class Ladies(models.Model):
    foto = models.ImageField(upload_to='pyladiesSE_site/static/img/ladies')
    nome = models.CharField(max_length=35)
    biografia = models.TextField()
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    blog_pessoal = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Publicacao(models.Model):
    imagem = models.ImageField(upload_to='publicacoes', blank=True, null=True)
    titulo = models.CharField(max_length=150)
    resumo = models.CharField(max_length=100)
    texto = models.TextField()
    slug = models.SlugField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    publicado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

class Contato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    assunto = models.CharField(max_length=300)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + ' - ' + str(self.data)