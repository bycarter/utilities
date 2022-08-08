# small program for work to scrape csvs for work
from configparser import ConfigParser
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def main():
    test()


def test():
    """Use selenium to scrape csv.  All private info pulled in from config.ini"""

    # initialize session with Brave
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # pull config data
    config_obj = ConfigParser()
    config_obj.read("config.ini")

    # open site
    driver.get(config_obj["SITE"]["login"])
    title = driver.title
    assert title == config_obj["TITLE"]["login"]

    # fill in user and pass
    driver.find_element(by=By.NAME, value="Username").send_keys(config_obj["USERINFO"]["loginId"])
    driver.find_element(by=By.NAME, value="Password").send_keys(config_obj["USERINFO"]["password"])

    # click button and check title
    driver.find_element(by=By.ID, value="login_button").click()
    title = driver.title
    assert title == config_obj["TITLE"]["loggedIn"]

    # navigate to next page
    driver.get(config_obj["SITE"]["second"])
    title = driver.title
    assert title == config_obj["TITLE"]["second"]

    # wait, then load
    a = (By.CSS_SELECTOR, config_obj["SELECT"]["val1"])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(a))
    driver.find_element(by=By.CSS_SELECTOR, value=config_obj["SELECT"]["val1"]).click()

    b = (By.XPATH, config_obj["SELECT"]["val2"])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(b))
    driver.find_element(by=By.XPATH, value=config_obj["SELECT"]["val2"]).click()

    c = (By.XPATH, config_obj["SELECT"]["val3"])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(c))
    driver.find_element(by=By.XPATH, value=config_obj["SELECT"]["val3"]).click()

    # wait until blob loads
    # enter keys and download

    # today = 'dc-' + str(date.today())
    # ActionChains(driver).send_keys(today)
    # ActionChains(driver).send_keys(Keys.RETURN)

    # driver.quit()


# def wait_all(driver, css_selector):


if __name__ == "__main__":
    main()
