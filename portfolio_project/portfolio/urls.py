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
]