import os
import shutil
'''Sepearates the images from JSON files after downloading'''

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
download_dir = os.path.join(base_dir, "images", "00000")

img_dir = os.path.join(base_dir, 'data', 'images')
json_dir = os.path.join(base_dir, 'data', 'json')

if not os.path.isdir(img_dir):
    os.mkdir(img_dir)
if not os.path.isdir(json_dir):
    os.mkdir(json_dir)

for filename in os.listdir(download_dir):
    name, ext = os.path.splitext(filename)
    file_dir = os.path.join(download_dir, filename)

    if ext.lower() == '.json':
        shutil.copy(file_dir, os.path.join(base_dir, "data", "json"))
    else:
        shutil.copy(file_dir, os.path.join(base_dir, "data", "images"))
