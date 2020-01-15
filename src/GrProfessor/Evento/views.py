from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..Turma.models import Turma
from ..Atividade.models import Atividade
from ..Turma.views import verify_turma
from ..Grupo.models import Grupo
from ..Aluno.models import Aluno
from .forms import EventoForm
from .models import Evento


@login_required
def createEventoView(request, id_turma):
    valid_turma = verify_turma(id_turma)
    if valid_turma:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')

    if request.POST:
        form = EventoForm(request.POST)

        if form.is_valid():
            f = form.save(commit=False)
            tamanho = f.quantidade_atividades

            pode_sortear = sortear_evento(tamanho, id_turma)

            if not pode_sortear:
                messages.warning(request, "Quantidade de atividades insuficiente")
                return redirect('criar-atividade', id_turma)

            f.turma_pertencente = turma
            f.save()
            for atividade in pode_sortear:
                atividade.evento_atribuido = Evento.objects.get(id=f.id)
                atividade.save()

            messages.success(request, "Evento criado com sucesso")
            return redirect('evento', id_turma)

    else:
        form = EventoForm()

    return render(request, 'Evento/criar_evento.html', {'form': form})


def detailEventoView(request, id_turma):
    valid = verify_turma(id_turma)
    if valid:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request, "Turma não existente.")
        return redirect('dashboard')

    context = {'eventos': Evento.objects.filter(turma_pertencente=turma),
               'turma': Turma.objects.get(id=id_turma)}

    return render(request, 'Evento/evento.html', context)


def showEventView(request, id_turma, id_evento):
    valid = verify_turma(id_turma)
    if valid:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request, "Turma não existente.")
        return redirect('dashboard')

    atividades = Atividade.objects.filter(evento_atribuido=id_evento)
    print(atividades)

    context = {'atividades': Atividade.objects.filter(evento_atribuido=id_evento),
               'evento': Evento.objects.get(id=id_evento),
               'turma': Turma.objects.get(id=id_turma)}

    return render(request, 'Evento/show_event.html', context)


def sortear_evento(quantidade, id_turma):
    lista_atividades = sortear_atividades(quantidade, id_turma)

    if not lista_atividades:
        return False

    return lista_atividades


def sortear_atividades(quantidade, id_turma):
    atividades = Atividade.objects.filter(turma_pertencente=id_turma)
    queryset = []

    for atividade in atividades:
        if atividade.evento_atribuido is not None:
            continue
        queryset.append(atividade)

    if len(queryset) != quantidade:
        return False
    return queryset
