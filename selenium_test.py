"""
このモジュールはSeleniumを使用してWebページのテストを実行します。
"""

import os
import time
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


TARGET_URL = "https://den2k6.github.io/actions_aws_deploy/"
EXPECTED_H1 = "Deploy to AWS S3 by GitHub Actions"


def selenium_test(url, expected_h1):
    """テストの実行"""

    #  Selenium の設定
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # ヘッドレスモード

    if os.name == "posix" and platform.system() != "Darwin":
        service = Service("/usr/bin/chromedriver")
    elif platform.system() == "Darwin":
        service = Service("/usr/local/bin/chromedriver")
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        chrome_driver_path = os.path.join(current_dir, "chromedriver.exe")
        service = Service(executable_path=chrome_driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    # テスト開始
    driver.get(url)
    title = driver.title
    h1_text = driver.find_element(By.TAG_NAME, "h1").text

    assert (
        h1_text == expected_h1
    ), f"Title does not match. Expected: {expected_h1}, Actual: {h1_text}"

    print(f"page title: {title}")
    print(f"h1 text:    {h1_text}")

    time.sleep(0)
    driver.quit()


if __name__ == "__main__":
    selenium_test(TARGET_URL, EXPECTED_H1)
