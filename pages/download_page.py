import time
from selenium.webdriver.common.by import By

class DownloadPage:
    def __init__(self, driver):
        self.driver = driver
        self.download_button_locator = (
            By.CLASS_NAME, "hero-download_hero-links__Ch5xq"
        )

    def go_to_download_page(self):
        self.driver.get("https://metamask.io/download")
        time.sleep(2)  # wait for page load

    def click_download_button(self):
        button = self.driver.find_element(*self.download_button_locator)
        time.sleep(2)
        button.click()