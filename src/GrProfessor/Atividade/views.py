from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from random import shuffle, choice
from ..Aluno.models import Aluno
from ..Grupo.models import Grupo
from ..Turma.models import Turma
from ..Turma.views import verify_turma
from .forms import AtividadeForm
from .models import Atividade


@login_required
def createAtividadeView(request, id_turma):
    valid_turma = verify_turma(id_turma)
    if valid_turma:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')

    if request.POST:
        form = AtividadeForm(request.POST)

        if form.is_valid():

            fs = form.save(commit=False)

            fs.turma_pertencente = turma
            fs.save()

            messages.success(request, "Atividade criada com sucesso")
            return redirect('atividade', id_turma)

    else:
        form = AtividadeForm()

    return render(request, 'Atividade/criar_atividade.html', {'form': form})


@login_required
def detailAtividadeView(request, id_turma):
    valid = verify_turma(id_turma)
    if valid:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request, "Turma não existente.")
        return redirect('dashboard')

    context = {'atividades': Atividade.objects.filter(turma_pertencente=id_turma),
               'turma': Turma.objects.get(id=id_turma)}

    return render(request, 'Atividade/atividade.html', context)

def sorteio(tipo, key):
    alunos = Aluno.objects.filter(turma_pertencente=key)
    queryset = []
    ids = []
    if tipo == 'grupo':
        for aluno in alunos:
            grupo = aluno.grupo_pertencente.last()
            if grupo not in queryset:
                queryset.append(grupo)

    elif tipo == 'aluno':
        queryset = Aluno.objects.filter(turma_pertencente=key)

    for query in queryset:
        ids.append(query.id)

    shuffle(ids)
    return choice(ids)


@login_required
def sorteioGrupoView(request, id_turma, id_atividade):
    valid_turma = verify_turma(id_turma)

    if not valid_turma:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')
    valid_atividade = verify_atividade(id_atividade)

    if not valid_atividade:
        messages.warning(request,
                         "Atividade não existente.")
        return redirect('turma', id_turma)

    atv = Atividade.objects.filter(id=id_atividade)
    gp = sorteio('grupo', id_turma)

    atv(aluno_atribuido=None, grupo_atribuid=Grupo.objects.get(id=gp)).save()

    messages.success(request, 'Sorteio realizado com sucesso')
    return redirect('atividade', id_turma)


@login_required
def sorteioAlunoView(request, id_turma, id_atividade):
    valid_turma = verify_turma(id_turma)

    if not valid_turma:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')
    valid_atividade = verify_atividade(id_atividade)

    if not valid_atividade:
        messages.warning(request,
                         "Atividade não existente.")
        return redirect('turma', id_turma)

    atv = Atividade.objects.get(id=id_atividade)
    al = sorteio('aluno', id_turma)

    atv.aluno_atribuido=Aluno.objects.get(id=al), grupo_atribuido = None).save()

    messages.success(request, 'Sorteio realizado com sucesso')
    return redirect('atividade', id_turma)


@login_required
def atividadeView(request, id_turma, id_atividade):
    valid_turma = verify_turma(id_turma)

    if not valid_turma:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')
    valid_atividade = verify_atividade(id_atividade)

    if not valid_atividade:
        messages.warning(request,
                         "Atividade não existente.")
        return redirect('atividade', id_turma)

    context = {'atividade': Atividade.objects.get(id=id_atividade),
               'turma': Turma.objects.get(id=id_turma)}

    return render(request, 'Atividade/opcoes_atividade.html', context)


@login_required
def updateAtividadeView(request, id_turma, id_atividade):
    valid_turma = verify_turma(id_turma)

    if not valid_turma:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')
    valid_atividade = verify_atividade(id_atividade)

    if not valid_atividade:
        messages.warning(request,
                         "Atividade não existente.")
        return redirect('atividade', id_turma)

    atividade = Atividade.objects.get(id=id_atividade)

    form = AtividadeForm(request.POST or None, instance=atividade)

    if form.is_valid():
        form.save()
        messages.success(request, "Dados alterados com sucesso")
        return redirect('atividade', id_turma)

    return render(request, 'Atividade/editar_atividade.html', {'form': form})


@login_required
def deleteAtividadeView(request, id_turma, id_atividade):
    valid_turma = verify_turma(id_turma)

    if not valid_turma:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')
    valid_atividade = verify_atividade(id_atividade)

    if not valid_atividade:
        messages.warning(request,
                         "Atividade não existente.")
        return redirect('atividade', id_turma)

    atividade = Atividade.objects.get(id=id_atividade)

    atividade.delete()
    messages.success(request, "Atividade deletada com sucesso")
    return redirect('atividade', id_turma)


def verify_atividade(key):
    try:
        turma = Atividade.objects.get(id=key)
        return True
    except Atividade.DoesNotExist:
        return False
