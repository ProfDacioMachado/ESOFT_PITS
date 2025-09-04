from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Iniciando teste Swag Labs")

def test_eight_components():
    print("Executando teste")
    driver = setup()

    driver.implicitly_wait(0.5)

    input_username = driver.find_element(by=By.NAME, value="username")
    input_password = driver.find_element(by=By.NAME, value="password")

    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")

    input_username.send_keys("Admin")
    input_password.send_keys("admin123")
    submit_button.click()

    # Wait for the footer to appear
    message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "oxd-layout-footer"))
    )
    value = message.text
    assert "OrangeHRM OS 5.7" in value


    teardown(driver)

def setup():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    return driver

def teardown(driver):
    driver.quit()

test_eight_components()
