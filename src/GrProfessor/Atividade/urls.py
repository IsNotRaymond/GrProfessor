from django.urls import path
from . import views

urlpatterns = [
    path('listar_atividades/<int:id_turma>/', views.detailAtividadeView, name='atividade'),
    path('detalhe_atividade/<int:id_turma>/<int:id_atividade>/', views.atividadeView, name='detalhe-atividade'),
    path('atividade/criar/<int:id_turma>/', views.createAtividadeView, name='criar-atividade'),
    path('atividade/sortear_para_grupo/<int:id_turma>/<int:id_atividade>/', views.sorteioGrupoView, name='sorteio-grupo'),
    path('atividade/sortear_para_aluno/<int:id_turma>/<int:id_atividade>/', views.sorteioAlunoView, name='sorteio-aluno'),
    path('atividade/editar/<int:id_turma>/<int:id_atividade>/', views.updateAtividadeView, name='editar-atividade'),
    path('atividade/deletar/<int:id_turma>/<int:id_atividade>/', views.deleteAtividadeView, name='deletar-atividade'),
]
