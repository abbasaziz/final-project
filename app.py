from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

from auth import AuthError, requires_auth
from models import setup_db, create_tables, Movie, Actor


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app, resources={r'/api/': {'origins': '*'}})

    setup_db(app)
    create_tables()




    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization, True')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, POST, DELETE, PATCH, OPTIONS')
        return response


#<-------------- API Endpoints for APP Functionality ----------------> 

    # Basic endpoint to check if the app is deployed properly or not 
    @app.route('/', methods=['GET'])
    def health_check():
        return jsonify({
            'success': True,
            'description': 'App is running successfully.'
        })
    


    # GET endpoint API to display movies for a visitor after login 
    @app.route('/movies', methods=['GET'])
    @requires_auth('display:movies')
    def get_movies(jwt):
        movies = Movie.query.all()

        if not movies:
            abort(404)

        movies = [movie.format() for movie in movies]

        return jsonify({
            'success': True,
            'movies': movies
        })




    # POST endpoint to define route for adding a new movie
    @app.route('/movies/new', methods=['POST'])
    # Require authentication to add a movie
    @requires_auth('add:movies')
    def add_movie(jwt):
        # Get JSON data from request
        body = request.get_json()

        # Extract movie title and release year from JSON data
        title = body.get('title')
        release_year = body.get('release_year')

        # If the title or release year are missing, return an error
        if not (title and release_year):
            abort(422)

        try:
            # Create a new movie with the given title and release year
            movie = Movie(title=title, release_year=release_year)
            # Insert the new movie into the database
            movie.insert()

            # Return a JSON response indicating that the movie was added successfully
            return jsonify({
                'success': True,
                'movie_id': movie.id
            })
        except BaseException:
            # If an error occurs, return an error response
            abort(422)




    # DELETE endpoint for the API
    @app.route('/movies/delete/<int:movie_id>', methods=['DELETE'])
    @requires_auth('remove:movies')
    def delete_movie(jwt, movie_id):
        # Get the movie with the given movie_id
        movie = Movie.query.get(movie_id)

        # If the movie exists
        if movie:
            try:
                # Delete the movie from the database
                movie.delete()

                # Return a success message
                return jsonify({
                    'success': True,
                    'deleted': movie_id
                })
            
            # If there was an error, return a 422 Unprocessable Entity error
            except BaseException:
                abort(422)
        # If the movie does not exist, return a 404 Not Found error
        else:
            abort(404)




    @app.route('/movies/update/<int:movie_id>', methods=['PATCH'])
    @requires_auth('edit:movies')
    def update_movie(jwt, movie_id):
        # Get the movie object with the specified movie_id from the database
        movie = Movie.query.get(movie_id)

        # If the movie exists, try to update it with the new data in the request body
        if movie:
            try:
                # Get the request body and extract the title and release year
                body = request.get_json()
                title = body.get('title')
                release_year = body.get('release_year')
                
                # Update the movie object with the new title and release year, if provided
                if title:
                    movie.title = title
                if release_year:
                    movie.release_year = release_year

                # Commit the changes to the database
                movie.update()

                # Return a JSON response indicating that the update was successful
                return jsonify({
                    'success': True,
                    'movie_id': movie.id
                })
            except BaseException as e:
                # If there was an error updating the movie, return a 422 Unprocessable Entity error
                print(e)
                abort(422)
        else:
            # If the movie does not exist, return a 404 Not Found error
            abort(404)





    # Define a route for GET requests to '/actors'
    @app.route('/actors', methods=['GET'])
    @requires_auth('display:actors')
    def get_actors(jwt):
        # Retrieve all actors from the database
        actors = Actor.query.all()

        # If there are no actors, return 404 error
        if not actors:
            abort(404)

        # Format actors as dictionary and add them to a list
        actors = [actor.format() for actor in actors]

        # Return a JSON response with success status and list of actors
        return jsonify({
            'success': True,
            'actors': actors
        })
    





    @app.route('/actors/new', methods=['POST'])
    @requires_auth('add:actors')
    def add_actor(jwt):
        # Get the JSON data from the request body
        body = request.get_json(force=True)

        # Extract the name, age, gender, and movie ID from the JSON data
        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')
        movie_id = body.get('movie_id')
        print(name, age, gender, movie_id)

        # Check that all required fields are present
        if not (name and age and gender and movie_id):
            abort(422)

        try:
            # Create a new Actor object with the provided data
            actor = Actor(name=name,
                        age=age,
                        gender=gender,
                        movie_id=movie_id)

            # Insert the new actor into the database
            actor.insert()

            # Return a JSON response indicating success and the new actor's ID
            return jsonify({
                'success': True,
                'actor_id': actor.id
            })
        except BaseException as e:
            # If there is an error, print it and return an HTTP 422 error code
            print(e)
            abort(422)


    # Decorator to handle HTTP DELETE requests to delete an actor with given actor_id
    @app.route('/actors/delete/<int:actor_id>', methods=['DELETE'])
    @requires_auth('remove:actors')

    # Function to handle deleting an actor with given actor_id
    def delete_actors(jwt, actor_id):
        # Find the actor with given actor_id
        actor = Actor.query.get(actor_id)

        if actor:
            try:
                # Delete the actor
                actor.delete()

                # Return success message with actor_id of deleted actor
                return jsonify({
                    'success': True,
                    'deleted': actor_id
                })
            
            except BaseException:
                # If there is any error while deleting, abort with HTTP status code 422
                abort(422)
            
        else:
            # If the actor with given actor_id is not found, abort with HTTP status code 404
            abort(404)



    # This route allows updating an actor with a specific ID using a PATCH request
    @app.route('/actors/update/<int:actor_id>', methods=['PATCH'])
    @requires_auth('edit:actors')
    def update_actors(jwt, actor_id):
        # Retrieve the actor with the given ID from the database
        actor = Actor.query.get(actor_id)

        # If the actor exists in the database
        if actor:
            try:
                # Get the JSON body of the request
                body = request.get_json()

                # Extract the fields to update from the JSON body
                name = body.get('name')
                age = body.get('age')
                gender = body.get('gender')
                movie_id = body.get('movie_id')

                # Update the actor object with the new field values, if provided
                if name:
                    actor.name = name
                if age:
                    actor.age = age
                if gender:
                    actor.gender = gender
                if movie_id:
                    actor.movie_id = movie_id

                # Update the actor in the database
                actor.update()

                # Return a JSON response indicating success and the ID of the updated actor
                return jsonify({
                    'success': True,
                    'actor_id': actor.id
                })

            # If an exception is raised during the update, abort with a 422 error
            except BaseException:
                abort(422)

        # If the actor with the given ID is not found in the database, abort with a 404 error
        else:
            abort(404)


#<-------------- Endpoints for handling ERRORS ----------------> 
    # For 422 Error
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Request not processable'
        }), 422
    

    # For 404 Error
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Could not Find'
        }), 404


    # For 401 Error in Authentication
    @app.errorhandler(AuthError)
    def handle_auth_errors(x):
        return jsonify({
            'success': False,
            'error': x.status_code,
            'message': x.error
        }), 401

    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=8080, debug=True)
