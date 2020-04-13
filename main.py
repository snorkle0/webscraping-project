from bs4 import BeautifulSoup
import requests

search = input("Enter search term: ")
url = 'https://bing.com/search'
params = {'q': search}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get(url, params=params, headers=headers)


soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
