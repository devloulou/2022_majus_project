import os
import requests

def get_files(folder_path):
    return [os.path.join(folder_path, item) for item in os.listdir(folder_path)\
         if item.endswith('.mkv')]

"""
image letöltés webről: ha ismered a kép elérési útvonalát:

filekiírást csinálok -> kiírási mód: wb
"""

def download_image(url, img_location):
    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(img_location, 'wb') as f:
            f.write(r.content)
        return True
    return False

if __name__ == '__main__':
    folder_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_movies')

    movies = get_files(folder_path)

    download_image('https://image.tmdb.org/t/p/w300/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg', folder_path + '/test_image.jpg')
