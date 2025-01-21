# Order management

Web application for managing orders in a cafe

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
    ```
    git clone https://github.com/hiOganes/Order_Management.git
    ```

2. Create and activate a virtual environment
    ```
    python -m venv venv
    source venv/bin/activate # for linux
    venv\Scripts\activate # for Windows
    ```

3. Install dependencies
    ```
    pip install -r requirements.txt
    ```

4. Create a `.env` file and configure environment variables
    ```
    DEBUG=True
    SECRET_KEY='your-secret-key'
    DATABASES = {"ENGINE": "django.db.backends.postgresql", "NAME": "your-name", "USER": "your-user", "PASSWORD": "your-password", "HOST": "localhost", "PORT": "5432"}
    ```

## Configuration

1. Apply database migrations
    ```
    python manage.py migrate
    ```

## Running the Project

1. Start the development server
    ```
    python manage.py runserver
    ```

2. Open your browser and go to [Website](http://127.0.0.1:8000/orders/create/)
3. Open your browser and go to [OpenAPI](http://127.0.0.1:8000/api/schema/swagger-ui/)

## Testing

 ```
   python manage.py loaddata fixtures/db_orders.json # Loading data into the database
   python manage.py test # Run tests
   ```