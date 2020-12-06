from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup
import requests
import sys

# create a new chrome session
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=options, executable_path="/home/ubuntu/mypgm/LOLAPIServer/Modules/chromedriver")

driver.implicitly_wait(3)
driver.maximize_window()

url = 'https://www.op.gg/summoner/userName=' + sys.argv[1]
action = ActionChains(driver)
driver.get(url)

try:
    driver.find_element_by_css_selector('.Button.SemiRound.Blue').click()
    action.send_keys(Keys.ENTER)
    time.sleep(1)
    #driver.get_screenshot_as_file('opgg.png')
except Exception as ex:
    print("exception: ", ex)
    driver.quit()
driver.quit()
#driver.close()
