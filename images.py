from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

search = input("Search for: ")
params = {"q": search}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get("http://bing.com/search", params=params, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "thumb"})

for item in links:
    img_obj = requests.get(item.attrs["href"])
    print(f'Getting {item.attrs["href"]}')
    title = item.attrs["href"].split("/")[-1]
    img = Image.open(BytesIO(img_obj.content))
    img.save("./scraped images/" + title, img.format)
