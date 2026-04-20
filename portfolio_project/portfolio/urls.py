## portfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('', views.portfolio_view, name='home'),

    path('uc/', views.ucs_view, name='uc'),

    path('docentes/', views.docentes_view, name='docentes'),

]