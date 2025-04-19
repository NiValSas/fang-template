# Fang Template Project

This is a template for a FastAPI project that includes common structure and configurations for fast development and best practices. 

## Features
- CI/CD pipeline (GitHub Actions)
- Docker support
- Environment variable management with `.env`
- Project structure based on separation of concerns

## Requirements
- Python 3.9+
- Docker (optional)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-org/fang-template.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the FastAPI app:
    ```bash
    uvicorn app.main:app --reload
    ```
4. Access the application:
    ```bash
    http://localhost:8000
    ```

## Structure
    fang-template/
    ├── .github/
    │   ├── workflows/
    │   │   ├── backport.yml
    │   │   ├── ci-cd.yml
    │   │   ├── validate_branch_name.yml
    │   │   ├── python-security.yml
    │   │   ├── deploy.yml
    │   ├── pull_request_template.yml
    ├── app/
    │   ├── __init__.py
    │   ├── config/
    │   │   ├── __init__.py
    │   ├── controllers/
    │   │   ├── __init__.py
    │   ├── middlewares/
    │   │   ├── __init__.py
    │   ├── models/
    │   │   ├── __init__.py
    │   ├── services/
    │   │   ├── __init__.py
    │   └── main.py
    ├── Dockerfile
    ├── .gitignore
    ├── .env
    ├── README.md
    └── requirements.txt