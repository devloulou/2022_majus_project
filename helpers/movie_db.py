import tmdbsimple as tmdb

tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

search = tmdb.Search()
movies = tmdb.Movies()

def get_movie_data(title):
    search.movie(query=title)
    return search.results

def get_popular_movies():
    top_rated = movies.top_rated()['results']
    popular = movies.popular()['results']

    return [*top_rated, *popular]

if __name__ == '__main__':
    from pprint import pprint
    data = get_movie_data('Prey')
    
    popular = get_popular_movies()
    pprint(data[0], indent=4)