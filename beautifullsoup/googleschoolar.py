from bs4 import BeautifulSoup
from pip._vendor import requests
import csv

# Url tujuan
result = requests.get("https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=AODV&btnG=&oq=")

# Mendefisinikan file
f = csv.writer(open('google-schoolar.csv', 'w'))
f.writerow(['Judul', 'Link'])


# Untuk melihat website up
#print(result.status_code)

# Untuk melihat HTTP Header
#print(result.headers)

# Mentimpan konten ke variabel
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

titles = []
urls = []
for div_items in soup.findAll("div", {"class": "gs_r gs_or gs_scl"}):
    h3_tag = div_items.find('h3')
    a_tag = h3_tag.find('a')

    # Data yang akan disimpan
    judul = a_tag.text
    link = a_tag.attrs['href']

    # Menambahkan ke array
    titles.append(judul)
    urls.append(a_tag.attrs['href'])

    # Menginputkan ke CSV
    f.writerow([judul, link])

# print(titles)
# print(urls)