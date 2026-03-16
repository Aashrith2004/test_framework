from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.logger import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger()


def test_alerts_handling(driver):

    logger.info("TC07 started")

    login_page = LoginPage(driver)
    login_page.login_as_admin("admin@example.com", "Admin@123")

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(., 'Dashboard')]"))
    )

    dashboard = DashboardPage(driver)

    logger.info("Opening Test Scenarios page")
    dashboard.go_to_test_scenarios()

    # ---------- Simple Alert ----------
    logger.info("Triggering simple alert")
    driver.find_element(By.ID, "btn-simple-alert").click()
    alert = driver.switch_to.alert
    alert.accept()

    # ---------- Confirm Dialog ----------
    logger.info("Triggering confirm dialog")
    driver.find_element(By.ID, "btn-confirm").click()
    confirm = driver.switch_to.alert
    confirm.dismiss()

    # ---------- Prompt Dialog ----------
    logger.info("Triggering prompt dialog")
    driver.find_element(By.ID, "btn-prompt").click()
    prompt = driver.switch_to.alert
    prompt.send_keys("Automation Test")
    prompt.accept()

    prompt_result = driver.find_element(By.ID, "prompt-result").text
    assert "Automation Test" in prompt_result

    logger.info("TC07 passed")