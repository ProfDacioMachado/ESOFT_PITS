from selenium import webdriver
from selenium.webdriver.common.by import By

print("Iniciando teste Swag Labs")

def test_eight_components():
    print("Executando teste")
    driver = setup()

    driver.implicitly_wait(0.5)

    input_username = driver.find_element(by=By.ID, value="user-name")
    input_password = driver.find_element(by=By.ID, value="password")

    submit_button = driver.find_element(by=By.ID, value="login-button")

    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    submit_button.click()

    message = driver.find_element(by=By.CLASS_NAME, value="app_logo")
    value = message.text
    assert value == "Swag Labs"

    teardown(driver)

def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    return driver

def teardown(driver):
    driver.quit()

test_eight_components()
