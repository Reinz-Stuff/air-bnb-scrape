import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


# buka link
driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=ID&continue=https%3A%2F%2Fwww.google'
           '.com%2Fsearch%3Fq%3Dhow%2Bto%2Bupdate%2Bvenv%2Bpackage%26oq%3Dhow%2Bto%2Bupdate%2Bvenv%2Bpackage%26aqs'
           '%3Dchrome..69i57.12409j0j1%26sourceid%3Dchrome%26ie%3DUTF-8&dsh=S34503346%3A1670585397139649&flowEntry'
           '=SignUp&flowName=GlifWebSignIn&hl=id&ifkv=AeAAQh7n7rkg4SRqfm9lhNFkKUxK3RwYKIiiOEpdP0nrH-eWcLzTACGqUc'
           '-kv89N5-DpSY04xXolbQ')

# target username dan password
firstname = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name=\"firstName\"]')))
lastname = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name=\"lastName\"]')))
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name=\"Username\"]')))

# masukkan username dan password
firstname.clear()
firstname.send_keys('fauzi')
lastname.clear()
lastname.send_keys('kurniawan')
username.clear()
username.send_keys('fauzikurniawan1')

time.sleep(5)