#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():  # Função principal que executa as tarefas administrativas do Django

    # Define o módulo de configurações do Django, caso ainda não tenha sido definido
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

    try:
        # Importa a função responsável por processar comandos administrativos do Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Exceção caso o Django não esteja instalado ou a configuração não esteja correta
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc  # Relança a exceção com uma mensagem mais detalhada

    # Executa o comando que foi passado via linha de comando
    execute_from_command_line(sys.argv)


# Verifica se o script foi chamado diretamente (e não importado como módulo)
if __name__ == '__main__':
    main()  # Chama a função principal para executar as tarefas administrativas