import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def download_message_image(url, photo_name):
    photo_name = f'{photo_name}.jpg'
    r = urllib.request.urlopen(url)
    with open(f"{photo_name}", "wb") as f:
        f.write(r.read())
    return photo_name


def add_water_mark(input_image_path, output_image_path, text, pos):
    photo = Image.open(input_image_path)
    drawing = ImageDraw.Draw(photo)
    black = (3, 8, 12)
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save('output_image_path')


def aa():
    photo = Image.open('image_cloud/photo_name (2).png')
    watermark = Image.open('image_cloud/watermark.png')
    photo.paste(watermark, (25, 25), watermark)
    photo.save('output_image_path')


if __name__ == '__main__':
    aa()