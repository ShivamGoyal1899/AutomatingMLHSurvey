from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from getpass import getpass
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
    
for i in range(0, 100):
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=chrome_options)
    driver.get('https://mlh.az1.qualtrics.com/jfe/form/SV_3kIVGinpkQAETsN')
    time.sleep(2)

    driver.find_element_by_id('NextButton').click()
    time.sleep(2)

    driver.find_element_by_id('QID4-1-label').click()
    time.sleep(1)

    driver.find_element_by_id('NextButton').click()
    time.sleep(2)

    driver.find_element_by_id('QR~QID1').send_keys('singh'+i+'@airadio.co')
    time.sleep(1)

    driver.find_element_by_id('QR~QID5').send_keys('helloindia'+i+'.com')
    time.sleep(2)

    driver.find_element_by_id('QID6-4-label').click()
    time.sleep(1)

    driver.find_element_by_id('NextButton').click()
    time.sleep(5)

    print('YaY! Promo Code number {} has been mailed.'.format(i))
    driver.close()