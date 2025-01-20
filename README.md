# Order management

Веб-приложение на Django для управления заказами в кафе

## Table of Contents

- [Technologies](#technologies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Testing](#testing)

## Technologies

- Python 3.13.0
- Django 5.1.3
- PostgreSQL 17.0
- HTML

## Installation

1. Clone the repository
    ```sh
    git clone git@github.com:hiOganes/Order_Management.git
    ```

2. Create and activate a virtual environment
    ```sh
    python -m venv venv
    for linux: source venv/bin/activate
    for Windows: venv\Scripts\activate
    ```

3. Install dependencies
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file and configure environment variables
    ```env
    DEBUG=True
    SECRET_KEY='your-secret-key'
    DATABASES = {"ENGINE": "django.db.backends.postgresql", "NAME": "your-name", "USER": "your-user", "PASSWORD": "your-password", "HOST": "localhost", "PORT": "5432"}
    ```

## Configuration

1. Apply database migrations
    ```sh
    python manage.py migrate
    ```

## Running the Project

1. Start the development server
    ```sh
    python manage.py runserver
    ```

2. Open your browser and go to [Website](http://127.0.0.1:8000/orders/create/)
3. Open your browser and go to [OpenAPI](http://127.0.0.1:8000/api/schema/swagger-ui/)

## Testing

1. Run tests
    ```sh
    python manage.py test
    ```
