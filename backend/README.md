FastAPI TODO Application

This is a TODO application built with FastAPI, SQLAlchemy, and other modern Python libraries. It includes user authentication and user-specific task management.
Requirements

    Python 3.12+
    Poetry (for dependency management)

Installation

Clone the repository:
``` bash
git clone https://github.com/yourusername/fastapi_todo.git
cd fastapi_todo/backend
```
Install Poetry (if not already installed):

``` bash 
curl -sSL https://install.python-poetry.org | python3 -
```
Or follow the instructions from the official Poetry documentation.

Install dependencies:

``` bash
poetry install
```
Activate the virtual environment:
``` bash
poetry shell
```
Set up environment variables:

Create a .env file in the backend directory with the following content (replace the placeholders with actual values):

env
``` bash
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
Run database migrations:

``` bash
alembic upgrade head
```
Running the Application

Start the FastAPI server:

``` bash
uvicorn main:app --reload
```
This will start the server on http://127.0.0.1:8000.

Access the application:
    Open your web browser and go to http://127.0.0.1:8000/docs to see the interactive API documentation provided by Swagger UI.

Project Structure

    main.py: The entry point of the application.
    db/: Contains database models, schemas, and the database configuration.
    routers/: Contains the FastAPI routers for different endpoints.
    secure/: Contains security-related functions and dependencies.
    alembic/: Contains migration scripts for Alembic.

Dependencies

Here are the main libraries used in this project:

    FastAPI: Web framework for building APIs with Python 3.6+ based on standard Python type hints. <br>
    SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library. <br>
    Alembic: Database migration tool for SQLAlchemy. <br>
    Uvicorn: ASGI server implementation, using uvloop and httptools. <br>
    Pydantic: Data validation and settings management using Python type annotations. <br>
    Passlib: Password hashing library for Python.  <br>
    Email-validator: Library for validating email addresses. <br>


### Contact

telegram: @mirbekov0909 <br>
email: mirbekov1kylych@lgmail.com