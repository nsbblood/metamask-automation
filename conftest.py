import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile
import os

@pytest.fixture
def driver():
    options = Options()
    
    # Headless mod (CI/CD için)
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Her run için benzersiz kullanıcı klasörü
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    
    # Tarayıcı sessiz ve problemsiz başlasın
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()