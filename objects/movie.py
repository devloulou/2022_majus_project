import os
import json
from uuid import uuid4

from helpers.movie_db import get_movie_data
from helpers.mongo_helper import MongoHelper
from helpers.file_helper import download_image

home_folder = os.path.join(os.path.expanduser("~"), 'movie_meta_images')

print(home_folder)

class Movie:
    client = None
    poster_api = "https://image.tmdb.org/t/p/w300/"
    backdrop_api = "https://image.tmdb.org/t/p/w500/"

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

        if not os.path.exists(home_folder):
            os.makedirs(home_folder)

        if not movie_data:
            self.refresh_movie_data()
            # adatbázisból ki kellene szedni az adatot, ha ott van, ha nincs ott, le kell tölteni
        else:
            self.load(movie_data)
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

                self.download_poster(movie_data)
                # ide kell egy insert
                self.save()

        else:
            for k, v in movie_db_data.items():
                setattr(self, k, v)

    def download_poster(self, movie_data):      
        poster_path = None
        backdrop_path = None
        poster_url = None
        backdrop_url = None

        if movie_data.get('poster_path'):
            poster_url = self.poster_api + movie_data['poster_path']

        if movie_data.get('backdrop_path'):
            backdrop_url = self.backdrop_api + movie_data['backdrop_path']

        image_id = str(uuid4())

        poster_path = os.path.join(home_folder, image_id + '.jpg')
        backdrop_path = os.path.join(home_folder, image_id + '_backdrop.jpg')

        if poster_url:
            self.poster = download_image(poster_url, poster_path)

        if backdrop_url:
            self.backdrop = download_image(backdrop_url, backdrop_path)

    def save(self):
        if self.client:
            self._id = self.client.insert_doc(self.__dict__)

    def load(self, movie_data):
        for k, v in movie_data.items():
            setattr(self, k, v)

if __name__ == '__main__':
    movie_path = r"C:\WORK\2022_majus_project\2022_majus_project\test_movies\Prey.mkv"
    client = MongoHelper()
    test = Movie(client=client, movie_path=movie_path)

    print(test.__dict__)
    #test.refresh_movie_data()