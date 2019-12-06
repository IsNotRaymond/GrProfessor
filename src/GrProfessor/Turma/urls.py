from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboardView, name='dashboard'),
    path('criar_turma/', views.TurmaView, name='criar-turma'),
    path('turma/', views.detailTurmaView, name='turma'),
]
