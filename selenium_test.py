"""
このモジュールはSeleniumを使用してWebページのテストを実行します。
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#  Chromeのオプションを設定
chrome_options = Options()
chrome_options.add_argument("--headless")  # ヘッドレスモード

# ソースコードと同じディレクトリにあるchromedriverのパスを取得
current_dir = os.path.dirname(os.path.abspath(__file__))
chrome_driver_path = os.path.join(current_dir, "chromedriver")
service = Service(executable_path=chrome_driver_path)  # 変更: serviceを定義
driver = webdriver.Chrome(service=service, options=chrome_options)

# テスト対象のWebページにアクセス
driver.get("https://den2k6.github.io/actions_aws_deploy/")

# ページのタイトルを取得
title = driver.title
h1_text = driver.find_element(By.TAG_NAME, "h1").text

# タイトルが期待通りかチェック
assert (
    title == "AWS deploy test using Actions"
), f"タイトルが一致しません。取得されたタイトル: {title}"

print(f"page title: {title}")
print(f"h1 text:    {h1_text}")

time.sleep(1)

# WebDriverを終了
driver.quit()
