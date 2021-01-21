from PIL import Image
import requests
import os
import imghdr
import shutil


os.mkdir('cats_and_dogs/dataset')
os.mkdir('cats_and_dogs/dataset/tmp')
os.mkdir('cats_and_dogs/dataset/test')
os.mkdir('cats_and_dogs/dataset/test/cat')
os.mkdir('cats_and_dogs/dataset/test/dog')
os.mkdir('cats_and_dogs/dataset/val')
os.mkdir('cats_and_dogs/dataset/val/cat')
os.mkdir('cats_and_dogs/dataset/val/dog')
os.mkdir('cats_and_dogs/dataset/train')
os.mkdir('cats_and_dogs/dataset/train/cat')
os.mkdir('cats_and_dogs/dataset/train/dog')


print('Downloading cat dataset...')
cat_urls = open('cats_and_dogs/cat_urls.txt', 'r')
cat_ctr = 0
for i, cat_url in enumerate(cat_urls):

    if cat_ctr >= 500:
        print("Done.")
        break

    try:
        cat_response = requests.get(cat_url, timeout=1)
    except:
        continue

    image_name = f'cats_and_dogs/dataset/tmp/cat_{i}.jpg'

    with open(image_name, 'wb') as f:
        f.write(cat_response.content)

    if imghdr.what(image_name) is None:
        os.remove(image_name)
        continue

    else:
        if cat_ctr >= 100:
            shutil.move(image_name, f'cats_and_dogs/dataset/train/cat/cat_{cat_ctr}.jpg')

        elif i >= 50:
            shutil.move(image_name, f'cats_and_dogs/dataset/val/cat/cat_{cat_ctr}.jpg')

        else:
            shutil.move(image_name, f'cats_and_dogs/dataset/test/cat/cat_{cat_ctr}.jpg')
        
        cat_ctr += 1  

if cat_ctr < 500:
    print(f"ERROR: There are only {cat_ctr} valid cat images. Please find more cat URLS. This script wont work properly otherwise.")

cat_urls.close()


print('Downloading dog dataset...')
dog_urls = open('cats_and_dogs/dog_urls.txt', 'r')
dog_ctr = 0
for i, dog_url in enumerate(dog_urls):

    if dog_ctr >= 500:
        print("Done.")
        break

    try:
        dog_response = requests.get(dog_url, timeout=0.5)
    except:
        continue
    image_name = f'cats_and_dogs/dataset/tmp/dog_{i}.jpg'
    with open(image_name, 'wb') as f:
        f.write(dog_response.content)

    if imghdr.what(image_name) is None:
        os.remove(image_name)
        continue

    else:
        if dog_ctr >= 100:
            shutil.move(image_name, f'cats_and_dogs/dataset/train/dog/dog_{dog_ctr}.jpg')

        elif i >= 50:
            shutil.move(image_name, f'cats_and_dogs/dataset/val/dog/dog_{dog_ctr}.jpg')

        else:
            shutil.move(image_name, f'cats_and_dogs/dataset/test/dog/dog_{dog_ctr}.jpg')
        
        dog_ctr += 1  

if dog_ctr < 500:
    print(f"ERROR: There are only {dog_ctr} valid dog images. Please find more dog URLS. This script wont work properly otherwise.")

dog_urls.close()

os.rmdir("cats_and_dogs/dataset/tmp")
