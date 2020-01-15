from django.urls import path
from . import views

urlpatterns = [
    path('listar_eventos/<int:id_turma>/', views.detailEventoView, name='evento'),
    path('evento/criar/<int:id_turma>/', views.createEventoView, name='criar-evento'),
    path('evento/detalhes/<int:id_turma>/<int:id_evento>/', views.showEventView, name='detalhe-evento')
]
