from django.urls import path

# Importa as views da aplicação 'galeria'
from apps.galeria.views import \
     index, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem, filtro

# Define as rotas da aplicação
urlpatterns = [
    path('', index, name='index'),  # Rota para a página inicial
    path('imagem/<int:foto_id>', imagem, name='imagem'),  # Exibe uma imagem específica
    path('buscar', buscar, name='buscar'),  # Rota para a funcionalidade de busca
    path('nova-imagem', nova_imagem, name='nova_imagem'),  # Página para adicionar uma nova imagem
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),  # Edita uma imagem específica
    path('deletar-imagem/<int:foto_id>', deletar_imagem, name='deletar_imagem'),  # Deleta uma imagem específica
    path('filtro/<str:categoria>', filtro, name='filtro'),  # Filtra imagens por categoria
]