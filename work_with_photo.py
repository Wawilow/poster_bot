import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from data_base import last_image_in_cloud, new_directory


def download_message_image(url, photo_name, user_id='test_id'):
    photo_name = f'{photo_name}.png'
    r = urllib.request.urlopen(url)
    new_directory('C:/Users/Admin/Desktop/проекты/meme_posting/image_cloud', user_id)
    with open(f"image_cloud/{user_id}/{photo_name}", "wb") as f:
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
    download_message_image('https://sun9-59.userapi.com/impg/qrcMuHpWQfvxYhd3oYjkDxlCZHL5Zo_Uwl5HJw/-czMnWTP7ZE.jpg?size=510x382&quality=96&sign=520dc3a6d1b2161c80670704a684b2b6&c_uniq_tag=LgoVyxMvHb683wvGQK5q-9wN34n9JAhFDmU00QdWphg&type=album',
                           f'{last_image_in_cloud(delta=1)}',
                           user_id='1')