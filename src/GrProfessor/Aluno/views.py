from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..Turma.models import Turma
from .forms import AlunoForm


@login_required
def createAlunoView(request, id):
    if request.POST:
        form = AlunoForm(request.POST)

        if form.is_valid():
            fs = form.save(commit=False)
            fs.turma_pertencente = Turma.objects.get(id=id)
            fs.save()

            messages.success(request, "Aluno criado com sucesso")
            return redirect('turma', id=id)

    else:
        form = AlunoForm()

    return render(request, 'Aluno/criar_aluno.html', {'form': form})

