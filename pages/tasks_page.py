from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time

class TasksPage(BasePage):
    FIRST_EDIT_BUTTON = (By.XPATH, "//table//tbody//tr[1]//button[contains(@class,'btn-outline-primary')]")
    STATUS_DROPDOWN = (By.XPATH, "//label[text()='Status']/following::select[1]")
    SAVE_BUTTON = (By.XPATH, "//button[contains(.,'Save')]")
    STATUS_BADGE = (By.XPATH, "//table//tbody//tr[1]//span[contains(@class,'badge')]")
    MODAL = (By.XPATH, "//div[contains(@class,'modal') and contains(@class,'show')]")

    def click_first_edit(self):
        # Wait for table to be fully loaded first
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_EDIT_BUTTON)
        )
        self.click(self.FIRST_EDIT_BUTTON)
        self.wait.until(
            EC.visibility_of_element_located(self.STATUS_DROPDOWN)
        )

    def change_status(self, status):
        # Wait for dropdown to be clickable before selecting
        self.wait.until(
            EC.element_to_be_clickable(self.STATUS_DROPDOWN)
        )
        dropdown = Select(self.find(self.STATUS_DROPDOWN))
        dropdown.select_by_value(status)

    def save_task(self):
        # Wait for save button to be clickable
        save_btn = self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        )
        # Scroll into view and click
        self.driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
        time.sleep(0.5)
        save_btn.click()

        # Wait for modal to fully disappear
        self.wait.until(
            EC.invisibility_of_element_located(self.MODAL)
        )
        # Small buffer for table to refresh
        time.sleep(1)

    def get_status(self):
        # Always re-find the badge to avoid stale element
        badge = self.wait.until(
            EC.presence_of_element_located(self.STATUS_BADGE)
        )
        return badge.text
