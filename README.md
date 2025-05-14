
# 📝 Task Manager App

This project is a Task Manager web application built using Django, Docker, PostgreSQL, and Nginx. It allows users to create, update, and delete tasks. It uses Docker for containerization, and Nginx as a reverse proxy for the Django application.

This project includes:
- Custom user authentication
- CRUD operations for tasks
- Tailwind CSS for modern UI
- Django REST Framework APIs with Swagger documentation
- Docker support
- Pytest test suite


---

## 📁 Project Structure

```
taskmanager/                 # Django project root
├── taskmanager/             # Project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tasks/                   # Task app (models, views, forms, templates)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/          # Database migrations
│   ├── models.py            # Task models
│   ├── views.py             # Regular views (non-API)
│   ├── api/                 # DRF API views, serializers, and urls
│   │   ├── __init__.py
│   │   ├── serializers.py   # Serializers for Task model
│   │   ├── views.py         # API views for Task
│   │   └── urls.py          # API URL patterns for tasks
│   ├── forms.py             # Forms for task creation/editing
│   ├── templates/           # HTML templates for regular views
│   │   └── tasks/
│   │       ├── task_list.html
│   │       ├── task_form.html
│   │       └── task_confirm_delete.html
│   └── urls.py              # URL routing for the tasks app
├── users/                   # User registration/login
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py             # Forms for user registration/login
│   ├── models.py            # User-related models
│   ├── views.py             # Views for registration/login
│   ├── urls.py              # URL routing for the users app
│   └── templates/           # Templates for user authentication
│       └── registration/
│           ├── login.html
│           └── register.html
├── templates/               # Shared base templates
│   └── base.html            # Base template to extend
├── static/                  # Tailwind CSS and other static files
│   ├── css/
│   │   └── style.css        # Tailwind output
├── nginx/                   # Nginx folder
│   └── default.conf         # Nginx configuration for reverse proxy
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose configuration
├── requirements.txt         # Project dependencies
├── .dockerignore            # Docker ignore file to exclude unnecessary files
├── README.md                # Project documentation
└── manage.py                # Django management script



```

---

## 🚀 Features

- ✅ User registration, login, and logout
- ✅ Authenticated users can create/update/delete their own tasks
- ✅ Task status and due date tracking
- ✅ Styled with Tailwind CSS
- ✅ RESTful API with Swagger documentation
- ✅ Docker support for deployment
- ✅ Unit tests using Pytest

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/webcraft0123/task-management.git
cd task-management
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations and create a superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Compile Tailwind CSS (if applicable)

If you use `django-tailwind`, run:

```bash
python manage.py tailwind install
python manage.py tailwind build
```

---

## 🧪 Running the App Locally

```bash
python manage.py runserver
```

Then open your browser at:  
👉 http://127.0.0.1:8000/tasks/

---

## 🔐 Authentication

- Visit `/register/` to create a new account.
- Visit `/login/` to log in.
- Users can only see and manage their own tasks.

---

## 🖥️ Web Pages

| URL                      | Description              |
|--------------------------|--------------------------|
| `/register/`             | User registration page   |
| `/login/`                | Login page               |
| `/logout/`               | Logout                   |
| `/tasks/`                | List of user tasks       |
| `/tasks/create/`         | Create new task          |
| `/tasks/update/<id>/`    | Edit existing task       |
| `/tasks/delete/<id>/`    | Delete task              |

---

## 🔌 API Endpoints (DRF)

The API is available under `/api/`:

| Method | Endpoint           | Description           |
|--------|--------------------|-----------------------|
| GET    | `/api/tasks/`      | List user's tasks     |
| POST   | `/api/tasks/`      | Create new task       |
| GET    | `/api/tasks/<id>/` | Retrieve task         |
| PUT    | `/api/tasks/<id>/` | Update task           |
| DELETE | `/api/tasks/<id>/` | Delete task           |

### 📘 Swagger Docs
Visit:
```
http://127.0.0.1:8000/swagger/
```

---

## 🧪 Running Tests

To run tests using `pytest`:

```bash
pytest
```

Make sure `pytest-django` is installed.

Create a `pytest.ini` file:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = taskmanager.settings
```

---

## 🐳 Docker Deployment

To run the project with Docker:

### 1. Build and start containers

```bash
docker-compose up --build
```
After the containers are running, you need to apply the database migrations.

```bash
docker-compose exec app python manage.py migrate
```

### 2. Open in browser

```
http://localhost:8000/
```
### Stop the application

```bash
docker-compose down

```


## A Brief Explanation of My Approach

In this project, I aimed to create a scalable and easily deployable Task Manager application using Django as the backend framework. My approach focused on containerizing the application to simplify deployment and ensure consistency across different environments. Below are the key elements of my approach:

### Django for Backend
I used **Django**, a robust and well-supported Python web framework, for building the task management features. Django was chosen for its built-in functionalities like authentication, admin panel, and ORM, which made it easy to focus on the core task management features. The app allows users to register, log in, create tasks, and manage them (edit/delete).

### PostgreSQL as the Database
**PostgreSQL** was chosen as the database due to its strong support for data integrity and performance. It is a reliable, open-source database system that integrates smoothly with Django. The database stores tasks and user data, and the connection is configured using Django's ORM to interact with the database.

### Containerization with Docker
The project was **containerized** using **Docker** to create isolated environments for each component. This ensures that the application runs consistently across all systems, from development to production. With Docker, the entire app, including the Django app and PostgreSQL database, can be packaged into containers, reducing the risk of conflicts due to differing environments.

### Docker Compose for Multi-Container Setup
**Docker Compose** was used to manage the multi-container setup, which consists of the following services:
- **Django app** (running Gunicorn as the WSGI server): Handles the application logic and serves the backend API.
- **PostgreSQL database**: Stores the task data.
- **Nginx reverse proxy**: Routes incoming traffic to the Django application, handling HTTP requests on port 80 and passing them to the Django app on port 8000.

### Nginx as Reverse Proxy
**Nginx** was used as a reverse proxy to ensure a clean separation between the client-facing HTTP requests and the backend application. It also allows for future scalability (e.g., load balancing) and acts as a security layer, enabling features like SSL termination (in case you add HTTPS support later). It forwards requests to the Django app running on Gunicorn.
