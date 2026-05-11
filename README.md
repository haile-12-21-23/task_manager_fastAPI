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

## 📂 Project Structure

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
```

### ⚙️ Technologies Used

- **Python 3.12+**
- **FastAPI**
- **SQLAlchemy 2.x**
- **Async SQLite**
- **Pydantic**
- **Docker**
- **Uvicorn**

### ✨ Features

#### Task CRUD Operations

- **Create** task
- **Read** all tasks
- **Read** single task
- **Update** task
- **Delete** task

#### Advanced Query Features

- **Search** by title
- **Filter** by status
- **Sorting**
- **Pagination**

#### Architecture

- **Async** database operations
- **Modular** router structure
- **Separated** CRUD layer
- **Clean** scalable backend design

### 📦 Installation

1. **Clone Repository**

   ```bash
   git clone https://github.com/haile-12-21-23/task_manager_fastAPI.git

2. **Navigate Into Project**

      ```cd task_manager```

3. **Create Virtual Environment**

- **macOS/Linux**

     ```bash
     python3 -m venv .venv

- **Windows**

    ```Bash
    python -m venv .venv 
    ```

---

### ▶️ Activate Virtual Environment

- **macOS/Linux**

  ```bash
  source .venv/bin/activate
  
- **Windows**

    ```Bash
    .venv\Scripts\activate

---

### 📥 Install Dependencies

```bash
pip install -r requirements.txt
 ```

### 🔐 Environment Variables

*Create a .env file in the root directory.*

Example:

```DATABASE_URL=sqlite+aiosqlite:///./tasks.db```

### 🚀 Run the Server ###

```uvicorn app.main:app --reload```

### Server will run at ###

 <http://127.0.0.1:8000>

### 📚 Swagger API Documentation ###

Open: <http://127.0.0.1:8000/docs>

#### Swagger UI allows you to ####

- Test endpoints

- Send requests

- View responses

- Explore schemas

### 🧪 API Endpoints ###

#### Create Task

#### POST /tasks/ ####

 Request Body:

```JSON
{
  "title": "Learn FastAPI",
  "status": "pending"
}
```

### Example Response ###

```JSON
{
  "id": 1,
  "title": "Learn FastAPI",
  "status": "pending",
  "owner_id": 1
} 
```

### Get All Tasks ###

**GET /tasks/**

| Feature | Endpoint |
| :--- | :--- |
| **All Tasks** | `GET /tasks/` |
| **Search** | `GET /tasks/?search=fastapi` |
| **Filter** | `GET /tasks/?status=pending` |
| **Sorting** | `GET /tasks/?sort_by=id&order=desc` |
| **Pagination** | `GET /tasks/?limit=5&offset=0` |           GET /tasks/?limit=5&offset=0

### Individual Task Operations ###

**Get Single Task**: ```GET /tasks/1```

**Update Task:** ```PUT /tasks/1```

**Body**:```{"title": "Learn Async FastAPI", "status": "completed"}```

**Delete Task:** ``DELETE /tasks/1``

**Response**: ```{"message": "Task deleted successfully"}```

### 🐳 Docker Setup ###

1. #### Build Docker Image ###

```Bash
docker build -t task-manager-api . 
```

1. ### Run Docker Container ###

```Bash
   docker run -p 8000:8000 task-manager-api
   ```

**API will be available at**: <http://127.0.0.1:8000>

### 🧱 Database ###

**Current default**: SQLite (Async)

**Connection:** DATABASE_URL=sqlite+aiosqlite:///./tasks.db

Modular design allows easy switching to PostgreSQL or MySQL without changing the project structure.

### 📌 Future Improvements ###

- JWT Authentication & User Login

- PostgreSQL Deployment

- Alembic Migrations

- CI/CD Pipeline

- Pytest Unit Testing

- Role-Based Access Control (RBAC)

- Task Due Dates & File Uploads

## 👨‍💻 Author

Built as part of a backend engineering learning journey using FastAPI and modern Python tools.

## 📄 License
This project is open-source and available for learning and educational purposes.
