# Gerenciador de Imagens Espaciais

Este projeto é uma aplicação web desenvolvida utilizando Django e Python orientado a objetos para o gerenciamento de imagens espaciais. A aplicação permite aos usuários fazer upload, editar, excluir e buscar imagens relacionadas a temas espaciais, como nebulosas, estrelas, galáxias e planetas. O armazenamento das imagens é integrado com a AWS, garantindo escalabilidade e segurança.

### Funcionalidades

* Cadastro e Login de Usuários: Sistema de autenticação de usuários, com possibilidade de criação de contas e login.
* Gerenciamento de Imagens: Os usuários podem adicionar novas imagens, editar informações e excluir imagens.
* Busca e Filtros: Sistema de busca por nome e filtros por categorias de imagens (ex: Nebulosa, Estrela, Galáxia, Planeta).
* Exibição de Imagens: Interface de visualização de imagens espaciais com seus detalhes.
* Integração com AWS: As imagens são armazenadas na AWS S3, proporcionando armazenamento escalável.

### Tecnologias Utilizadas

* Backend: Django, Python
* Frontend: HTML, CSS, JavaScript
* Banco de Dados: SQLite (padrão do Django, mas configurável)
* Armazenamento de Imagens: AWS S3
* Autenticação de Usuários: Django Authentication
* CSS Framework: Bootstrap (para responsividade e estilo)
* Deploy: Pode ser configurado para deploy em plataformas como Heroku ou AWS Elastic Beanstalk.