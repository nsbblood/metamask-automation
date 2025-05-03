import time
from pages.download_page import DownloadPage

def test_download_metamask_extension(driver):
    """
    Test Case: Download MetaMask Extension from Official Website

    Steps:
    1. Open https://metamask.io/download
    2. Click the active download button
    3. Wait for 10 seconds to simulate the download
    4. Print success message

    Expected Result:
    - Button is clicked successfully
    - Simulated download finishes without errors
    """
    page = DownloadPage(driver)
    page.go_to_download_page()
    page.click_download_button()
    time.sleep(10)
    print("✅ Download process simulated successfully!")