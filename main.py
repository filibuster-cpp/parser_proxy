from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pandas

profile_path = r'/usr/local/bin/geckodriver'
options = Options()
options.set_preference('profile', profile_path)
driver = webdriver.Firefox(options=options)

driver.get('https://hidemy.name/ru/proxy-list/?type=5#list')
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
data = str(soup.findAll('td'))
data = data.replace("<td>", "")
data = data.replace(" ", "")
data = data.replace(",", "")
spl_data = data.split("</td>")
proxy_ip_address = []
proxy_port = []
for string in spl_data:
    if string.count('.') == 3:
        proxy_ip_address.append(string)
    elif string.isdigit():
        proxy_port.append(string)
df = pandas.DataFrame({'IP': proxy_ip_address, 'Port': proxy_port})
print(df)
df.to_csv('ip-port.csv', index=False, header=False)
