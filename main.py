import json
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


def pars_texno(category):
    texno_data = []
    load_dotenv()

    URL = os.getenv('URL')
    HOST = os.getenv('HOST')
    HEADERS = {
    'USER-AGENT' : "Mozilla"
    }


    html = requests.get(URL + category,headers=HEADERS).text
    soup = BeautifulSoup(html,"html.parser")

    blocks = soup.find_all('div', class_="col-3")

    for block in blocks:
        images_link = block.find('a', class_="product-link")
        images = images_link.find('img').get('data-src')
        title = block.find('h2').get_text()
        credit_price = block.find('div', class_='installment-price').get_text(strip=True)
        price = block.find('div',class_='product-price__current').get_text(strip=True)

        texno_data.append({
            'image':images,
            'title': title,
            'credit_price': credit_price,
            ' price':  price,
        })

        print(texno_data)

        with open('phone.json', mode='w',encoding='utf-8') as file:
            json.dump(texno_data,file,indent=4)
pars_texno('katalog/smartfony-apple/')