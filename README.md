# CAPSTONE PROJECT

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

# Models:

## Movies
with attributes title, director and release date
## Actors 
attributes name, age and gender
## Director 
attributes name, age and gender
# Endpoints:
GET /actors  , /movies and /directors 

DELETE /actors/ , /movies/ and /directors

POST /actors , /movies and /directors

PATCH /actors/ , /movies/ and /directors

## Roles:
admin
Can create , delete and edit actors and movies and directors
editor
Can only edit actors and movies and directors

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## API
there is a postman json file that contain all the API

## Heroku app
https://capstone-project-ipklaid.herokuapp.com


## Auth0 data
Auth0 Link: https://dev-ap4b1iwy.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=36yhDVCKItBN06jQ2yJWXzejcd6rtHFq&redirect_uri=http://localhost:8100/tabs/user-page

admin rule can do post, delete and patch 
admin account
