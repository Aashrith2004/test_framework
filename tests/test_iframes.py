from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.logger import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger()


def test_frames_tabs_windows(driver):

    logger.info("TC08 started")

    login_page = LoginPage(driver)
    login_page.login_as_admin("admin@example.com", "Admin@123")

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(., 'Dashboard')]"))
    )

    dashboard = DashboardPage(driver)

    logger.info("Opening Test Scenarios page")
    dashboard.go_to_test_scenarios()

    main_window = driver.current_window_handle

    # -------- IFRAME --------
    logger.info("Switching to iframe")

    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "test-iframe"))
    )
    driver.switch_to.frame(iframe)

    assert driver.title is not None

    driver.switch_to.default_content()

    # -------- NEW TAB --------
    logger.info("Opening new tab")

    driver.find_element(By.ID, "btn-new-tab").click()

    WebDriverWait(driver, 10).until(
        lambda d: len(d.window_handles) > 1
    )

    for window in driver.window_handles:
        if window != main_window:
            driver.switch_to.window(window)
            break

    assert driver.current_url is not None

    driver.close()
    driver.switch_to.window(main_window)

    # -------- POPUP WINDOW --------
    logger.info("Opening popup window")

    driver.find_element(By.ID, "btn-popup-window").click()

    WebDriverWait(driver, 10).until(
        lambda d: len(d.window_handles) > 1
    )

    for window in driver.window_handles:
        if window != main_window:
            driver.switch_to.window(window)
            break

    assert driver.current_url is not None

    driver.close()
    driver.switch_to.window(main_window)

    logger.info("TC08 passed")