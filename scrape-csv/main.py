# small program to scrape csv, edit,
from configparser import ConfigParser
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os


def main():

    # pull config data
    config_obj = ConfigParser()
    config_obj.read("config.ini")

    # scrape_csv()
    file_df = verify_and_open_csv(config_obj)
    mod_data_to_csv(file_df, config_obj)


def mod_data_to_csv(dataframe, config_object):
    dataframe["Business"] = 33
    dataframe["Discontinued"] = ''
    n_df = dataframe.replace(",", ";", regex=True)
    # print(n_df.to_markdown())
    file_out = 'dc-' + str(date.today()) + '.csv'
    path_out = config_object["OS"]["downloads"] + '/'
    combo_out = path_out + file_out

    n_df.to_csv(combo_out)


def verify_and_open_csv(config_o):
    """confirm download exists and open in pd"""
    os.chdir(config_o["OS"]["downloads"])
    files = os.listdir()
    target_file_name = config_o["OS"]["fileName"]

    for file in files:
        file_found = False  # flag for logging, -WIP-
        if file == target_file_name:
            print(file, 'found')
            file_found = True

    # create dataframe and
    path = os.getcwd() + '/' + target_file_name
    file_df = pd.read_excel(path, index_col=0)

    return file_df


def scrape_csv():
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

    # wait, then load active button
    a = (By.XPATH, config_obj["SELECT"]["val1"])
    WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(a))
    driver.find_element(by=By.XPATH, value=config_obj["SELECT"]["val1"]).click()

    # wait, then click toggle button
    b = (By.XPATH, config_obj["SELECT"]["val2"])
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(b))
    driver.find_element(by=By.XPATH, value=config_obj["SELECT"]["val2"]).click()

    # wait, then click
    c = (By.XPATH, config_obj["SELECT"]["val3"])
    WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located(c))
    driver.find_element(by=By.XPATH, value=config_obj["SELECT"]["val3"]).click()

    # wait until alert is present
    #WebDriverWait(driver, 20).until(EC.alert_is_present());

    # enter keys
    today = 'dc-' + str(date.today())
    time.sleep(3)
    ActionChains(driver).send_keys(today)
    ActionChains(driver).send_keys(Keys.RETURN)

    driver.quit()


if __name__ == "__main__":
    main()
