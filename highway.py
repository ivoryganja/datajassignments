import requests, mechanize
from bs4 import BeautifulSoup
 
url = 'https://www.mshp.dps.missouri.gov/HP71/SearchAction?searchDate=10/31/2017'

br = mechanize.Browser()
 br.open(url)
<response_seek_wrapper at 0x10b999758 whose wrapped object = <closeable_response at 0x10b9995f0 whose fp = <socket._fileobject object at 0x10b790ad0>>>
 html = br.response().read()

soup=BeautifulSoup(html, "html.parser")
 
main_table = soup.find('table', 
	{'class':'accidentOutput'}
	)

row_list = main_table.find_all('tr')
for r in row_list:
    cell_list = r.find_all('td')
     if len(cell_list) > 0:
         for c in cell_list:
             print c.text.strip()
        print '---------'
