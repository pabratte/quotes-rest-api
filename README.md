# Quotes REST API

Simple quote management system for storing and editing simple quotes. Created as an exercise for a technical interview using Django REST Framework.

The REST API for quotes has endpoints for:

* Fetching all existing quotes
* Fetching a specific existing quote by it's ID 
* Creating a new quote
* Updating an existing quote by it's ID
* Deleting an existing quote by it's ID

Request are also validated using [Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)


### Running the server

```sh
# create a Python3 virtual environment and activate it
python3 -m venv venv
source venv/bin/activate

# install dependiencies
pip install -r requirements

# run migrations
python manage.py migrate

# create user to authenticate requests
python manage.py createsuperuser --username user --email user@example.com

# run server
python manage.py runserver
```


### Testing the API with curl
 
```sh
# Fetching all existing quotes
curl --user user:password http://127.0.0.1:8000/api/quotes/

# Updating quote with id: 1
curl --user user:password http://127.0.0.1:8000/api/quotes/1

# Creating a new quote
curl --user user:password -X POST http://127.0.0.1:8000/api/quotes/ -H "Content-Type: application/json" -d '{"quote":"This is a new quote", "author":"This is the author"}'

# Updating quote with id: 3
curl --user user:password -X PUT http://127.0.0.1:8000/api/quotes/3 -H "Content-Type: application/json" -d '{"quote":"This is a modified quote", "author":"This is the modified author"}'

# Deleting quote with id: 4
curl --user user:password -X DELETE http://127.0.0.1:8000/api/quotes/4
```