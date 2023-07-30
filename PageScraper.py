from bs4 import BeautifulSoup
import requests



page = requests.get("https://www.doordash.com/en-AU/convenience/store/liquorland-brighton-24127484/")

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
[type(item) for item in list(soup.children)]
html = list(soup.children)[2]
list(html.children)



print(page.status_code)
