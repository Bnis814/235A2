from datetime import datetime


class Actor:
    def __init__(self, name: str):
        if name == "" or type(name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = name.strip()
        self.__workedWith = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return "<Actor {}>".format(self.__actor_full_name)

    def __eq__(self, other):
        return self.__actor_full_name == other.actor_full_name

    def __lt__(self, other):
        if (self.__actor_full_name is None and other.actor_full_name is None) or other.actor_full_name  is None:
            return False
        if self.__actor_full_name is None:
            return True
        return self.__actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if colleague not in self.__workedWith:
            self.__workedWith.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.__workedWith


class Director:
    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return "<Director {}>".format(self.director_full_name)

    def __eq__(self, other):
        return self.__director_full_name == other.director_full_name

    def __lt__(self, other):
        if (self.__director_full_name is None and other.director_full_name is None) or other.director_full_name  is None:
            return False
        if self.__director_full_name is None:
            return True
        return self.__director_full_name < other.director_full_name

    def __hash__(self):
        return hash(self.__director_full_name)

class Genre:
    def __init__(self, name: str):
        if name == "" or type(name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return "<Genre {}>".format(self.__genre_name)

    def __eq__(self, other):
        return self.__genre_name == other.genre_name

    def __lt__(self, other):
        if (self.__genre_name is None and other.genre_name is None) or other.genre_name is None:
            return False
        if self.__genre_name is None:
            return True
        return self.__genre_name < other.genre_name

    def __hash__(self):
        return hash(self.__genre_name)




class Movie:
    def __init__(self, name: str, year: int):
        if name == "" or type(name) is not str:
            self.__name = None
        else:
            self.__name = name.strip()

        if year >= 1900:
            self.__year = year
        else:
            self.__year = None

        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None

    @property
    def title(self):
        return self.__name

    @title.setter
    def title(self, title):
        if not (title == "" or type(title) is not str):
            self.__name = title.strip()

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year >= 1900:
            self.__name = year

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not (description == "" or type(description) is not str):
            self.__description = description.strip()

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, direc):
        if isinstance(direc, Director):
            self.__director = direc

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, lst):
        self.__actors = lst

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, lst):
        self.__genres = lst

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, time):
        if time > 0 and isinstance(time, int):
            self.__runtime_minutes = time
        else:
            raise ValueError

    def __repr__(self):
        return "<Movie {}, {}>".format(self.__name, self.__year)

    def __eq__(self, other):
        return self.__name == other.title and self.__year == other.year

    def __lt__(self, other):
        if self.__name is None or other.title is None or self.__name == other.title:
            if self.__name is None:
                if not other.title is None:
                    return True
                else:
                    if (self.__year is None and other.year is None) or other.year is None:
                        return False
                    if self.__year is None:
                        return True
                    return self.__year < other.year

            elif other.title is None:
                return False

            elif self.__name == other.title:
                if (self.__year is None and other.year is None) or other.year is None:
                    return False
                if self.__year is None:
                    return True
                return self.__year < other.year

        return self.__name < other.title

    def __hash__(self):
        return hash((self.__name, self.__year))

    def add_actor(self, actor):
        if isinstance(actor, Actor):
            self.__actors.append(actor)
        else:
            raise ValueError

    def remove_actor(self, actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre):
        if isinstance(genre, Genre):
            self.__genres.append(genre)
        else:
            raise ValueError

    def remove_genre(self, genre):
        if genre in self.__genres:
            self.__genres.remove(genre)



class Review:
    def __init__(self, movie, review_text, rating):
        if type(movie) is not Movie:
            self.__review_text = None
        else:
            self.__movie = movie

        if review_text == "" or type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text.strip()

        if isinstance(rating, int) and 1 <= rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None

        self.__timestamp = datetime.now().timestamp()


    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, movie):
        if type(movie) is Movie:
            self.__movie = movie

    @property
    def review_text(self):
        return self.__review_text

    @review_text.setter
    def review_text(self, review_text):
        if not(review_text == "" or type(review_text) is not str):
            self.__review_text = review_text.strip()

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 10:
            self.__rating = rating

    @property
    def timestamp(self):
        return self.__timestamp


    def __repr__(self):
        return "<Review {}, {}>".format(self.__movie, self.__timestamp)

    def __eq__(self, other):
        return self.__movie == other.movie and self.__review_text == other.review_text and self.__rating == other.rating and self.__timestamp == other.timestamp

class User:
    def __init__(self, user_name, password):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()

        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password.strip()

        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def actors(self, user_name):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()

    @property
    def password(self):
        return self.__password

    @password.setter
    def actors(self, password):
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password.strip()

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    def __repr__(self):
        return "<User {}>".format(self.__user_name)

    def __eq__(self, other):
        if self.__user_name is None and other.user_name is None:
            return True
        if self.__user_name is None or other.user_name is None:
            return False

        return self.__user_name == other.user_name

    def __lt__(self, other):
        if (self.__user_name is None and other.user_name is None) or other.user_name is None:
            return False
        if self.__user_name is None:
            return True
        return self.__user_name < other.user_name

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie):
        if isinstance(movie, Movie) and movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
            if movie.runtime_minutes is not None:
                self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if isinstance(review, Review) and review not in self.__reviews:
            self.__reviews.append(review)

