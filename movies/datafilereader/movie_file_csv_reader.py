import csv

from movies.domain.model import Movie
from movies.domain.model import Actor
from movies.domain.model import Genre
from movies.domain.model import Director


class MovieFileCSVReader:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.dataset_of_movies = []
        self.dataset_of_actors = []
        self.dataset_of_directors = []
        self.dataset_of_genres = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                description = row['Description']
                self.dataset_of_movies.append(Movie(title, release_year))
                self.dataset_of_movies[-1].description = description

                lstactors = row['Actors'].split(',')
                for ele in lstactors:
                    if not Actor(ele) in self.dataset_of_actors:
                        self.dataset_of_actors.append(Actor(ele))

                self.dataset_of_movies[-1].actors = lstactors

                lstgenres = row['Genre'].split(',')
                for ele in lstgenres:
                    if not Genre(ele) in self.dataset_of_genres:
                        self.dataset_of_genres.append(Genre(ele))

                self.dataset_of_movies[-1].genres = lstgenres

                if not Director(row['Director']) in self.dataset_of_directors:
                    self.dataset_of_directors.append(Director(row['Director']))

                self.dataset_of_movies[-1].director = Director(row['Director'])

                index += 1


