from app import create_app
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, db, Director, Movie, Actor, Casting, db_drop_and_create_all
from auth import AuthError, requires_auth
import json
import unittest
import os


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client

        self.admin_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IklteDcwZWswekZZdENEUEpTbVZxRyJ9.eyJpc3MiOiJodHRwczovL2Rldi1hcDRiMWl3eS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY0NTkyZDcxNDYxNjEwMDZkMjUwN2Q1IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1OTg0NjgxODIsImV4cCI6MTU5ODU0MDE4MSwiYXpwIjoiMzZ5aERWQ0tJdEJOMDZqUTJ5SldYemVqY2Q2cnRIRnEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6ZGlyZWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOmRpcmVjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDpkaXJlY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.HLXa9Gwu71tAlykh83h823Zx8fL4540uwFCjkmlOInbhVV5EQLhQp1JZ8SQbkPbcbqHDid81UR02VEOkruNiZJkQ-I-ON6axnX6E3-XYv31_W14qSfoyqZGUI8BDrVELBsS8-f6XUBn5GLv3RY9Tj2QlUUC2hMvxO9vJ1ud7kCvPslnMWiIbpaXUa3i6M-DjDt1F5WVJH2DYLRu7NEWuvZHkqoR8xCZeU6Voh12OxOMzW7xP1EGPV_q_aJlUuidumhx84DHf7VDyTvMDFRJzSQBF4fOviWvHvMn7FyPDEccV_dBsfezWZq-qBrDQDrlO63mj345NbhpVouBMGdmM0Q'
        self.editor_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IklteDcwZWswekZZdENEUEpTbVZxRyJ9.eyJpc3MiOiJodHRwczovL2Rldi1hcDRiMWl3eS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY0NTkxZTdlOWVmNWYwMDY3YjU2MGNlIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE1OTg0NjkzMzUsImV4cCI6MTU5ODU0MTMzNCwiYXpwIjoiMzZ5aERWQ0tJdEJOMDZqUTJ5SldYemVqY2Q2cnRIRnEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInBhdGNoOmFjdG9ycyIsInBhdGNoOmRpcmVjdG9ycyIsInBhdGNoOm1vdmllcyJdfQ.wPztATtDJHfVvNHfSEfxNyGZUhJurG0AGxgeB49VGBTRHRRImVvyfPJDKNWm3NdnKSpdfBIy9UYg4cqNxjgqz5UapA68jD0LHHuBSFrR-2UTN-AZXCJ6H3spfrL3DDv_UG-k9wpmS8MiYMrDwHzCPfI8O6YcOTIzo_qCY3jUPcCyB792U626tQI1HKT9QUQy0yo8DFfxRE5LYXIhI9M1gR-agukUZ98v8vC3OO5N4N2QsxgmP4pIc04FgJVhE8cRpI678GeTsvD9Z-6YwYrMsPSJFnp_9E7srHHeyb5N3LJsxGkvhbI0rShfLQmY-cFG8qpdfB6gKl49li8q4sCY3w'

        self.database_path = "postgres://postgres:1234@localhost:5432/test_data"

        setup_db(self.app, self.database_path)
        db_drop_and_create_all()
        Director.insertData()
        Actor.insertData()
        Movie.insertData()

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # GET requests

    # Actor

    def test_get_actors(self):

        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_get_actor_detail(self):

        res = self.client().get('/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['id'])

    def test_404_get_actor_detail(self):

        res = self.client().get('/actors/20')
        data = json.loads(res.data)


        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # Movie
    def test_get_movies(self):

        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_get_movies_detail(self):

        res = self.client().get('/movies/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['id'])

    def test_404_get_movies_detail(self):

        res = self.client().get('/movies/20')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # director

    def test_get_directors(self):

        res = self.client().get('/directors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['directors'])

    def test_get_directors_detail(self):

        res = self.client().get('/directors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['id'])

    
    def test_404_get_directors_detail(self):

        res = self.client().get('/directors/22')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    #POST requests

    #actor

    def test_post_actors(self):
        res = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format(self.admin_token)
        }, json={"name": "example",
                 "gender": "Female",
                 "birth_date": "1997/12/3"})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["success"])
        self.assertIn('actor', data)

    def test_404_post_actors(self):
        res = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format(self.admin_token)
        }, json={"name": "example",
                "gender": "Female"})

        self.assertEqual(res.status_code, 401)
        
    

    #movie

    def test_post_movies(self):
        res = self.client().post('/movies', headers={
            'Authorization': "Bearer {}".format(self.admin_token)
        }, json={"name": "example",
                 "director_id": 2,
                 "relese_date": "2020/8/12"})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["success"])
        self.assertIn('movie', data)

    def test_404_post_movies(self):
        res = self.client().post('/movies', headers={
            'Authorization': "Bearer {}".format(self.admin_token)
        }, json={"name": "example",
                "gender": "Female"})

        self.assertEqual(res.status_code, 401)


    # directors

    def test_post_directors(self):
        res = self.client().post('/directors', headers={
            'Authorization': "Bearer {}".format(self.admin_token)
        }, json={"name": "example",
                 "gender": "Female",
                 "birth_date": "1997/12/3"})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["success"])
        self.assertIn('director', data)

    def test_404_post_directors(self):
        res = self.client().post('/directors', headers={
            'Authorization': "Bearer {}".format(self.admin_token)
        }, json={"name": "example",
                "gender": "Female"})

        self.assertEqual(res.status_code, 401)

    # DELETE requests

    #actor

    def test_delete_actors(self):
        res = self.client().delete('/actors/2', headers={
            'Authorization': "Bearer {}".format(self.admin_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["success"])
        self.assertIsNotNone('delete')

    def test_404_delete_actors(self):
        res = self.client().delete('/actors/22', headers={
            'Authorization': "Bearer {}".format(self.admin_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    # movie

    def test_delete_movies(self):
        res = self.client().delete('/movies/2', headers={
            'Authorization': "Bearer {}".format(self.admin_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["success"])
        self.assertIsNotNone('delete')
    
    def test_404_delete_movies(self):
        res = self.client().delete('/movies/22', headers={
            'Authorization': "Bearer {}".format(self.admin_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    # directors

    def test_delete_directors(self):
        res = self.client().delete('/directors/2', headers={
            'Authorization': "Bearer {}".format(self.admin_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["success"])
        self.assertIsNotNone('delete')

    def test_404_delete_directors(self):
        res = self.client().delete('/directors/22', headers={
            'Authorization': "Bearer {}".format(self.admin_token)
        })

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        




    # PATCH requests success
    # actor

    def test_patch_actors(self):
        res = self.client().patch('/actors/3', headers={
            'Authorization': "Bearer {}".format(self.editor_token)
        }, json={"name": "example",
                 "gender": "Female",
                 "birth_date": "1997/12/3"})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["success"])
        self.assertIn('actor', data)

    def test_404_patch_actors(self):
        res = self.client().patch('/actors/22', headers={
            'Authorization': "Bearer {}".format(self.editor_token)
        }, json={"name": "example",
                 "gender": "Female",
                 "birth_date": "1997/12/3"})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    # movie

    def test_patch_movies(self):
        res = self.client().patch('/movies/3', headers={
            'Authorization': "Bearer {}".format(self.editor_token)
        }, json={"name": "example",
                 "director_id": 2,
                 "relese_date": "2020/8/12"})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["success"])
        self.assertIn('movie', data)

    def test_404_patch_movies(self):
        res = self.client().patch('/movies/22', headers={
            'Authorization': "Bearer {}".format(self.editor_token)
        }, json={"name": "example",
                 "gender": "Female",
                 "birth_date": "1997/12/3"})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)

    # directors

    def test_patch_directors(self):
        res = self.client().patch('/directors/3', headers={
            'Authorization': "Bearer {}".format(self.editor_token)
        }, json={"name": "example",
                 "gender": "Female",
                 "birth_date": "1997/12/3"})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["success"])
        self.assertIn('director', data)


    def test_404_patch_directors(self):
        res = self.client().patch('/directors/22', headers={
            'Authorization': "Bearer {}".format(self.editor_token)
        }, json={"name": "example",
                 "gender": "Female",
                 "birth_date": "1997/12/3"})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)


    #  false auth
    #admin token
    def test_post_actors(self):
        res = self.client().post('/actors', headers={
            'Authorization': "Bearer {}".format('bvkdsbhjsdjhvfdsjhvfjs')
        }, json={"name": "example",
                 "gender": "Female",
                 "birth_date": "1997/12/3"})

        

        self.assertEqual(res.status_code, 500)
    
    #editor token
    def test_false_auth_editor(self):
        res = self.client().patch('/actors/3', headers={
            'Authorization': "Bearer {}".format('gjdhfjgkhdfjkghjkdfhgjkdfh')
        }, json={"name": "example",
                 "gender": "Female",
                 "birth_date": "1997/12/3"})


        self.assertEqual(res.status_code, 500)

 
        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
