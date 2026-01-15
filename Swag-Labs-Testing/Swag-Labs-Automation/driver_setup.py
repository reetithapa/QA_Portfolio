from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    service = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.headless = False
    options.add_argument("start-maximized")

    driver = webdriver.Chrome(service=service, options=options)
    return driver

