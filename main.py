import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from auth_data import a_password, a_login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle


def test_auth():
    options = Options()
    options.set_preference(
        'general.useragent.override',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0)Gecko/20100101 Firefox/93.0'
    )
    options.set_preference('dom.webdriver.enabled', False)
    service = Service(r'C:\Py3on\selenium_1\geckodriver.exe')
    browser = webdriver.Firefox(
        options=options,
        service=service
    )
    try:
        browser.get('https://www.i.ua/')
        browser.implicitly_wait(5)
        login = browser.find_element(By.NAME, 'login')
        login.clear()
        login.send_keys(a_login)
        browser.implicitly_wait(5)
        password = browser.find_element(By.NAME, 'pass')
        password.clear()
        password.send_keys(a_password + Keys.ENTER)
        browser.implicitly_wait(5)
        pickle.dump(browser.get_cookies(), open('cookies', 'wb'))
    except Exception as e:
        print(e)
    finally:
        browser.close()
        browser.quit()
    return None


def test_load_cook():
    options = Options()
    options.set_preference(
        'general.useragent.override',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0)Gecko/20100101 Firefox/93.0'
    )
    service = Service(r'C:\Py3on\selenium_1\geckodriver.exe')
    browser = webdriver.Firefox(
        options=options,
        service=service
    )
    try:
        browser.get('https://www.i.ua/')
        browser.implicitly_wait(5)
        for cookie in pickle.load(open('cookies', 'rb')):
            browser.add_cookie(cookie)
        browser.implicitly_wait(5)
        browser.refresh()
        browser.implicitly_wait(5)
    except Exception as e:
        print(e)
    finally:
        browser.close()
        browser.quit()
    return None


def scrap_olx():
    options = Options()
    options.set_preference(
        'general.useragent.override',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0)Gecko/20100101 Firefox/93.0'
    )
    service = Service(r'C:\Py3on\selenium_1\geckodriver.exe')
    browser = webdriver.Firefox(
        options=options,
        service=service
    )
    try:
        browser.get('https://www.olx.ua/')
        browser.find_element(By.XPATH, './/div[@id="cookiesBar"]/button').click()
        wait = WebDriverWait(browser, 10)
        browser.implicitly_wait(5)
        search = browser.find_element(By.ID, 'headerSearch')
        search.send_keys('nvidia' + Keys.ENTER)
        #browser.implicitly_wait(5)
        time.sleep(5)
        wait.until(EC.invisibility_of_element_located((By.XPATH, ".//p[@class ='offer-path color-9 lheight16 margintop5']/small")))
        items = browser.find_elements(By.XPATH, ".//h3[@class='lheight22 margintop5']/a")
        items[1].click()
        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        browser.close()
        browser.quit()
    return None


def main():
    scrap_olx()


if __name__ == '__main__':
    main()
