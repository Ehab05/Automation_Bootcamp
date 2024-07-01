from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_google_search():
    driver = webdriver.Chrome()
    try:
        driver.get("http://www.google.com/")
        driver.implicitly_wait(10)
        search_field = driver.find_element(By.NAME, "q")
        search_field.send_keys("Python programming", Keys.ENTER)
        search_result = driver.find_element(By.CSS_SELECTOR, "h3.LC20lb.MBeuO.DKV0Md")
        assert "Python For Beginners" in search_result.text
        print(f"Yay the test has passed we found : {search_result.text}")

    except Exception as e:
        print(f"we didn't find it sorry:{e}")

    driver.quit()
