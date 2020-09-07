from os import makedirs, path
from urllib import request
from bs4 import BeautifulSoup
import wget

target_dir = './dataset/'

makedirs(target_dir, exist_ok=True)

base_url = 'https://vision.cs.uiuc.edu/pascal-sentences/'
page = request.urlopen(base_url)
soup = BeautifulSoup(page, features="html5lib")

all_images = soup.body.findAll('img')

for image in all_images:
    suffix = image.get('src')
    link = base_url + suffix
    dir_name, img_name = path.split(suffix)

    dir_path = path.join(target_dir, dir_name)
    makedirs(dir_path, exist_ok=True)

    filepath = path.join(dir_path, img_name)
    print('Downloading %s ...' % link)
    wget.download(link, filepath)
