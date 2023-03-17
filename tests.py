import json
import unittest
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db

# This creates a CastingTestCase class that inherits from unittest.TestCase. This class will contain the individual test methods.
class CastingTestCase(unittest.TestCase):

# Setting up the testing environment before running each test case
    def setUp(self):

        # Create a new Flask app for testing
        self.app = create_app()
        # Create a test client to send HTTP requests to the Flask app
        self.client = self.app.test_client
        setup_db(self.app)

        
        
        # Define some test data for creating a movie
        self.test_movie = {
            'title': 'Movie that doesnt exist',
            'release_year': 2054
        }

        
        # Define some test data for creating an actor
        self.test_actor = {
            'name': 'Jane Doesnotexist',
            'age': 22,
            'gender': 'female',
            'movie_id': 1
        }


        # Drop all tables in the database and create them again to have a fresh start
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.drop_all()
            self.db.create_all()


    # Executed after each test case
    def tearDown(self):
        pass

    # GET Endpoint Tests
    # -------------------------------------------------------------------------

    
    # SUCCESSFUL GET CASE
    # Creating a test for the /movies GET endpoint
    def test_get_movies(self):
        # Send a GET request to the /movies endpoint
        res = self.client().get('/movies')

        data = json.loads(res.data)

        # Check that the response status code is 200
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
    
    
    # FAILING GET CASE
    # Test for failing case of /movies GET endpoint
    def test_get_movies_fail(self):
        res = self.client().get('/m00vies')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Could not Find')

    # SUCCESSFUL GET CASE
    # Creating a test for the /actors GET endpoint
    def test_get_actors(self):
        res = self.client().get('/actors')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # FAIL GET CASE
    # Test for failing case of /actors GET endpoint
    def test_get_actors_fail(self):
        res = self.client().get('/acters')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Could not Find')

    # SUCCESSFUL POST CASE
    # Creating a test for the /movies/create POST endpoint
    def test_add_movie(self):
        res = self.client().post('/movies/create', json=self.test_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie_id'])

    # FAIL POST CASE
    # Creating a fail test for the /movies/create POST endpoint
    def test_add_movie_fail(self):
        res = self.client().post(
            '/movies/create',
            json={
                'title': 'Movie Title'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Request not processable')

    # SUCCESSFUL POST CASE
    # Creating a test for the /actors/create POST endpoint
    def test_add_actor(self):
        res = self.client().post('/actors/create', json=self.test_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor_id'])

    # FAIL POST CASE
    # Creating a fail test for the /actors/create POST endpoint
    def test_add_actor_fail(self):
        res = self.client().post('/actors/create', json={'name': 'John Doesntexist'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Request not processable')

    # SUCCESSFUL DELETE CASE
    # Creating a successful test for the /movies/delete/<movie_id> DELETE endpoint
    def test_delete_movie(self):
        res = self.client().delete('/movies/delete/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    # FAIL DELETE CASE
    # Creating a fail test for the /movies/delete/<movie_id> DELETE endpoint
    def test_delete_movie_fail(self):
        res = self.client().delete('/movies/delete/100000000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Could not Find')

    # SUCCESSFUL DELETE CASE
    # Creating a success test for the /actors/delete/<actor_id> DELETE endpoint
    def test_delete_actor(self):
        res = self.client().delete('/actors/delete/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    # FAIL DELETE CASE
    # Creating a Fail test for the /actors/delete/<actor_id> DELETE endpoint
    def test_delete_actor_fail(self):
        res = self.client().delete('/actors/delete/1023100000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Could not Find')

    # SUCCESSFUL UPDATE CASE
    # Creating a Success test for the /movies/update/<movie_id> UPDATE endpoint
    def test_update_movie(self):
        res = self.client().patch(
            '/movies/update/3',
            json={
                'title': 'New movie that doesnt exist'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie_id'])

    # FAIL UPDATE CASE
    # Creating a Fail test for the /movies/update/<movie_id> UPDATE endpoint
    def test_update_movie_fail(self):
        res = self.client().patch('/movies/update/100000000',
                                  json={'title': 'New movie title'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Could not Find')

    # SUCCESSFUL UPDATE CASE
    # Creating a Success test for the /actors/update/<actor_id> UPDATE endpoint
    def test_update_actor(self):
        res = self.client().patch(
            '/actors/update/2',
            json={
                'name': 'Updated Name'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor_id'])

    # FAIL UPDATE CASE
    # Creating a Fail test for the /actors/update/<actor_id> UPDATE endpoint
    def test_update_actor_fail(self):
        res = self.client().patch(
            '/actors/update/100000000',
            json={
                'name': 'Updated Name'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Could not Find')


if __name__ == '__main__':
    unittest.main()
