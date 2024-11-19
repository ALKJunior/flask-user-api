# flask-user-api

**flask-user-api** é uma aplicação simples que permite o cadastro, consulta, atualização e remoção de usuários. Desenvolvida com Flask, essa API é ideal para estudos e aplicações básicas que necessitam de um sistema de gerenciamento de usuários.

<br>

## 📜 Descrição do Projeto

Esta API fornece endpoints para operações CRUD (Create, Read, Update, Delete) de usuários. É um projeto básico voltado para aprendizado e demonstração das funcionalidades do Flask no desenvolvimento de APIs RESTful.

<br>

## 🚀 Funcionalidades

- Criar novos usuários.
- Consultar detalhes de usuários individuais ou listar todos os usuários.
- Atualizar informações de um usuário específico.
- Remover usuários do sistema.

<br>

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Flask**
- **Flask-SQLAlchemy** para gerenciamento do banco de dados.
- **SQLite** como banco de dados padrão (pode ser substituído por outros bancos).

Agora entendi exatamente o que você precisa! Vou formatar as instruções de uma maneira mais limpa e organizada, utilizando a estrutura de blocos de código no README de forma agradável para leitura. Veja abaixo:


<br>


## 📦 Como Executar o Projeto


1. Certifique-se de ter o Python instalado na sua máquina. Verifique a versão com o comando:
   python --version

2. Clone este repositório e navegue até o diretório do projeto:
   git clone https://github.com/seu-usuario/flask-user-api.git
   cd flask-user-api

3. Crie e ative um ambiente virtual:
   - Linux/Mac:
     python3 -m venv venv
     source venv/bin/activate
   - Windows:
     python -m venv venv
     venv\Scripts\activate

4. Instale as dependências do projeto:
   pip install -r requirements.txt

5. Configure o banco de dados inicializando o esquema:
   flask db upgrade

6. Inicie o servidor Flask:
   flask run

7. Acesse a API no navegador ou em um cliente HTTP (como Postman) pelo endereço:
   http://127.0.0.1:5000/


<br>
   

##  🔗 Endpoints Principais
POST /users: Criar um novo usuário.
GET /users: Listar todos os usuários.
GET /users/<id>: Consultar um usuário específico.
PUT /users/<id>: Atualizar os dados de um usuário.
DELETE /users/<id>: Remover um usuário.








##  ⚠️ Observação
Este projeto utiliza SQLite como banco de dados padrão para facilitar o desenvolvimento e testes. Para produção, recomenda-se configurar um banco de dados mais robusto, como PostgreSQL ou MySQL.
