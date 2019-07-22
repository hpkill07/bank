from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
executable_path = "./chromedriver.exe"
browser = webdriver.Chrome(executable_path=executable_path)
browser.get("https://online.kasikornbankgroup.com/K-Online/")
username_field = browser.find_element_by_name("userName")
password_field = browser.find_element_by_name("password")
username_field.send_keys("populapor07")
password_field.send_keys("por19030703")
password_field.send_keys(Keys.RETURN)
browser.get('https://ebank.kasikornbankgroup.com/retail/cashmanagement/inquiry/AccountSummary.do?action=list_domain2')
soup = BeautifulSoup(browser.page_source, 'html.parser')
browser.quit()
div = soup.find_all('td',{'class':'inner_table_center'})
print(div)
