from bs4 import BeautifulSoup
import requests

content = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(content.text, "html.parser")
# print(soup.p)
# all_titles=soup.find_all("h3")
# for title in all_titles:
#     all_link=title.findAll("a")
#     for link in all_link:
#         print(link.string)
price = soup.find_all("p", class_="price_color")
#print(price)
#print((" ".join(price)).string)
