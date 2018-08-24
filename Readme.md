## Stack API

A question and answer api tool like stackoverflow

# Description 
 The **stackoverflow-api** is the backbone of an application for managing questions and answers. The api provides features for registering a user, post a question and posting relevant answers to questions.


 ## Key Application features
1.	Register User
2.	Post a Question
3.	Post an Answer

## Development set up
- Check that python 3 is installed:
    ```
    python --v
    >> Python 3.6.5
    ```

- Install pipenv:
    ```
    brew install pipenv
    ```

- Check pipenv is installed:
    ```
    pipenv --version
    >> pipenv, version 2018.6.25
    ```

- Check that postgres is installed:
    ```
    postgres --version
    >> postgres (PostgreSQL) 10.1

    ```

- Clone the activo-api repo and cd into it:
    ```
    git clone https://github.com/victorjambo/stack-api.git

    ```
- Install dependencies:
    ```
    pipenv install
    ```

- Install dev dependencies to setup development environment:
    ```
    pipenv install --dev
    ```

- Rename the .env.sample file to .env and update the variables accordingly:
    ```
    FLASK_ENV = "development" # Takes either development, production, testing
    DATABASE_URI = "postgresql://YOUR_DB_USER:YOUR_DB_PASSWORD@YOUR_HOST/YOUR_DATABASE_NAME" # Development and production postgres db uri
    TEST_DATABASE_URI = "postgresql://YOUR_DB_USER:YOUR_DB_PASSWORD@YOUR_HOST/YOUR_TEST_DATABASE_NAME" # Testing postgres db uri
    ```

- Activate a virtual environment:
    ```
    pipenv shell
    ```

- Apply migrations:
    ```
    flask db upgrade
    ```

- If you'd like to seed initial data to the database:
    ```
    flask seed_database
    ```

- Run the application:
    ```
    python manage.py runserver
    ```

- Should you make changes to the database models, run migrations as follows
    - Migrate database:
        ```
        flask db migrate
        ```

    - Upgrade to new structure:
        ```
        flask db upgrade
        ```

- Deactivate the virtual environment once you're done:
    ```
    exit
    ```

## Running the API

Manually Test the endpoints with: [![Postman](https://run.pstmn.io/button.svg)](https://www.getpostman.com/apps)

**EndPoint** | **Functionality**
--- | ---
POST `/api/v1/users` | Creates a user account
GET `/api/v1/users` | List users
PUT `/api/v1/users` | Update Password or username
POST  `/api/v1/questions` | Post a question
PUT `/api/v1/questions/<questions_id>` | Updates a question
DELETE `/api/v1/questions/<questions_id>` | Remove a question
GET  `/api/v1/questions` | List questions
GET  `/api/v1/questions/<questions_id>` | Get a question
POST  `/api/v1/questions/<questions_id>/reviews` | Answer a question
GET  `/api/v1/questions/<questions_id>/reviews` | List answers for a question


## Testing

To run your tests use

```bash
$ nosetests
```

## ToDo
- [] Authentication
- [] Integrate CircleCI
