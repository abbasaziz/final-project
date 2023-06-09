import os
from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.app_context().push() 
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    migrate = Migrate(app,db)
    db.init_app(app)


def create_tables():
    db.create_all()
    
class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    release_year = Column(Integer())
    actors = db.relationship('Actor', backref='movies')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year
        }





class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    gender = Column(String())

    movie_id = db.Column(
        db.Integer,
        db.ForeignKey('movies.id'),
        nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movie_id': self.movie_id
        }


