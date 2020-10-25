import os
import random as rand
import math

from flask import Flask
from flask import request, render_template, redirect, url_for, session

from movies.domain.model import Actor, Movie, Director, Genre, User
from movies.datafilereader.movie_file_csv_reader import MovieFileCSVReader


def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    filename = 'movies/adapters/data/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()


    @app.route('/')
    def index():
        if(request.args.get('index') == None):
            indexf=0
        else:
            indexf = int(request.args.get('index'))
        return render_template(
            'movies.html', my_list=movie_file_reader.dataset_of_movies[indexf:indexf+3], index=indexf, disp="cont"
        )

    @app.route('/random')
    def random():
        randint = rand.randint(0, int(math.floor((len(movie_file_reader.dataset_of_movies)-1)/3))) * 3
        return render_template(
            'movies.html', my_list=movie_file_reader.dataset_of_movies[randint:randint+3], index=randint, disp="cont"
        )

    @app.route('/list')
    def lists():
        return render_template(
            'movies.html', my_list=movie_file_reader.dataset_of_movies, index=0, disp="list"
        )

    return app
