# Projeto Carros

O projeto **Carros** é uma aplicação web construída com Django que permite aos usuários criar uma conta e, após o login, listar, criar, editar e excluir anúncios de carros.

## Funcionalidades

- **Criar um usuário**: Permite a criação de novas contas de usuário.
- **Listar carros**: Usuários logados podem visualizar uma lista de carros disponíveis.
- **Criar um anúncio de carro**: Usuários logados podem criar novos anúncios de carros.
- **Editar um anúncio de carro**: Usuários logados podem editar seus anúncios existentes.
- **Excluir um anúncio de carro**: Usuários logados podem excluir seus anúncios existentes.

## Requisitos

Certifique-se de ter o [Python](https://www.python.org/downloads/) e o [pip](https://pip.pypa.io/en/stable/) instalados.

## Instalação

1. Clone o repositório:

    ```bash
    git clone [https://github.com/seuusuario/carros.git](https://github.com/jccarlosjr/carros.git)
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd carros
    ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5. Execute as migrações:

    ```bash
    python manage.py migrate
    ```

6. Crie um superusuário para acessar o painel de administração (opcional):

    ```bash
    python manage.py createsuperuser
    ```

7. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

    O servidor estará disponível em `http://127.0.0.1:8000/`.

## Uso

1. Acesse a página principal do aplicativo e registre uma nova conta ou faça login com uma conta existente.
2. Após o login, você pode listar, criar, editar e excluir anúncios de carros.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).
