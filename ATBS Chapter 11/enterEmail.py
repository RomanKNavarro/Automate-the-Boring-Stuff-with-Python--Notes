from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get('https://gmail.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('ronnoverro@gmail.com')
nextButtonElem = browser.find_element_by_id('identifierNext')
nextButtonElem.click()
time.sleep(2)
passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys('ocegueda22')
passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys('ocegueda22')
passwordElem.sudmit()

