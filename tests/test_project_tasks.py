from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.project_page import ProjectsPage
from utils.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
logger = get_logger()


def test_project_creation_flow(driver):

    logger.info("TC05 started")

    login_page = LoginPage(driver)
    login_page.login_as_admin("admin@example.com", "Admin@123")

    WebDriverWait(driver, 10).until(
        EC.url_contains("dashboard")
    )

    dashboard = DashboardPage(driver)
    dashboard.go_to_projects_page()

    projects_page = ProjectsPage(driver)

    project_name = f"Automation Test Project {int(time.time())}"
    

    logger.info("Creating new project")

    projects_page.click_new_project()
    projects_page.enter_title(project_name)
    projects_page.enter_description("Created via Selenium")
    projects_page.select_status("active")
    projects_page.click_save()

    WebDriverWait(driver, 10).until(
        lambda d: projects_page.is_project_visible(project_name)
    )

    assert projects_page.is_project_visible(project_name)

    logger.info("TC05 passed")
