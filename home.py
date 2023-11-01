from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://weka.inf.ufes.br/IFESTP/index.php")

login = driver.find_element(By.ID, "username")
login.clear()
login.send_keys("Botafogo")
login.send_keys(Keys.RETURN) #se eu tirar sozinho não muda nada, mas se eu tirar os dois não loga

email = driver.find_element(By.ID, "email")
email.clear()
email.send_keys("botafogo1904@campeao.com")
email.send_keys(Keys.RETURN) #se eu tirar sozinho não muda nada, mas se eu tirar os dois não loga

password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys("botafogo1904")
password.send_keys(Keys.RETURN) 

password_2 = driver.find_element(By.ID, "passwordConfirm")
password_2.clear()
password_2.send_keys("botafogo1904")
password_2.send_keys(Keys.RETURN) 

button = driver.find_element(By.NAME, "submit")
button.send_keys(Keys.RETURN) #se eu tirar não loga 

login = driver.find_element_by_xpath('//a[text()="Login"]')
login.click()

assert "No results found." not in driver.page_source
driver.close()