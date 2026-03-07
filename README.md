# Super App

## What is the our problem?

We download apps for our needs but why we download different app for different needs. I decided fix this problem.

## Project Structure

```text
SUPERAPP
|-- App
|   |-- deploy
|       |-- docker-compose.yml
|       |-- Dockerfile
|   |-- main.py
|-- .env
|-- .gitignore
|-- README.md
```

## Features

- Docker & Docker Compose
- PostgreSQL

### Deployment

#### Database Information

> Create .env file and write your database information.

#### Setup

```bash
git clone <repo>

cd <repo>

docker compose -f App/deploy/docker-compose.yml up --build -d

cd App/deploy

docker compose up
```

#### Get's to App

> Open the localhost at 5544 port.
>
> Click to [localhost](http://localhost:5544/)

---

---

---

### Developer

Muhammet Emin OCAK
