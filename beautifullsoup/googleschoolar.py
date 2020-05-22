from bs4 import BeautifulSoup
from pip._vendor import requests
import csv

pages = []
# Pagination Url 
for i in range(1, 6):
    if i == 1:
        index = 0
    else:
        index = i * 10
    url = 'https://scholar.google.com/scholar?start='+ str(index) +'&q=AODV&hl=en&as_sdt=0,5'
    pages.append(url)

# Mendefisinikan file
f = csv.writer(open('google-schoolar.csv', 'w'))
f.writerow(['Judul', 'Link'])

for item in pages:
    # Request
    result = requests.get(item)

    # Untuk melihat website up
    #print(result.status_code)

    # Untuk melihat HTTP Header
    #print(result.headers)

    # Menyimpan konten ke variabel
    src = result.content

    # Memparsing data yang telah disimpan
    soup = BeautifulSoup(src, 'lxml')

    #  Setelah halam diproses, kemudian kita dapat mengakses informasinya
    # links = soup.find_all("a")
    # print(links)
    # print("\n")

    # Link Condition
    # for link in links:
    #     if "AODV" in link.text:
    #         # print(link)
    #         print(link.text)

    # titles = []
    # urls = []
    for div_items in soup.findAll("div", {"class": "gs_r gs_or gs_scl"}):
        h3_tag = div_items.find('h3')
        a_tag = h3_tag.find('a')

        # Data yang akan disimpan
        # Jika hasil tidak ada link dan hanya sitasi saja
        if a_tag:
            judul = a_tag.text
            link = a_tag.attrs['href']
        else:
            judul = h3_tag.text
            link = ""
        # Menambahkan ke array
        # titles.append(judul)
        # urls.append(a_tag.attrs['href'])

        # Menginputkan ke CSV
        f.writerow([judul, link])

    # print(titles)
    # print(urls)