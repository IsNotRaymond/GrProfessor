from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Turma
from .forms import TurmaForm
from django.contrib.auth.decorators import login_required


@login_required
def createTurmaView(request):
    form = TurmaForm(request.POST or None)

    if form.is_valid():
        fs = form.save(commit=False)
        fs.user = request.user
        fs.save()

        messages.success(request, "Turma criada com sucesso")
        return redirect('dashboard')

    return render(request, 'Turma/criar_turma.html', {'form': form})


@login_required
def detailTurmaView(request, id_turma):
    valid = verify_turma(id_turma)
    if valid:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request, "Turma não existente.")
        return redirect('dashboard')

    context = {'turma': turma}

    return render(request, 'Turma/turma.html', context)


@login_required
def updateTurmaView(request, id_turma):
    valid = verify_turma(id_turma)
    if valid:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request, "Turma não existente.")
        return redirect('dashboard')

    form = TurmaForm(request.POST or None, instance=turma)

    if form.is_valid():
        form.save()
        messages.success(request, "Dados alterados com sucesso")
        return redirect('dashboard')

    return render(request, 'Turma/editar_turma.html', {'form': form})


@login_required
def deleteTurmaView(request, id_turma):
    valid = verify_turma(id_turma)
    if valid:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request, "Turma não existente.")
        return redirect('dashboard')

    turma.delete()
    messages.success(request, "Turma deletada com sucesso")
    return redirect('dashboard')


def verify_turma(key):
    try:
        turma = Turma.objects.get(id=key)
        return True
    except Turma.DoesNotExist:
        return False
