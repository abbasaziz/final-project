# Casting Agency Project



##### Main Project Dependencies

- **Flask** - Slim python web library.
- **SQLAlchemy** - A very useful Python ORM library.
- **Heroku** or **Render** - PaaS platform for easy hosting of web applications
- **Postman** - An API testing tool for your system to check the app locally.

### Installation instructions

- Clone the project from the [repository](https://github.com/abbasaziz/final-project) to a directory on your own machine.
- Create a virtualenv in project directory using the cli commands 
- Type and run `pip install -r requirements.txt` to install all the dependencies
- Inside the setup.sh file update the `DATABASE_URL` with appropriate environment variables of your system and database.
- On Unix systems, use `export DATABASE_URL={username}:{password}@{host}:{port}/{database_name}`
- On Windows systems, use `set $DATABASE_URL="{username}:{password}@{host}:{port}/{database_name}"`
- After that, run `export FLASK_APP=app.py`(for Unix) and `set $FLASK_APP="app.py"`
- Once all that is done, execute `flask run` in terminal

### Endpoints

- **GET endpoint** with /actors and /movies.
- **DELETE endpoint** with /actors/ and /movies.
- **POST endpoint** with /actors and /movies.
- **PATCH endpoint** with /actors/ and /movies.

### Roles

- Casting Assistant

  - The casting assistant gets access to the actors and movies in the database
  - GET /actors and /movies

- Casting Director

  - The casting director gets access to the actors and movies. Can post and delete actors. Also update existing actors and movies.
  - GET /actors and /movies
  - ADD /actors and DELETE /actors
  - PATCH /actors and /movies

- Executive Producer

  - The executive producer gets access to the actors and movies. Can post and delete actors. Can post and delete movies. Also update existing actors and movies.
  - GET /actors and /movies
  - ADD /actors and DELETE /actors
  - PATCH /actors and /movies
  - ADD /movies and DELETE /movies

### JWT Tokens for each role:

- Casting Assistant (Basic user)- `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InM2ak83SUtoNEU4cC1rMDI4SUVfNiJ9.eyJpc3MiOiJodHRwczovL2Rldi14bXFseWZ3bTZ5a3Uxa2hkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDEzZWJmZjhjY2EyZGIyMzRiNDlhZjkiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjc5MDY5MTgxLCJleHAiOjE2NzkwNzYzODEsImF6cCI6IjdLeDlqeXVuTnlLWWt4YUE3MlBVZ1pmZ0FRSmN6U0doIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkaXNwbGF5OmFjdG9ycyIsImRpc3BsYXk6bW92aWVzIl19.EuOa7tiXztnx2KaxheafASz_fkMfrs6sB5bGEGcUHkQFIad4Mp2h7aHe7QW9GbIk_viNK7H1Vz2eWbtBYGbbD8TN9KQ-CpaxK6oY5muzJoI4hWecZbooseN6qqhv3sym2X6jwgcWGUdW4Eu2sNBBj4MCRdWit0wOmEolXVOA2qOLztrTbyR1DOolfupPUmhywBOa_8TXwd_weH9LTbkZHgPkNsXDuVd0_A_rSuGPVLGAcusPwjB_m3N-aP4OIau1938ZsCyVSzRRzH59uIYGU34PydlJ-H8nLCFW8Z3iUqyYPvb8tiq11KL1oISzEBrwK32D92P0Q2mpaSPLTjM0dw`

- Casting Director - `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InM2ak83SUtoNEU4cC1rMDI4SUVfNiJ9.eyJpc3MiOiJodHRwczovL2Rldi14bXFseWZ3bTZ5a3Uxa2hkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDEzZTllZDczOTk3NmI3NDcwZDM0ZGYiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjc5MDY5MDk3LCJleHAiOjE2NzkwNzYyOTcsImF6cCI6IjdLeDlqeXVuTnlLWWt4YUE3MlBVZ1pmZ0FRSmN6U0doIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiZGlzcGxheTphY3RvcnMiLCJkaXNwbGF5Om1vdmllcyIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJyZW1vdmU6YWN0b3JzIl19.fQeeZ-0uYPJEPiSfql1ZDOCjXbc6OhvlmC1EhYIoNsHVdXxvjwxQ0DWcw0-RWytQ2_PtqNlN1FS09RY4BbSxGMsAhZwZdbh6-Fh_8NqXO6u6FDQfkg0l534GsAM82FvA_7WOZIOv2Fqt8ZWcITg5e5GupVChpWAucYzPuAec0-n-W73gd0T5NzaKy4ehkC50VNxc0UoU6JbdPJnpNyeuIXOKKHFfhsRT0uoqY4uryMS6_QzFGPcv7KdvOXYVNuX4gPaPiycwsmnVbx6jEmiL2U__Gu_gKd8slNFaHjDtF6qw1ZI8GH5zF7zEwKvDeoQHada77F6mQR5pG1hXAuF26A`

- Executive Producer - `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InM2ak83SUtoNEU4cC1rMDI4SUVfNiJ9.eyJpc3MiOiJodHRwczovL2Rldi14bXFseWZ3bTZ5a3Uxa2hkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDEzZTg5NmE0NzY3MTc5N2EzZTAzZTgiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjc5MDY5MDMwLCJleHAiOjE2NzkwNzYyMzAsImF6cCI6IjdLeDlqeXVuTnlLWWt4YUE3MlBVZ1pmZ0FRSmN6U0doIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiYWRkOm1vdmllcyIsImRpc3BsYXk6YWN0b3JzIiwiZGlzcGxheTptb3ZpZXMiLCJlZGl0OmFjdG9ycyIsImVkaXQ6bW92aWVzIiwicmVtb3ZlOmFjdG9ycyIsInJlbW92ZTptb3ZpZXMiXX0.oGRlCQGPHGACEZfcmAV7mutiscmyGzeDrtzLaNb478jRdEnOzcHFawNTDwJ0sVKtLqSnF1Z7DjZo-xl0I-pK9FCBhIXUF8r6pcnHJ-HwtZQNa5_yP0Wfcm4GE4VO3V3o0N4wWnpi_YA2iq-cv53kApG7YYcRApA9fKfbGFdUVPoDxwOHNJ2TnmJSjRWe1L3avTIJv0frJP4NQuU-YAx6tEAuYE0M8TKkyJER1mu0-q4cGICQ12OhiEsr9C_5ATB4s_9BjfRw1w4BwozZQxWEW9ZKhuWUoEPuKxTnr942WoGXQxeNr9Nr4RbWcenkyCX5gTWBKLkuYw7TDZ_si03PEA`

## API Endpoints

Now we will cover all the endpoints in the application one by one along with their functionality.

### The Default Path

#### GET /

Verifies that application is up and running on Render, AWS or Heroku.

Sample response:

```
{
    "description": "App is running.",
    "success": true
}
```

### Application's GET Endpoints

#### GET /movies

Shows all the movies listed inside the app's database.

Sample response:

```
{
    "movies": [
        {
            "id": 3,
            "release_year": 2005,
            "title": "Batman Begins"
        },
        {
            "id": 4,
            "release_year": 2015,
            "title": "Interstellar"
        },
    ],
    "success": true
}
```

#### GET /actors

Shows all the actors and actresses listed inside the app's postgres database.

Sample response:

```
{
    "actors": [
        {
            "age": 30,
            "gender": "female",
            "id": 3,
            "movie_id": 2,
            "name": "Jennifer Lawrence"
        },
        {
            "age": 58,
            "gender": "male",
            "id": 4,
            "movie_id": 3,
            "name": "Matt Damon"
        },
    ],
    "success": true
}
```

### POST Endpoints

#### POST /movies/create

Adds a new movie into the app's database.

Sample response:

```
{
    "movie_id": 8,
    "success": true
}
```

#### POST /actors/create

Adds a new actor or actress into the app's database.

Sample response:

```
{
    "actor_id": 6,
    "success": true
}
```

### PATCH Endpoints

#### PATCH /movies/update/<movie_id>

Edits the movie details for an existing movie_id and newly updated attribute info.

Sample response:

```
{
    "movie_id": 6,
    "success": true
}
```

#### PATCH /actors/update/<actor_id>

Edits the movie details for an existing actor_id and newly updated attribute info.

Sample response:

```
{
    "actor_id": 2,
    "success": true
}
```

### DELETE Endpoints

#### DELETE /movies/delete/<movie_id>

Removes a specific movie's entry from the app's database using the given movie_id.

Sample response:

```
{
    "deleted": 1,
    "success": true
}
```

#### DELETE /movies/actors/<actor_id>

Removes a specific actor or actress's entry from the app's database using the given actor_id.

Sample response:

```
{
    "deleted": 1,
    "success": true
}
```

## Author

Abbas Aziz [abbasaziz](https://github.com/abbasaziz)
