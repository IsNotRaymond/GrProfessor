from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Turma
from .forms import TurmaForm
from ..Aluno.models import Aluno
from django.contrib.auth.decorators import login_required


@login_required
def turmaFormView(request):
    form = TurmaForm(request.POST or None)

    if form.is_valid():
        fs = form.save(commit=False)
        fs.user = request.user
        fs.save()

        messages.success(request, "Turma criada com sucesso")
        return redirect('dashboard')

    return render(request, 'Turma/criar_turma.html', {'form': form})


@login_required
def detailTurmaView(request, id):
    context = {'turma': Turma.objects.get(id=id),
               'alunos': Aluno.objects.filter(turma_pertencente=id)}

    return render(request, 'Turma/turma.html', context)


@login_required
def updateTurmaView(request, id):
    turma = Turma.objects.get(id=id)

    form = TurmaForm(request.POST or None, instance=turma)

    if form.is_valid():
        form.save()
        messages.success(request, "Os dados foram alterados com sucesso")
        return redirect('dashboard')

    return render(request, 'Turma/editar_turma.html', {'form': form})


@login_required
def deleteTurmaView(request, id):
    turma = Turma.objects.get(id=id)
    turma.delete()
    messages.success(request, "A turma foi deletada com sucesso")
    return redirect('dashboard')
