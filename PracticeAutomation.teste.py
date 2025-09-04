from selenium import webdriver
from selenium.webdriver.common.by import By

print("Iniciando teste Swag Labs")

def test_eight_components():
    print("Executando teste")
    driver = setup()

    driver.implicitly_wait(0.5)

    input_username = driver.find_element(by=By.NAME, value="username")
    input_password = driver.find_element(by=By.NAME, value="password")

    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")

    input_username.send_keys("student")
    input_password.send_keys("Password123!")
    submit_button.click()

    message = driver.find_element(by=By.CSS_SELECTOR, value="title")
    value = message.text
    assert value == "Logged In Successfully"


    teardown(driver)

def setup():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    return driver

def teardown(driver):
    driver.quit()

test_eight_components()
