from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
import time
import os

# Use ChromeDriverManager to download and install the correct version of ChromeDriver
service = ChromeService(ChromeDriverManager().install())

def initialize_driver():
    try:
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10)  # Set an implicit wait to handle dynamic elements
        return driver
    except Exception as e:
        print(f"Failed to initialize WebDriver: {e}")
        return None

def login_to_facebook(driver, email, password):
    try:
        driver.get('https://www.facebook.com')
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'pass'))
        )
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'login'))
        )

        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()
        print("Login attempted.")
    except TimeoutException:
        print("Login elements did not appear in time.")
    except NoSuchWindowException:
        print("No such window: Target window already closed.")

def test_home_page_load():
    driver = initialize_driver()
    if driver is None:
        return
    try:
        # Use environment variables for sensitive information
        email = os.getenv('FACEBOOK_EMAIL')
        password = os.getenv('FACEBOOK_PASSWORD')
        login_to_facebook(driver, email, password)
        time.sleep(5)  # Wait for 5 seconds to allow the page to load fully
        actual_title = driver.title
        print(f"Actual Title: {actual_title}")
        assert "Facebook" in actual_title, "Home page did not load correctly."
        print("Test Passed: Home page loaded correctly.")
    except AssertionError as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

def test_login_button_presence():
    driver = initialize_driver()
    if driver is None:
        return
    try:
        driver.get('https://www.facebook.com')
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'login'))
        )
        assert login_button.is_displayed(), "Login button is not displayed."
        print("Test Passed: Login button is displayed.")
    except TimeoutException:
        print("Test Failed: Login button did not appear in time.")
    except AssertionError as e:
        print(f"Test Failed: {e}")
    except NoSuchWindowException:
        print("No such window: Target window already closed.")
    finally:
        driver.quit()

def test_create_account_button_presence():
    driver = initialize_driver()
    if driver is None:
        return
    try:
        driver.get('https://www.facebook.com')
        create_account_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-testid='open-registration-form-button']"))
        )
        assert create_account_button.is_displayed(), "Create New Account button is not displayed."
        print("Test Passed: Create New Account button is displayed.")
    except TimeoutException:
        print("Test Failed: Create New Account button did not appear in time.")
    except AssertionError as e:
        print(f"Test Failed: {e}")
    except NoSuchWindowException:
        print("No such window: Target window already closed.")
    finally:
        driver.quit()

def test_scrolling_down():
    driver = initialize_driver()
    if driver is None:
        return
    try:
        driver.get('https://www.facebook.com')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Test Passed: Scrolling down the page.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

def test_scrolling_up():
    driver = initialize_driver()
    if driver is None:
        return
    try:
        driver.get('https://www.facebook.com')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for 2 seconds to allow scrolling down
        driver.execute_script("window.scrollTo(0, 0);")
        print("Test Passed: Scrolling up the page.")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

# Run the test cases
test_home_page_load()
test_login_button_presence()
test_create_account_button_presence()
test_scrolling_down()
test_scrolling_up()
