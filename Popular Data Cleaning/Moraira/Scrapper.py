from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd

columns = ["Title", "Price", "Habitaciones", "Baños", "m2", "m2_parcela"]
df = pd.DataFrame(columns=columns)

for f in range(1,4):
    url="http://www.morairabuild.com/page/"+str(f)+"/?s&reference&post_type=properties"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    divs = soup.find_all(class_="item column column-block")
    listado=[]
    
    for div in divs:
        title=div.find("a")
        price=div.find("div", class_="price").text.replace("\n", "").replace("\t","").replace(",",".")[1:]
        bed=div.find("div", class_="column column-block bed").text.replace("\n", "").replace("\t","")
        bath=div.find_all("div", class_="column column-block bath")

        # print(title.attrs["title"], price, bed.text)
        listado.append(title.attrs["title"])
        listado.append(price)
        listado.append(bed)
        for i in bath:
            listado.append(i.text.replace("\n", "").replace("\t",""))
        df=df.append(pd.DataFrame([listado], columns=columns))
        listado=[]
        
df.to_csv("Moraria.csv", header=columns, index=False, sep=";")
        


# with open("housing.csv", "w", encoding="utf8", newline="") as f:
#     thewriter = writer(f)
# soup = BeautifulSoup(page.content, "html.parser")
# lists = soup.find_all("div", class_="item column column-block")

# h_price =[]

# for list in lists:
#     price =list.find("div", class_="price").text.replace("\n", "").replace("\t","")

#     h_price.append(price)


# titles = soup.find_all("div", {"class:", "inner", "attrs"})

# h_titles=[]
# for title in titles:
#     title=list.find("div", class_=["inner"]["h3"])
# h_titles.append(title)
# print(h_titles)




"""for list in lists:
    title = list.find("a", attrs="title")
    price =list.find("div", class_="price").text.replace("\n", "").replace("\t","")
    bed =list.find("text", class_="Plot Size")
    information = [title, price, bed]
    
print(information)"""
