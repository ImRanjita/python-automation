from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
service = Service('C:\\Users\\Karthik\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-link-features = AutomationControlled")
    driver = webdriver.Chrome(service=service ,options=options)
    driver.get("http://automated.pythonanywhere.com")

    return driver

def main():


    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath",value ="/html/body/div[1]/div/h1[2]")
    return element.text

print(main())

