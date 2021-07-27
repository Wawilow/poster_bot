import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


def download_message_image(url, photo_name):
    photo_name = f'{photo_name}.jpg'
    r = urllib.request.urlopen(url)
    with open(f"{photo_name}", "wb") as f:
        f.write(r.read())
    return photo_name


def add_water_mark():
    pass


if __name__ == '__main__':
    pass