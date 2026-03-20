# Super App

## What is the our problem?

We download apps for our needs but why we download different app for different needs. I decided fix this problem.

![Project Frontend](./frontend/src/assets/superappmainpage.png)

## Project Structure

```text
SUPERAPP
|-- backend
|   |-- src
|       |-- assets
|           |-- super_structure.png
|       |-- config
|       |-- core
|           |-- database.py
|       |-- models
|           |-- user.py
|       |-- routers
|           |-- v1
|               |-- auth.py
|           |-- api_v1.py
|       |-- schemas
|           |-- auth.py
|       |-- services
|           |-- auth.py
|       |-- main.py
|   |-- Dockerfile
|   |-- requirements.txt
|-- .env
|-- .env.example
|-- .gitignore
|-- docker-compose.yml
|-- README.md
```

## Features

- Docker & Docker Compose
- PostgreSQL

| **Backend**      | **Frontend** |
| ---------------- | ------------ |
| Python (FastAPI) | React (Vite) |

### Deployment

#### Database Information

> Create .env file and write your database information.

### Setup

Backend

```bash
git clone <repo>

cd <repo>

docker compose up --build -d

docker compose up
```

Frontend

```bash
cd frontend
npm run dev
```

#### Get's to App

> Open the localhost at 5544 port and goes to the Swagger UI.
>
> Click to [localhost](http://localhost:5544/docs)

> Open the localhost at 5173 port and goes to the main page.
>
> Click to [localhost](http://localhost:5173/)

---

---

---

### Developer

Muhammet Emin OCAK
