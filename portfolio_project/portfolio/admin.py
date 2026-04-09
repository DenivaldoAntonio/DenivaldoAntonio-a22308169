from django.contrib import admin
from .models import *

@admin.register(SobreMim)
class SobreMimAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "email",
        "linkedin",
        "github"
    )

    search_fields = (
        "nome",
        "email"
    )


@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "sigla",
        "instituicao",
        "ano_inicio"
    )

    list_filter = (
        "instituicao",
        "ano_inicio"
    )

    search_fields = (
        "nome",
        "sigla"
    )

    ordering = ("nome",)


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "codigo",
        "ects",
        "semestre",
        "licenciatura"
    )

    list_filter = (
        "licenciatura",
        "ects",
        "semestre"
    )

    search_fields = (
        "nome",
        "codigo"
    )

    ordering = ("nome",)


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "email"
    )

    search_fields = (
        "nome",
        "email"
    )

    filter_horizontal = (
        "unidades",
    )

    ordering = ("nome",)


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "nivel_interesse"
    )

    list_filter = (
        "nivel_interesse",
    )

    search_fields = (
        "nome",
    )

    ordering = ("nome",)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "data",
        "unidade",
        "github"
    )

    list_filter = (
        "data",
        "unidade",
        "tecnologias"
    )

    search_fields = (
        "titulo",
        "descricao"
    )

    filter_horizontal = (
        "tecnologias",
    )

    ordering = ("-data",)


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "nivel"
    )

    list_filter = (
        "nivel",
        "tecnologias"
    )

    search_fields = (
        "nome",
    )

    filter_horizontal = (
        "tecnologias",
        "projetos"
    )

    ordering = ("nivel",)


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "entidade",
        "data_inicio",
        "data_fim"
    )

    list_filter = (
        "entidade",
        "data_inicio"
    )

    search_fields = (
        "nome",
        "entidade"
    )

    ordering = ("-data_inicio",)


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "autor",
        "ano",
        "interesse"
    )

    list_filter = (
        "ano",
        "interesse",
        "tecnologias"
    )

    search_fields = (
        "titulo",
    )

    filter_horizontal = (
        "tecnologias",
    )

    ordering = ("-ano",)


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "data"
    )

    list_filter = (
        "data",
    )

    search_fields = (
        "titulo",
    )

    ordering = ("-data",)