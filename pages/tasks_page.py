from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class TasksPage(BasePage):
    # More specific - finds Edit button in first row
    FIRST_EDIT_BUTTON = (By.XPATH, "//table//tbody//tr[1]//button[contains(.,'Edit')]")
    STATUS_DROPDOWN   = (By.XPATH, "//label[text()='Status']/following::select[1]")
    # More specific - finds Save button inside modal only
    SAVE_BUTTON       = (By.XPATH, "//div[contains(@class,'modal-footer')]//button[contains(.,'Save')]")
    STATUS_BADGE      = (By.XPATH, "//table//tbody//tr[1]//span[contains(@class,'badge')]")
    # Wait for STATUS_DROPDOWN to disappear after save
    MODAL_BACKDROP    = (By.XPATH, "//div[contains(@class,'modal-backdrop')]")

    def click_first_edit(self):
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_EDIT_BUTTON)
        )
        self.click(self.FIRST_EDIT_BUTTON)
        self.wait.until(
            EC.visibility_of_element_located(self.STATUS_DROPDOWN)
        )

    def change_status(self, status):
        self.wait.until(
            EC.element_to_be_clickable(self.STATUS_DROPDOWN)
        )
        dropdown = Select(self.find(self.STATUS_DROPDOWN))
        dropdown.select_by_value(status)

    def save_task(self):
        save_btn = self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
        save_btn.click()
        # Wait for backdrop to disappear = modal fully closed
        self.wait.until(
            EC.invisibility_of_element_located(self.MODAL_BACKDROP)
        )
        time.sleep(1)

    def get_status(self):
        badge = self.wait.until(
            EC.presence_of_element_located(self.STATUS_BADGE)
        )
        return badge.text
