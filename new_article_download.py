from lxml import html
import requests
from bs4 import BeautifulSoup

pm_id = input('PM ID: ')

page = requests.get(f'https://pubmed.ncbi.nlm.nih.gov/{pm_id}/')
webpage = html.fromstring(page.content)

x = webpage.xpath('//*[@id="full-view-identifiers"]/li[3]/span/a/@href')
url = x[0]
print(url)
r = requests.get(url, stream=True)


# filename = url.split('/')[-1]
# with open('python_new6.pdf', 'wb') as pdf:
#     pdf.write(r.content)
