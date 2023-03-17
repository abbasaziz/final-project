# Casting Agency Project

Final Project for Full-Stack Nano-Degree program. You can access the full project deployed at Render [here](https://final-project-service-nkei.onrender.com/).

##### Main Project Dependencies

- **Flask** - Slim python web library.
- **SQLAlchemy** - A very useful Python ORM library.
- **Heroku** or **Render** - PaaS platform for easy hosting of web applications
- **Postman** - An API testing tool for your system to check the app locally.

### Installation instructions

- Clone the project from the [repository](https://github.com/abbasaziz/final-project) to a directory on your own machine.
- Create a virtualenv in project directory
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

- Casting Assistant (Basic user)- `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InM2ak83SUtoNEU4cC1rMDI4SUVfNiJ9.eyJpc3MiOiJodHRwczovL2Rldi14bXFseWZ3bTZ5a3Uxa2hkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDEzZWJmZjhjY2EyZGIyMzRiNDlhZjkiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjc5MDI3MjkyLCJleHAiOjE2NzkwMzQ0OTIsImF6cCI6IjdLeDlqeXVuTnlLWWt4YUE3MlBVZ1pmZ0FRSmN6U0doIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.Iz9Yn6FNCfPKvkLFHr9b1I8lxdMUkNsr2zxmsuHv5b08Ygy4SISzd3tn0bUZAq0G2XnaYheVQIGPHNypr7nczxTqTTsCtnYXqXbRXD1h8uQrn5If3lHlk4tIxtZHkF-OeSmD8o645tp2IIIyt92nV9B7kDDFlzd0PKJ0ReL6JEeNk3wYKVtOCwFWoj3lEXIYHAz4NaB5hVqg-kdKTeB230O7Mj89SfttrDj1ECgTRxayaGZopI8S0BiwXONetVakBjq6LoRhQcVhjTmTpUspyiBhEKNdOqPjx59XGZmO20bVhhXkt2nCmz5GWLb7yHx7uliEonlyT8RoTMOwFydPAg`

- Casting Director - `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InM2ak83SUtoNEU4cC1rMDI4SUVfNiJ9.eyJpc3MiOiJodHRwczovL2Rldi14bXFseWZ3bTZ5a3Uxa2hkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDEzZTllZDczOTk3NmI3NDcwZDM0ZGYiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjc5MDI2NzQ1LCJleHAiOjE2NzkwMzM5NDUsImF6cCI6IjdLeDlqeXVuTnlLWWt4YUE3MlBVZ1pmZ0FRSmN6U0doIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.VTJNHYyXmHj99pgf5I85c-ZY_LYbK9LpWFQ_udaCzy03BfyDZJXjoHpdTMta4YnVsZTLDy0zsIlE9sNLq8Z7vdUyXgeHM9FCkhZk6OTb5IUw4Ts3hnQ_HIwKosAwMrJ_ddmdEsPkYwTHQM2IoTNtcNznnz136OYJidd-K-jI_WRgbVRvEI2JP5txqqdIe204ZHuUbSfl11FmipN1yxzc5P8lKWOBDto1gjNN9N46ddGPCd240wi7D_l4b1WHoDl67mtQIyFylfvw-rjtjd9Fow3gDeTndTi_mRdyYCv2l2k691HW1qsAkMp_u7PHubpmTNf1vXAmUsOstc_FkejcdA`

- Executive Producer - `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InM2ak83SUtoNEU4cC1rMDI4SUVfNiJ9.eyJpc3MiOiJodHRwczovL2Rldi14bXFseWZ3bTZ5a3Uxa2hkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDEzZTg5NmE0NzY3MTc5N2EzZTAzZTgiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjc5MDI2NDQ2LCJleHAiOjE2NzkwMzM2NDYsImF6cCI6IjdLeDlqeXVuTnlLWWt4YUE3MlBVZ1pmZ0FRSmN6U0doIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.D6L2Sae3fvL7fJtlS29dZ_lm-MxNjbDRswntQ5ZuOqm_WgsPpzCNBgPB93j3pngmmaxK68gU4CGRlM0WkjQVzKJcNK3rd3RSe7PZzXaE9O_N_G9UZTcxrLXL_aFn3iXcCiyo97HkrhLlORLn_GrUeJ1nxsWpKF1K-0XfpCH1nScaEhdGTmkkeWcytjpefynwQx-LhUb6VSCCFNR165YfV8_raoLpOSa85YFNZzIbK-8rRuzsLY2haBBlJErJdbhNnRGU2OE9mdZtMzNT0Fd6ITg7U1bv0L-sIJGDIamJ0NIHuGOA_nupPmwB763O2Eh-z2dl3rmxR6t91WjJHAJ8Fg`

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
            "name": "Keanu Reeves"
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
