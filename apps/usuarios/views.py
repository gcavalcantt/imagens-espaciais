from django.shortcuts import render, redirect  # Importa funções para renderizar templates e redirecionar páginas

from apps.usuarios.forms import LoginForms, CadastroForms  # Importa os formulários de login e cadastro

from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django
from django.contrib import auth  # Importa funcionalidades de autenticação do Django
from django.contrib import messages  # Importa mensagens para feedback ao usuário

# Função para realizar o login do usuário
def login(request):
    form = LoginForms()  # Instancia o formulário de login

    if request.method == 'POST':  # Verifica se o formulário foi enviado
        form = LoginForms(request.POST)  # Preenche o formulário com os dados enviados

        if form.is_valid():  # Verifica se os dados do formulário são válidos
            nome = form['nome_login'].value()  # Obtém o nome do usuário
            senha = form['senha'].value()  # Obtém a senha digitada

        # Autentica o usuário com as credenciais fornecidas
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )

        if usuario is not None:  # Se a autenticação for bem-sucedida
            auth.login(request, usuario)  # Faz login do usuário
            messages.success(request, f'{nome} logado com sucesso!')  # Exibe mensagem de sucesso
            return redirect('index')  # Redireciona para a página inicial
        else:
            messages.error(request, 'Erro ao efetuar login')  # Exibe mensagem de erro
            return redirect('login')  # Redireciona para a página de login

    return render(request, 'usuarios/login.html', {'form': form})  # Renderiza a página de login com o formulário

# Função para realizar o cadastro de um novo usuário
def cadastro(request):
    form = CadastroForms()  # Instancia o formulário de cadastro

    if request.method == 'POST':  # Verifica se o formulário foi enviado
        form = CadastroForms(request.POST)  # Preenche o formulário com os dados enviados

        if form.is_valid():  # Verifica se os dados do formulário são válidos
            nome = form['nome_cadastro'].value()  # Obtém o nome do usuário
            email = form['email'].value()  # Obtém o email
            senha = form['senha_1'].value()  # Obtém a senha digitada

            # Verifica se o usuário já existe no banco de dados
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')  # Exibe mensagem de erro
                return redirect('cadastro')  # Redireciona para a página de cadastro

            # Cria um novo usuário no banco de dados
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()  # Salva o novo usuário no banco de dados
            messages.success(request, 'Cadastro efetuado com sucesso!')  # Exibe mensagem de sucesso
            return redirect('login')  # Redireciona para a página de login

    return render(request, 'usuarios/cadastro.html', {'form': form})  # Renderiza a página de cadastro com o formulário

# Função para realizar o logout do usuário
def logout(request):
    auth.logout(request)  # Realiza o logout do usuário
    messages.success(request, 'Logout efetuado com sucesso!')  # Exibe mensagem de sucesso
    return redirect('login')  # Redireciona para a página de login