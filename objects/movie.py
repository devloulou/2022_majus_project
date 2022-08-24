import os
import json

from helpers.movie_db import get_movie_data
from helpers.mongo_helper import MongoHelper
from helpers.file_helper import download_image

home_folder = os.path.join(os.path.expanduser("~"), 'movie_meta_images')

class Movie:
    client = None

    def __init__(self, client: MongoHelper, movie_path=None, movie_data=None):
        self.path = movie_path
        Movie.client = client

        self.poster = None
        self.backdrop = None
        self.title = None
        self.description = None
        self.rating = 0
        self.release_date = None
        self.trailer = None
        self.favorite = None
        self.watched = None
        self.original_language = None

        if not movie_data:
            self.refresh_movie_data()
            # adatbázisból ki kellene szedni az adatot, ha ott van, ha nincs ott, le kell tölteni
        else:
            pass
            # az objectnél be kell állítani az adatokat

    def refresh_movie_data(self):        
        movie_name = os.path.basename(self.path).split('.')[0]
        
        movie_db_data = self.client.find_by_path(self.path)

        if not movie_db_data:
            movie_data_list = get_movie_data(movie_name)

            if movie_data_list:
                movie_data = movie_data_list[0]

                self.title = movie_data['original_title']
                self.description = movie_data['overview']
                self.release_date = movie_data['release_date']
                self.original_language = movie_data['original_language']
                self.rating = movie_data['vote_average']




if __name__ == '__main__':
    movie_path = r"C:\WORK\2022_majus_project\2022_majus_project\test_movies\Prey.mkv"
    client = MongoHelper()
    test = Movie(client=client, movie_path=movie_path)

    print(test.description)

    #test.refresh_movie_data()