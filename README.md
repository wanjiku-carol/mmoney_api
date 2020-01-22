# mmoney_api

## Description
Mmoney API is a Python backend creation of a mobile money platform.
It will involve asynchronous processing of financial transactions:

- from bank accounts to mobile money accounts to mobile money accounts.

- Mobile money accounts to mobile money accounts.

- Mobile money accounts to bank accounts.

Users will get transaction-related messages each time a transaction occurs.
Since FastAPI eliminates the need for celery tasks and RabbitMQ, we will not be processing
messages through these.

## Docker Commands

Build the image and spin up the container

> docker-compose up -d --build

Run the tests on docker

> docker-compose exec web pytest


## Fast API Notes
The container runs on localhost

> http://localhost:8002

- It has a lightweight microframework feel with support for Flask-like route decorators.

- It takes advantage of Python type hints for parameter declaration which enables data validation (via Pydantic) and OpenAPI/Swagger documentation. View the interactive API documentation on:

> http://localhost:8002/docs

- Built on top of Starlette, it supports the development of asynchronous APIs.

- Its fast. Since async is much more efficient than the traditional synchronous threading model, it can compete with Node and Go with regards to performance.

### Links for More Info on FastAPI

FastAPI features:
- https://fastapi.tiangolo.com/features/

Alternatives, Inspiration, and Comparisons:
 - https://fastapi.tiangolo.com/alternatives/

Starlette
- https://www.starlette.io/

Pydantic
- https://pydantic-docs.helpmanual.io/

## Routes

- /users: GET, PUT, DELETE

- /recipients: GET, POST

- /transactions: GET

- countries: GET

- /send: POST

- /login: POST

- /logout: POST

- /signup: POST

- /verify_email: POST

- /verify_sms: POST

- forgot_password: POST


## Postgres SetUp
To view psql, run:

> docker-compose exec db psql --username=mmoney_api --dbname=mmoney_api_dev

To view the list of databases:

> mmoney_api_dev=# \l

To connect to the database:
> mmoney_api_dev=# \c

To view the tables created:

> mmoney_api_dev=# \dt
