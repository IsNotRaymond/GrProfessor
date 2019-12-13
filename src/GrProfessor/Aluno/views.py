import csv, io
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..Turma.models import Turma
from ..Turma.views import verify_turma
from .forms import AlunoForm
from .models import Aluno


@login_required
def createAlunoView(request, id_turma):
    valid_turma = verify_turma(id_turma)
    if valid_turma:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')

    if request.POST:
        form = AlunoForm(request.POST)

        if form.is_valid():
            fs = form.save(commit=False)
            fs.turma_pertencente = turma
            fs.save()

            messages.success(request, "Aluno criado com sucesso")
            return redirect('aluno', id_turma)

    else:
        form = AlunoForm()

    return render(request, 'Aluno/criar_aluno.html', {'form': form})


def detailAlunoView(request, id_turma):
    valid = verify_turma(id_turma)
    if valid:
        turma = Turma.objects.get(id=id_turma)
    else:
        messages.warning(request, "Turma não existente.")
        return redirect('dashboard')

    context = {'alunos': Aluno.objects.filter(turma_pertencente=id_turma),
               'turma': Turma.objects.get(id=id_turma)}

    return render(request, 'Aluno/aluno.html', context)


@login_required
def updateAlunoView(request, id_turma, id_aluno):
    valid_turma = verify_turma(id_turma)

    if not valid_turma:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')
    valid_aluno = verify_aluno(id_aluno)

    if not valid_aluno:
        messages.warning(request,
                         "Aluno não existente.")
        return redirect('aluno', id_turma)

    aluno = Aluno.objects.get(id=id_aluno)

    form = AlunoForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        messages.success(request, "Dados alterados com sucesso")
        return redirect('aluno', id_turma)

    return render(request, 'Aluno/editar_aluno.html', {'form': form})


@login_required
def deleteAlunoView(request, id_aluno, id_turma):
    valid_turma = verify_turma(id_turma)

    if not valid_turma:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')
    valid_aluno = verify_aluno(id_aluno)

    if not valid_aluno:
        messages.warning(request,
                         "Aluno não existente.")
        return redirect('aluno', id_turma)

    aluno = Aluno.objects.get(id=id_aluno)

    aluno.delete()
    messages.success(request, "Aluno deletado com sucesso")
    return redirect('aluno', id_turma)


def uploadAlunosView(request, id_turma):
    valid_turma = verify_turma(id_turma)

    if not valid_turma:
        messages.warning(request,
                         "Turma não existente.")
        return redirect('dashboard')

    if request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            messages.warning(request, 'Isso não é um arquivo csv')
            return redirect('upload-csv', id_turma)

        dataset = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(dataset)
        next(io_string)

        for coluna in csv.reader(io_string, delimiter=',', quotechar='|'):
            _, created = Aluno.objects.update_or_create(nome_aluno=coluna[0],
                                                        turma_pertencente=Turma.objects.get(id=id_turma))

        messages.success(request, 'Alunos importados com sucesso')
        return redirect('aluno', id_turma)

    return render(request, 'Aluno/upload_csv.html')


def verify_aluno(key):
    try:
        turma = Aluno.objects.get(id=key)
        return True
    except Aluno.DoesNotExist:
        return False
