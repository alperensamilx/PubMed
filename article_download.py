from lxml import html
import requests

pmc_id = input('PMC ID: ')

page = requests.get(f'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pmc_id}/')
webpage = html.fromstring(page.content)

x = webpage.xpath('//*[@id="rightcolumn"]/div[2]/div/ul/li[4]/a/@href')
url = f'https://www.ncbi.nlm.nih.gov{x[0]}'
r = requests.get(url, stream=True)


filename = url.split('/')[-1]
with open(filename, 'wb') as pdf:
    pdf.write(r.content)
