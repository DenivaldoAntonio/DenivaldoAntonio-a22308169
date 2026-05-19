from django.urls import path

from . import views


urlpatterns = [

    # HOME
    path(
        '',
        views.portfolio_view,
        name='home'
    ),

    # UCs
    path(
        'ucs/',
        views.ucs_view,
        name='ucs'
    ),

    path(
        'ucs/criar/',
        views.criar_uc,
        name='criar_uc'
    ),

    path(
        'ucs/editar/<int:id>/',
        views.editar_uc,
        name='editar_uc'
    ),

    path(
        'ucs/apagar/<int:id>/',
        views.apagar_uc,
        name='apagar_uc'
    ),

    # DOCENTES
    path(
        'docentes/',
        views.docentes_view,
        name='docentes'
    ),

    path(
        'docentes/criar/',
        views.criar_docente,
        name='criar_docente'
    ),

    path(
        'docentes/editar/<int:id>/',
        views.editar_docente,
        name='editar_docente'
    ),

    path(
        'docentes/apagar/<int:id>/',
        views.apagar_docente,
        name='apagar_docente'
    ),

    path(
    'tecnologias/',
    views.tecnologias_view,
    name='tecnologias'
),

path(
    'tecnologias/criar/',
    views.criar_tecnologia,
    name='criar_tecnologia'
),

path(
    'tecnologias/editar/<int:id>/',
    views.editar_tecnologia,
    name='editar_tecnologia'
),

path(
    'tecnologias/apagar/<int:id>/',
    views.apagar_tecnologia,
    name='apagar_tecnologia'
),

path('competencias/', views.competencias_view, name='competencias'),
path('projetos/', views.projetos_view, name='projetos'),
path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
path('formacoes/', views.formacoes_view, name='formacoes'),
path('makingofs/', views.makingofs_view, name='makingofs'),
path('tfcs/', views.tfcs_view, name='tfcs'),

]

