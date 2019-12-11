from django.urls import path, include
from . import views

urlpatterns = [
    path('turma/criar/', views.turmaFormView, name='criar-turma'),
    path('turma/<int:id>/', views.detailTurmaView, name='turma'),
    path('turma/editar/<int:id>/', views.updateTurmaView, name='editar-turma'),
    path('turma/deletar/<int:id>/', views.deleteTurmaView, name='deletar-turma'),
    path('turma/', include('GrProfessor.Aluno.urls')),
]
