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

## herokuapp
https://capstone-project-ipklaid.herokuapp.com


## Auth0 data
Auth0 Link: https://dev-ap4b1iwy.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=36yhDVCKItBN06jQ2yJWXzejcd6rtHFq&redirect_uri=http://localhost:8100/tabs/user-page

admin rule can do post, delete and patch 
admin account

Email: admin@admin.com
Password: meaM1234


editor can only do patch

Email: editor@admin.com
Password: meaM1234

Auth0 Link: https://dev-ap4b1iwy.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=36yhDVCKItBN06jQ2yJWXzejcd6rtHFq&redirect_uri=http://localhost:8100/tabs/user-page




adminToken: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IklteDcwZWswekZZdENEUEpTbVZxRyJ9.eyJpc3MiOiJodHRwczovL2Rldi1hcDRiMWl3eS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY0NTkyZDcxNDYxNjEwMDZkMjUwN2Q1IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1OTg0NjgxODIsImV4cCI6MTU5ODU0MDE4MSwiYXpwIjoiMzZ5aERWQ0tJdEJOMDZqUTJ5SldYemVqY2Q2cnRIRnEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6ZGlyZWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOmRpcmVjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDpkaXJlY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.HLXa9Gwu71tAlykh83h823Zx8fL4540uwFCjkmlOInbhVV5EQLhQp1JZ8SQbkPbcbqHDid81UR02VEOkruNiZJkQ-I-ON6axnX6E3-XYv31_W14qSfoyqZGUI8BDrVELBsS8-f6XUBn5GLv3RY9Tj2QlUUC2hMvxO9vJ1ud7kCvPslnMWiIbpaXUa3i6M-DjDt1F5WVJH2DYLRu7NEWuvZHkqoR8xCZeU6Voh12OxOMzW7xP1EGPV_q_aJlUuidumhx84DHf7VDyTvMDFRJzSQBF4fOviWvHvMn7FyPDEccV_dBsfezWZq-qBrDQDrlO63mj345NbhpVouBMGdmM0Q



newEditorTokin: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IklteDcwZWswekZZdENEUEpTbVZxRyJ9.eyJpc3MiOiJodHRwczovL2Rldi1hcDRiMWl3eS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY0NTkxZTdlOWVmNWYwMDY3YjU2MGNlIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1OTg0NjkzMzUsImV4cCI6MTU5ODU0MTMzNCwiYXpwIjoiMzZ5aERWQ0tJdEJOMDZqUTJ5SldYemVqY2Q2cnRIRnEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInBhdGNoOmFjdG9ycyIsInBhdGNoOmRpcmVjdG9ycyIsInBhdGNoOm1vdmllcyJdfQ.wPztATtDJHfVvNHfSEfxNyGZUhJurG0AGxgeB49VGBTRHRRImVvyfPJDKNWm3NdnKSpdfBIy9UYg4cqNxjgqz5UapA68jD0LHHuBSFrR-2UTN-AZXCJ6H3spfrL3DDv_UG-k9wpmS8MiYMrDwHzCPfI8O6YcOTIzo_qCY3jUPcCyB792U626tQI1HKT9QUQy0yo8DFfxRE5LYXIhI9M1gR-agukUZ98v8vC3OO5N4N2QsxgmP4pIc04FgJVhE8cRpI678GeTsvD9Z-6YwYrMsPSJFnp_9E7srHHeyb5N3LJsxGkvhbI0rShfLQmY-cFG8qpdfB6gKl49li8q4sCY3w
