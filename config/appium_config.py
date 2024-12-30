from appium import webdriver
import time
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    options = UiAutomator2Options()
    options.platformName = "Android"
    options.deviceName = "AOS14"  # 에뮬레이터 또는 실제 장치의 이름
    options.app = "/Users/soohyepark/apk/GmarketMobile.apk"  # 앱의 APK 파일 경로
    options.appPackage = "http://com.ebay.kr.gmarket"  # 앱 패키지 이름
    options.appActivity = "http://com.ebay.kr.gmarket.eBayKoreaGmarketActivity"  # 시작 액티비티 이름

    driver = webdriver.Remote("http://localhost:4723", options=options)
    return driver
