from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Turma
from .forms import TurmaForm


def dashboardView(request):
    turmas = Turma.objects.all()
    print(request)
    return render(request, 'dashboard.html', {'turmas': turmas})


def TurmaView(request):
    if request.POST:
        form = TurmaForm(request.POST)

        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()

            messages.success(request, "Turma criada com sucesso")
            return redirect('dashboard')

    else:
        form = TurmaForm()

    return render(request, 'Turma/criar_turma.html', {'form': form})


def detailTurmaView(request):
    if request.GET:
        id_turma = int(request.GET['id'])
        context = {'turma': Turma.objects.get(id=id_turma)}
        return render(request, 'Turma/turma.html', context)
    else:
        return render(request, 'Turma/turma.html', {})


