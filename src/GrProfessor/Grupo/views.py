from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GrupoQuantidadeForm, GrupoTamanhoForm
from random import shuffle
from .models import Grupo
from ..Aluno.models import Aluno
from ..Turma.models import Turma
from ..Turma.views import verify_turma


@login_required
def createGrupoView(request, id_turma):
    valid = verify_turma(id_turma)
    if valid:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request, "Turma não existente.")
        return redirect('dashboard')

    context = {'turma': turma}

    return render(request, 'Grupo/criar_grupo.html', context)


@login_required
def createGrupoQuantidadeView(request, id_turma):
    valid_turma = verify_turma(id_turma)

    if valid_turma:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')

    if request.POST:
        form = GrupoQuantidadeForm(request.POST)
        alunos = Aluno.objects.filter(turma_pertencente=id_turma)

        if form.is_valid():
            quantidade_grupos = form.cleaned_data['quantidade']
            quantidade_alunos = alunos.count()

            if quantidade_alunos // 2 < quantidade_grupos:
                messages.warning(request, 'Alunos insuficientes para a quantidade digitada')
                return redirect('criar-grupo', id_turma)

            else:
                over = False
                lista = []
                for query in alunos:
                    lista.append(query)

                parte_inteira = quantidade_alunos // quantidade_grupos
                resto = quantidade_alunos % quantidade_grupos
                if resto > 0:
                    over = True

                for i in range(1, quantidade_grupos + 1):
                    shuffle(lista)
                    grupo = Grupo(nome_grupo='Grupo %d' % i)
                    grupo.save()

                    for j in range(parte_inteira):
                        aluno = lista.pop(0)
                        aluno.grupo_pertencente.add(grupo)

                    if resto > 0:
                        aluno = lista.pop(0)
                        aluno.grupo_pertencente.add(grupo)
                        resto -= 1

                if over:
                    messages.success(request, 'Grupos gerados com sucesso. Alguns alunos foram realocados em '
                                              'outros grupos')
                else:
                    messages.success(request, 'Grupos gerados com sucesso')
                return redirect('grupo', id_turma)

    else:
        form = GrupoQuantidadeForm()

    return render(request, 'Grupo/criar_grupo_quantidade.html', {'form': form})


@login_required
def detailGrupoView(request, id_turma):
    valid = verify_turma(id_turma)
    if valid:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request, "Turma não existente.")
        return redirect('dashboard')
    alunos = Aluno.objects.filter(turma_pertencente=id_turma)

    temp = []
    for aluno in alunos:
        grupo = aluno.grupo_pertencente.last()
        if grupo not in temp:
            temp.append(grupo)

    context = {'grupos': temp,
               'turma': Turma.objects.get(id=id_turma)}

    return render(request, 'Grupo/grupo.html', context)


def createGrupoTamanhoView(request, id_turma):
    valid_turma = verify_turma(id_turma)

    if valid_turma:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')

    if request.POST:
        form = GrupoTamanhoForm(request.POST)
        alunos = Aluno.objects.filter(turma_pertencente=id_turma)

        if form.is_valid():
            quantidade_membros = form.cleaned_data['tamanho']
            quantidade_alunos = alunos.count()

            if quantidade_membros < 2 or quantidade_alunos // quantidade_membros < 2:
                messages.warning(request, 'Quantidade inválida. Lembre-se o número de membros deve ser o mais uniforme '
                                          'possível, e também não é possível criar grupos com menos de um membro')
                return redirect('criar-grupo', id_turma)

            else:
                over = False
                lista = []
                for query in alunos:
                    lista.append(query)

                parte_inteira = quantidade_alunos // quantidade_membros
                resto = quantidade_alunos % quantidade_membros

                if resto > 0:
                    over = True

                for i in range(1, parte_inteira + 1):
                    shuffle(lista)
                    grupo = Grupo(nome_grupo='Grupo %d' % i)
                    grupo.save()

                    for j in range(quantidade_membros):
                        aluno = lista.pop(0)
                        aluno.grupo_pertencente.add(grupo)

                    if resto > 0:
                        aluno = lista.pop(0)
                        aluno.grupo_pertencente.add(grupo)
                        resto -= 1

                if over:
                    messages.success(request, 'Grupos gerados com sucesso. Alguns alunos foram realocados em '
                                              'outros grupos')
                else:
                    messages.success(request, 'Grupos gerados com sucesso')
                return redirect('grupo', id_turma)

    else:
        form = GrupoTamanhoForm()

    return render(request, 'Grupo/criar_grupo_tamanho.html', {'form': form})


@login_required
def deleteGrupoView(request, id_turma):
    valid_turma = verify_turma(id_turma)

    if not valid_turma:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')

    alunos = Aluno.objects.filter(turma_pertencente=id_turma)

    for aluno in alunos:
        aluno.grupo_pertencente.clear()
    messages.success(request, 'Grupos deletados com sucesso')
    return redirect('grupo', id_turma)

