from django.urls import path, include
from . import views

urlpatterns = [
    path('turma/criar/', views.createTurmaView, name='criar-turma'),
    path('turma/<int:id_turma>/', views.detailTurmaView, name='turma'),
    path('turma/editar/<int:id_turma>/', views.updateTurmaView, name='editar-turma'),
    path('turma/deletar/<int:id_turma>/', views.deleteTurmaView, name='deletar-turma'),
    path('turma/', include('GrProfessor.Aluno.urls')),
    path('turma/', include('GrProfessor.Grupo.urls')),
    path('turma/', include('GrProfessor.Atividade.urls')),
]
