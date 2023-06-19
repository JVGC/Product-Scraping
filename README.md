# Open Food Facts Scraping

A ideia desse projeto é fazer o Scraping de produtos do site [Open Food Facts](https://world.openfoodfacts.org).

This is a challenge by **Coodesh**.

## Stack

O projeto foi desenvolvido utilizando a linguagem **Python**, mais especificamente o framework **Django**.

Para o desenvolvimento da API REST, foi utilizado o pacote **Django Rest Framework** que transforma o Django de um MVC para uma API Rest.

Para fazer o Scraping dos dados, foi utilizado a biblioteca **Scrapy** que facilita muito o scraping dos dados no Python. Para mais detalhes, acesse a pasta do [scraper](./src/scraper/).

Além disso, foi utilizado a biblioteca **django-crontab** para abstrair a criação e a execução de comandos Cron no Django.

E para finalizar o projeto, também foi utilizado biblioteca **drf-spectacular** que se integra ao Django Rest Framework e gera uma documentação utilizando Swagger automaticamente.

Todo o projeto foi desenvolvido usando Docker, como pode ver nos arquivos abaixo:

- [docker-compose.yml](./docker-compose.yml)
- [Dockefile](./Dockerfile)
- [docker-entrypoint.sh](./src/docker-entrypoint.sh)

## Banco de Dados

Pontos muito importantes sobre a decisão de qual banco utilizar.

Utilizar um banco NoSQL, como o MongoDB, seria a melhor solução para guardar esses dados.

Infelizmente, o Django (que é o principal ponto da vaga) não se integra facilmente ao MongoDB, e quando se integra, ele faz que o django perca muito da sua capacidade. A própria [documentação do MongoDB](https://www.mongodb.com/compatibility/mongodb-and-django), diz que para a integração com o mongo é necessário a implementação do ORM do Django utilizando outra biblioteca como o **pymongo**.

Por esses motivos, e como a descrição do problema deixava claro que eu poderia escolher um banco SQL caso achasse melhor, achei melhor seguir com um banco de dados SQL, no caso o PostgreSQL.

## Setup

1. Instale o [Docker.](https://docs.docker.com/engine/install/)
2. Criar um arquivo .env na raiz do projeto e preencha baseado no arquivo de exemplo: [env.example](./.env.example).

## Run

### Backend

A API roda por padrão na porta **8000**.
Para iniciar, é só rodar:

```sh
    docker compose up
```

## Testing

Django cria um banco de dados separado somente para testes e é totalmente responsável por criar e destruir ele após os testes.

Você pode rodar os testes usando:

```sh
    docker exec product-scraping-api-1 python3 manage.py test
```

## Scraping

O scraper roda automaticamente baseados nas configuração do cron job setados no arquivo .env. Mesmo assim, você pode rodar ele manualmente usando:

```sh
    docker exec product-scraping-api-1 python3 manage.py crawl
```

## API Documentation

A documentação da API foi feito utilizando o Swagger, e foi gerada utilizando a biblioteca **drf-spectacular**.

Você pode acessar o arquivo yml na pasta [/docs/api.yml](./docs/api.yml).

Para gerar o arquivo novamente, é só rodar:

```sh
    docker exec product-scraping-api-1 python3 manage.py spectacular --file ../docs/api.yml
```
