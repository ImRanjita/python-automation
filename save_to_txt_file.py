from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from datetime import datetime
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
    driver.get("http://automated.pythonanywhere.com/login/")

    return driver


def clean_text(text):
    """extract only the value from the text"""
    output = float(text.split(": ")[1])
    return output



def main():


    driver = get_driver()
    ""driver.find_element(by="id",value ="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id",value ="id_password").send_keys("automatedautomated" + Keys.RETURN)
    print(driver.current_url)
    time.sleep(2)
    driver.find_element(by="xpath", value = "/html/body/nav/div/a").click()
    print(driver.current_url)
    element = driver.find_element(by="xpath", value="//*[@id='displaytimer']")
    print(element)
    cleaned_line =  clean_text(element)
   # save_output_to_file()


def save_output_to_file() :
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Create file name with date-time
    file_name = f"web_output_{timestamp}.txt"

    # Save to text file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(cleaned_line)

    print(f"Saved: {file_name}")
    return


print(main())

