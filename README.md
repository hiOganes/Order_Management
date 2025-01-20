# Order management

Веб-приложение на Django для управления заказами в кафе

## Table of Contents

- [Technologies](#technologies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Testing](#testing)
- [Development](#development)
- [License](#license)
- [Contacts](#contacts)

## Technologies

- Python 3.13.0
- Django 5.1.3
- PostgreSQL 17.0
- HTML

## Installation

1. Clone the repository
    ```sh
    git clone https://github.com/your-username/project-name.git
    cd project-name
    ```

2. Create and activate a virtual environment
    ```sh
    python -m venv venv
    source venv/bin/activate  # use `venv\Scripts\activate` for Windows
    ```

3. Install dependencies
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file and configure environment variables
    ```env
    DEBUG=True
    SECRET_KEY='your-secret-key'
    DATABASE_URL='your-database-url'
    ```

## Configuration

1. Apply database migrations
    ```sh
    python manage.py migrate
    ```

2. Create a superuser
    ```sh
    python manage.py createsuperuser
    ```

3. Collect static files
    ```sh
    python manage.py collectstatic
    ```

## Running the Project

1. Start the development server
    ```sh
    python manage.py runserver
    ```

2. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Testing

1. Run tests
    ```sh
    python manage.py test
    ```

## Development

### Project Structure

A brief description of the project structure and main directories.

- `project_name/` - root directory of the project
- `project_name/settings/` - Django settings
- `project_name/urls.py` - routing
- `app_name/` - your application
- etc.

### Common Commands

- Create an application
    ```sh
    python manage.py startapp app_name
    ```

- Apply migrations
    ```sh
    python manage.py migrate
    ```

- Create migrations
    ```sh
    python manage.py makemigrations
    ```

## License

Specify the license, for example, MIT.

## Contacts

Provide contact information for feedback.

- Email: your.email@example.com
- Telegram: [@your_username](https://t.me/your_username)
- Other contact methods
