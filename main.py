from selenium import webdriver
from selenium.webdriver.firefox.options import Options

profile_path = r'/usr/local/bin/geckodriver'
options = Options()
options.set_preference('profile', profile_path)
driver = webdriver.Firefox(options=options)

driver.get("http://www.google.com")
ok3=driver.find_element_by_name('btnI')
driver.execute_script("arguments[0].click();",ok3)