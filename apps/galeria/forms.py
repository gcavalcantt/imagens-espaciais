from django import forms

from apps.galeria.models import Fotografia

# Define um formulário baseado no modelo Fotografia
class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia  # Define o modelo base do formulário
        exclude = ['publicada',]  # Exclui o campo 'publicada' do formulário
        labels = {  # Define rótulos personalizados para os campos do formulário
            'descricao':'Descrição',
            'data_fotografia': 'Data de registro',
            'usuario': 'Usuário',
        }
    
        widgets = {  # Define widgets para estilizar os campos do formulário
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%Y',  # Define o formato da data
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }