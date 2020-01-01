from django import forms


class GrupoQuantidadeForm(forms.Form):
    quantidade = forms.IntegerField(label="Quantidade de grupos",
                                    help_text="Quantos grupos você deseja criar?",
                                    required=True)


class GrupoTamanhoForm(forms.Form):
    tamanho = forms.IntegerField(label="Quantidade de membros",
                                 help_text="Quantos membros você deseja em cada grupo?",
                                 required=True)
