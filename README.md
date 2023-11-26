# Projeto Padaria Delivery

Este projeto é desenvolvido com liguagem de programação Python e Framework Django, no intuito como solução melhorar toda a logistica de vendas e entregas de produtos de padaria em modalidade delivery, para que as compras sejam agilizada da melhor forma, gerando valor e qualidade para todos os usuários.

# Requisitos

1. [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)
2. [Django 4.2.7](https://www.djangoproject.com/)
2. [Poetry](https://python-poetry.org/docs/basic-usage/)

# Como desenvolver?

1. Clone o repositório.
2. Instale todas as dependências.
3. Ative o ambiente virtual.
4. Efetuar as migrações
5. Rode a aplicação.

# Comandos para rodar o projeto:

Clonar projeto.
```
git clone https://github.com/geovanecarvalho/padaria-delivery
```
Instalar dependências.
```
poetry install
```
Ativar ambiente virtual.
```
poetry shell
```
Fazer migrações das tabelas.
```
python manage.py makemigrations
```
Fazer migração do banco de dados.
```
python manage.py migrate
```
Rodar o projeto.
```
python manage.py runserver
```
Acessar a página no navegado
[http://localhost:8000](http://localhost:8000)

# Caso não queira utilizar o Poetry como gerencidador de pacotes pode ser usado o PIP.

## Comandos para rodar o projeto

Criar um ambiente virtual.
```
python3 -m venv .padaria-delivery
```
Ativar ambiente virtual linux.
```
./.padaria-delivery/bin/activate
```
Ativar ambiente virtual no windows
```
./.padaria-delivery/Scripts/Activate
```
Instalar todos requerimentos.
```
pip install -r requirements.txt
```
Fazer migrações das tabelas.
```
python manage.py makemigrations
```
Fazer migração do banco de dados.
```
python manage.py migrate
```
Rodar o projeto.
```
python manage.py runserver
```

Acessar a página no navegado
[http://localhost:8000](http://localhost:8000)
 
