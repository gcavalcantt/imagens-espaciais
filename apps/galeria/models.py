from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

# Define o modelo Fotografia para armazenar informações sobre fotografias
class Fotografia(models.Model):

    # Define opções de categoria para a fotografia
    OPCOES_CATEGORIA = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]

    # Campos do modelo com suas definições
    nome = models.CharField(max_length=100, null=False, blank=False)  # Nome da fotografia
    legenda = models.CharField(max_length=150, null=False, blank=False)  # Legenda da fotografia
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')  # Categoria escolhida
    descricao = models.TextField(null=False, blank=False)  # Descrição detalhada
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)  # Caminho para salvar a imagem
    publicada = models.BooleanField(default=True)  # Define se a fotografia está publicada
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)  # Data do registro da foto
    
    # Relacionamento com o usuário que adicionou a fotografia
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,  # Se o usuário for removido, mantém a foto mas sem vínculo
        null=True,
        blank=False,
        related_name='user'
    )

    # Define a representação textual do objeto
    def __str__(self):
        return self.nome