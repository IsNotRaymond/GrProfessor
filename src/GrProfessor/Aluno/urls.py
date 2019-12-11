from django.urls import path
from . import views

urlpatterns = [
    path('criar_aluno/<int:id>/', views.createAlunoView, name='aluno-creation'),
]
