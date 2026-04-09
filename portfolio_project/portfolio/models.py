from django.db import models


class Licenciatura(models.Model):

    nome = models.CharField(max_length=200)

    sigla = models.CharField(max_length=20)

    instituicao = models.CharField(max_length=200)

    descricao = models.TextField(blank=True)

    ano_inicio = models.IntegerField(blank=True, null=True)

    def __str__(self):

        return self.nome


class UnidadeCurricular(models.Model):

    nome = models.CharField(max_length=200)

    codigo = models.CharField(max_length=20)

    ects = models.IntegerField()

    semestre = models.IntegerField()

    descricao = models.TextField(blank=True)

    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)

    def __str__(self):

        return self.nome


class Docente(models.Model):

    nome = models.CharField(max_length=200)

    email = models.EmailField(blank=True)

    pagina_lusofona = models.URLField(blank=True)

    unidades = models.ManyToManyField(UnidadeCurricular, blank=True)

    def __str__(self):

        return self.nome


class Tecnologia(models.Model):

    nome = models.CharField(max_length=100)

    descricao = models.TextField(blank=True)

    website = models.URLField(blank=True)

    nivel_interesse = models.IntegerField(blank=True, null=True)

    def __str__(self):

        return self.nome


class Projeto(models.Model):

    titulo = models.CharField(max_length=200)

    descricao = models.TextField(blank=True)

    conceitos = models.TextField(blank=True)

    github = models.URLField(blank=True)

    data = models.DateField(blank=True, null=True)

    unidade = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, blank=True, null=True)

    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    def __str__(self):

        return self.titulo


class Competencia(models.Model):

    nome = models.CharField(max_length=100)

    descricao = models.TextField(blank=True)

    nivel = models.IntegerField(blank=True, null=True)

    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    projetos = models.ManyToManyField(Projeto, blank=True)

    def __str__(self):

        return self.nome


class Formacao(models.Model):

    nome = models.CharField(max_length=200)

    entidade = models.CharField(max_length=200, blank=True)

    data_inicio = models.DateField(blank=True, null=True)

    data_fim = models.DateField(blank=True, null=True)

    descricao = models.TextField(blank=True)

    certificado = models.URLField(blank=True)

    def __str__(self):

        return self.nome


class TFC(models.Model):

    titulo = models.CharField(max_length=200)

    autor = models.CharField(max_length=100, blank=True)

    ano = models.IntegerField(blank=True, null=True)

    descricao = models.TextField(blank=True)

    interesse = models.IntegerField(blank=True, null=True)

    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    def __str__(self):

        return self.titulo


class MakingOf(models.Model):

    titulo = models.CharField(max_length=200)

    descricao = models.TextField(blank=True)

    data = models.DateField(blank=True, null=True)

    def __str__(self):

        return self.titulo
    

class SobreMim(models.Model):

    nome = models.CharField(max_length=200)

    biografia = models.TextField()

    email = models.EmailField(blank=True)

    linkedin = models.URLField(blank=True)

    github = models.URLField(blank=True)

    objetivo_profissional = models.TextField(blank=True)