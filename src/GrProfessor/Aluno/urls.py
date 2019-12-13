from django.urls import path
from . import views

urlpatterns = [
    path('upload_csv/<int:id_turma>', views.uploadAlunosView, name='upload-csv'),
    path('listar_alunos/<int:id_turma>/', views.detailAlunoView, name='aluno'),
    path('aluno/criar/<int:id_turma>/', views.createAlunoView, name='criar-aluno'),
    path('aluno/editar/<int:id_turma>/<int:id_aluno>/', views.updateAlunoView, name='editar-aluno'),
    path('aluno/deletar/<int:id_turma>/<int:id_aluno>/', views.deleteAlunoView, name='deletar-aluno'),
]
