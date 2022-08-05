# small program for work to scrape csvs for work
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    test()


def test():
    """use selenium to scrape csv"""
    driver = webdriver.Chrome()  # start a session
    driver.get('https://google.com')

    title = driver.title
    assert title == "Google"

    driver.implicitly_wait(0.5)

    search_box = driver.find_element(by=By.NAME, value="q")
    search_button = driver.find_element(by=By.NAME, value="btnK")

    search_box.send_keys("Selenium")
    search_button.click()

    search_box = driver.find_element(by=By.NAME, value="q")
    value = search_box.get_attribute("value")
    assert value == "Selenium"

    driver.quit()


if __name__ == "__main__":
    main()

