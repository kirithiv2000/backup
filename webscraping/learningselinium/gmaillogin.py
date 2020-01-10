from selenium import webdriver
from webdriver_manager.chrome  import ChromeDriverManager
from getpass import getpass
import time

usergmail=input()# to take the gmail of user

password=getpass()#getpass for hidding  the password

driver=webdriver.Chrome(ChromeDriverManager().install())#initialize chrome
driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(usergmail)# To enter the gmail id
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()# To click Next button
time.sleep(2)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)# To enter the password
driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()# To click login button


