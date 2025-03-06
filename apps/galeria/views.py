from django.shortcuts import render, get_object_or_404, redirect

from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

from django.contrib import messages

# Função para a página inicial
def index(request):
    if not request.user.is_authenticated:  # Verifica se o usuário está logado
        messages.error(request, 'Usuário não logado')  # Exibe uma mensagem de erro
        return redirect('login')  # Redireciona para a página de login

    # Obtém todas as fotografias publicadas ordenadas por data
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

# Função para exibir uma imagem específica
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)  # Obtém a imagem ou retorna erro 404
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

# Função para buscar fotografias pelo nome
def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    # Verifica se há um termo de busca na requisição
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)  # Filtra as fotos pelo nome

    return render(request, "galeria/index.html", {"cards": fotografias})

# Função para cadastrar uma nova fotografia
def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = FotografiaForms  # Instancia o formulário
    if request.method == 'POST':  # Se a requisição for POST, processa o formulário
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():  # Verifica se os dados são válidos
            form.save()  # Salva a nova fotografia no banco de dados
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')  # Redireciona para a página inicial

    return render(request, 'galeria/nova_imagem.html', {'form': form})

# Função para editar uma fotografia existente
def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)  # Obtém a fotografia pelo ID
    form = FotografiaForms(instance=fotografia)  # Preenche o formulário com os dados existentes

    if request.method == 'POST':  # Se a requisição for POST, processa o formulário
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()  # Salva as alterações
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

# Função para deletar uma fotografia
def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)  # Obtém a fotografia pelo ID
    fotografia.delete()  # Deleta a fotografia do banco de dados
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')

# Função para filtrar fotografias por categoria
def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {"cards": fotografias})