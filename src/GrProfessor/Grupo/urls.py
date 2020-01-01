from django.urls import path
from . import views

urlpatterns = [
    path('listar_grupos/<int:id_turma>/', views.detailGrupoView, name='grupo'),
    path('grupo/criar/<int:id_turma>/', views.createGrupoView, name='criar-grupo'),
    path('grupo/criar/quantidade/<int:id_turma>/', views.createGrupoQuantidadeView, name='criar-grupo-quantidade'),
    path('grupo/criar/tamanho/<int:id_turma>/', views.createGrupoTamanhoView, name='criar-grupo-tamanho'),
    path('grupo/deletar/<int:id_turma>/', views.deleteGrupoView, name='deletar-grupo'),
]
