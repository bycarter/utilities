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
    a = (By.CSS_SELECTOR, "#packages_tabstrip > ul > li.k-item.k-state-default.k-first")  # define locator to feed into WDW
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(a))
    driver.find_element(by=By.CSS_SELECTOR, value="#packages_tabstrip > ul > li.k-item.k-state-default.k-first").click()

    b = (By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[4]/div[1]/button")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(b))
    driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[4]/div[1]/button").click()

    c = (By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[4]/div[1]/ul/li[2]")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(c))
    driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[4]/div[1]/ul/li[2]").click()

    // wait until loaded
    //download file
    # element = (By.CSS_SELECTOR, "footer_push")
    # wait = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located(element))
    # login_button.click()
    #
    # element = (By.CSS_SELECTOR, ".btn-inverse > small")
    # wait = WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located(element))
    # switch = driver.find_element(by=By.CSS_SELECTOR, value=".btn-inverse > small")
    # switch.click()
    #
    # reclic = driver.find_element(by=By.CSS_SELECTOR, value="li:nth-child(2) div > small")
    # reclic.click()
    # driver.implicitly_wait(5.0)
    # active = driver.find_element(by=By.CSS_SELECTOR, value="#packages_tabstrip_ts_active > .k-link")
    # active.click()
    # driver.implicitly_wait(5.0)
    # exp1 = driver.find_element(by=By.CSS_SELECTOR, value="#packages_tabstrip_ts_active > .k-link")
    # exp1.click()
    # exp2 = driver.find_element(by=By.CSS_SELECTOR, value=".btn-group:nth-child(4) > .btn-group:nth-child(1) > .btn")
    # exp2.click()
    # driver.implicitly_wait(5.0)
    #
    # today = 'dc-' + str(date.today())
    # ActionChains(driver).send_keys(today)
    # ActionChains(driver).send_keys(Keys.RETURN)

    # search_box = driver.find_element(by=By.NAME, value="q")
    # value = search_box.get_attribute("value")
    # assert value == "Selenium"

    # driver.quit()


# def wait_all(driver, css_selector):


if __name__ == "__main__":
    main()
