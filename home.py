from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.ChromiumEdge()
driver.get("http://weka.inf.ufes.br/IFESTP/index.php")

#Cadastro e Login na plataforma, caso seja necessário.
'''
username = driver.find_element(By.ID, "username")
username.clear()
username.send_keys("EduardoOPato")
username.send_keys(Keys.RETURN) #se eu tirar sozinho não muda nada, mas se eu todos não loga

email = driver.find_element(By.ID, "email")
email.clear()
email.send_keys("eduardoopato@campeao.com")
email.send_keys(Keys.RETURN) 

password = driver.find_element(By.NAME, "password")
password.clear()
password.send_keys("eduopato0123")

password_2 = driver.find_element(By.NAME, "passwordConfirm")
password_2.clear()
password_2.send_keys("eduopato0123")

button = driver.find_element(By.NAME, "submit")
button.send_keys(Keys.RETURN) #se eu tirar não loga 

time.sleep(5)

login = driver.find_element(By.TAG_NAME, "a")
login.click()

username_login = driver.find_element(By.ID, "username")
username_login.clear()
username_login.send_keys("EduardoOPato")
username_login.send_keys(Keys.RETURN) 

password_login = driver.find_element(By.ID, "password")
password_login.clear()
password_login.send_keys("eduopato0123")
password_login.send_keys(Keys.RETURN) 

time.sleep(3)
'''

assert "No results found." not in driver.page_source
driver.close()