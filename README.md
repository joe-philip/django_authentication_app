# Django simple authentication app

## Requirements

- Python >=3.10

## Seting up project locally

1. Create virtual environment `python -m venv env`
1. Activate virtual environment `source env/bin/activate`
1. Install Requirements `pip install -r requirements.txt`
1. Create `.env` file
    ```
    SECRET_KEY
    ALLOWED_HOSTS
    DEBUG
    DATABASE_URL
    ```
1. Make migrations `python manage.py makemigrations`
1. Apply migrations `python manage.py migrate`
1. Load fixtures `python manage.py loaddata *.json`
1. Create superuser `python manage.py createsuperuser`
1. Run server `python manage.py runserver`

## .env variables

###### SECRET_KEY
A secret key used to sign cookies and other sensitive data. defaults to `django-insecure-r=#*ay%+%kw5fuso3-g!yv4z-fh$46r(44s8t!(bd()c0t-71p`. Random key can be generated using `python manage.py secret_key_gen`.
###### ALLOWED_HOSTS
List of hostnames that are allowed to access the app. defaults to `[]`
###### DEBUG
Set to `True` to enable debug mode. defaults to `False`
###### DATABASE_URL
The URL of the database to use. defaults to `sqlite:///db.sqlite3`
