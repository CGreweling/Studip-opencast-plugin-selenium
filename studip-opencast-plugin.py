from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


BASE_URL = 'http://YOURSTUDIP'
driver = webdriver.Chrome('./webdriver-chrome/chromedriver')
user = 'root@studip'
password = 'PASSWORD'

def navigate(driver, path):
    driver.get(f'{BASE_URL}{path}')


def wait_for(driver, element):
    WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(element))


def login():
    navigate(driver, '/studip/index.php?again=yes')
    assert 'Stud.IP' in driver.title
    elem = driver.find_element(By.ID, 'loginname')
    elem.clear()
    elem.send_keys(user)
    elem = driver.find_element(By.ID, 'password')
    elem.clear()
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    wait_for(driver, (By.ID, 'header_avatar_menu'))


def openOpencastPlugin():
    navigate(driver, '/studip/plugins.php/opencast/course/index?cid=a07535cf2f8a72df33c12ddfa4b53dde')
    assert 'Vorlesung: Test Lehrveranstaltung - Opencast Player - Vorlesungsaufzeichnungen - Stud.IP' in driver.title


def mediaUpload():
    elem = driver.find_element(By.LINK_TEXT, 'Medien hochladen')
    elem.click()
    wait_for(driver, (By.ID, 'course-upload'))
    assert driver.find_element(By.ID, 'course-upload')


def main():
    login()
    openOpencastPlugin()
    mediaUpload()

    driver.close()


if __name__ == '__main__':
    main()
