from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..Turma.models import Turma


@login_required
def dashboardView(request):
    turmas = Turma.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {'turmas': turmas})
