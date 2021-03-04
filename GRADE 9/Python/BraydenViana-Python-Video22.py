import random 
import urllib.request

def download_web_image(url):
	name = random.randrange(1, 1000)
	full_name = str(name) + ".jpg"
	urllib.request.urlretrieve(url, full_name)

download_web_image("https://buckysroom.org/photos/users/2/resized/2463u86fdf42a16B1c66ba8fd67B9f9d.jpg")