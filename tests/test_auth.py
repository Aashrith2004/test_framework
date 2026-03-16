from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login_as_admin("admin@example.com", "Admin@123")

    wait = WebDriverWait(driver, 20)

    dash_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(., 'Dashboard')]"))
    )

    assert dash_element.is_displayed()
    logger.info("TC01 passed")