# Site PyLadies Sergipe

Esse é o repositório para o projeto do nosso site.

## Instalação

Use o gerenciador de pacotes  [pip](https://pip.pypa.io/en/stable/) para instalar Virtualenvwrapper ([detalhes de configuração](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)). Após configuração do Virtualenvwrapper no seu computador, crie um ambiente virtual para o projeto

```bash
mkvirtualenv pyladies-site
```
Com o ambiente virtual criado, execute em seu terminal (estando na raiz do diretório do projeto):

```bash
pip install -r requirements.txt
```

Após seu computar finalizar as instalações dos pacotes de dependência, crie um usuário root para você poder acessar o painel admin e assim popular a base de dados.

```bash
python manage.py createsuperuser
```
*Obs.: Ainda estamos utilizando o sqlite como banco de dados e por isso não precisa, nesse momento, realizar nenhuma configuração de banco de dados.*

## Execução

```python
python manage.py runserver
```
Agora basta acessar no seu browser **localhost:8000** e navegar.

## Contribuição e desenvolvimento
Em breve maiores informações.
