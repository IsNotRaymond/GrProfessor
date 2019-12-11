from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('dashboard/', include('GrProfessor.Turma.urls')),
]
