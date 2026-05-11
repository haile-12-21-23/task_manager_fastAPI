# Task Manager API 🚀

A production-style Task & Resource Management API built with FastAPI, Async SQLAlchemy, and Docker.

This project demonstrates modern backend engineering concepts including:

- FastAPI async endpoints
- SQLAlchemy async ORM
- CRUD operations
- Filtering, sorting, and pagination
- Clean project architecture
- Docker containerization
- JWT-ready security structure

---

# 📂 Project Structure

```plaintext
task_manager/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   ├── routers/
│   │   └── tasks.py
│   └── core/
│       └── security.py
├── tests/
├── requirements.txt
├── Dockerfile
├── .env
└── README.md

### ⚙️ Technologies Used
* **Python 3.12+**
* **FastAPI**
* **SQLAlchemy 2.x**
* **Async SQLite**
* **Pydantic**
* **Docker**
* **Uvicorn**

### ✨ Features
#### Task CRUD Operations
* **Create** task
* **Read** all tasks
* **Read** single task
* **Update** task
* **Delete** task

#### Advanced Query Features
* **Search** by title
* **Filter** by status
* **Sorting**
* **Pagination**

#### Architecture
* **Async** database operations
* **Modular** router structure
* **Separated** CRUD layer
* **Clean** scalable backend design.