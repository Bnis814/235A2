from movies.datafilereader.movie_file_csv_reader import MovieFileCSVReader


def main():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    print(movie_file_reader.dataset_of_movies)
    print(movie_file_reader.dataset_of_actors)
    print(movie_file_reader.dataset_of_directors)
    print(movie_file_reader.dataset_of_genres)



if __name__ == "__main__":
    main()