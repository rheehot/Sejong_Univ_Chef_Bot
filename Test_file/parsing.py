from bs4 import BeautifulSoup
import urllib.request
import json
n_price=[]
n_menu=[]


html = urllib.request.urlopen("http://m.sejong.ac.kr/front/cafeteria.do")
text = html.read().decode("utf8")

soup = BeautifulSoup(text, 'html.parser')

menu = soup.find_all('div',{'class':'th'})
price = soup.find_all('div',{'class':'td price'})


for n in price:
        n_price.append(n.get_text())

for n in menu:
        n_menu.append(n.get_text())

for n in range(0,len(menu)):
    print(n_menu[n]+" "+n_price[n])