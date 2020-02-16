## Users Data API

### Technology used:

- Django
- Django-Rest-API
- MYSQL database

### How to run:

- RUN ```virtualenv -p python3 envname``` if virtualenv is not installed RUN ```pip install virtualenv```

- Activate virtualenv. 

- RUN ```pip install -r requirements.txt```

- create mysql database with name 'usersdb' set username and password in settings.py. 

- Data will be automatically imported from admin.py

- RUN ```python manage.py makemigrations```

- RUN ```python manage.py migrate```

- RUN ```python manage.py runserver```

### TEST Case

- For testing you can use Postman application to test the API. 

1. Get all users with certain parameters: 

```http://127.0.0.1:8000/api/v1/users/?page=1&limit=10&name=Les&sort=-age``` 

2. To GET all users: 

```http://127.0.0.1:8000/api/v1/users/``` 

3. POST add a user with post data: 

```http:127.0.0.1:8000/api/v1/users/```

4. GET certain User:

```http://127.0.0.1:8000/api/v1/users/1/```

5. PUT request for updating:

```http:127.0.0.1:8000/api/v1/users/1/``` 

6. DELETE request:

```http:127.0.0.1:8000/api/v1/users/1/```

