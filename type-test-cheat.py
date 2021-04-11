import time
import undetected_chromedriver as uc
uc.install()

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Very simple but just a bit of fun.
# Benchmarking how well a bot does on this typing test.
driver = Chrome()
driver.get('https://10fastfingers.com/advanced-typing-test/english')

while(True):
    text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.highlight"))).get_attribute("innerText")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#inputfield.form-control"))).send_keys(text+" ")