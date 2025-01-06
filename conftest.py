import time

import pytest
from appium.options.android import UiAutomator2Options
import platform
import os
from appium import webdriver

@pytest.fixture(scope="module")
def driver():
    # 디바이스 및 앱 정보 설정
    os_version = platform.platform()
    if 'Windows' in os_version:  # windows인 경우
        options = UiAutomator2Options()
        app_path = os.path.abspath("C:/APK/GmarketMobile.apk")
        options.PlatformName = "Android"
        options.deviceName = "AOS14"  # 에뮬레이터 또는 실제 장치의 이름
        options.app = app_path  # 앱의 APK 파일 경로
        options.appPackage = "com.ebay.kr.gmarket"  # 앱 패키지 이름
        options.appActivity = "com.ebay.kr.gmarket.eBayKoreaGmarketActivity"  # 시작 액티비티 이름
        options.adbExecTimeout = 60000

    elif 'mac' in os_version:
        options = UiAutomator2Options()
        app_path = os.path.abspath("/Users/soohyepark/apk/GmarketMobile.apk")
        options.platformName = "Android"
        options.deviceName = "AOS14"  # 에뮬레이터 또는 실제 장치의 이름
        options.app = app_path  # 앱의 APK 파일 경로
        options.appPackage = "com.ebay.kr.gmarket"  # 앱 패키지 이름
        options.appActivity = "com.ebay.kr.gmarket.eBayKoreaGmarketActivity"  # 시작 액티비티 이름
        options.adbExecTimeout = 60000

    # Appium 서버와 연결
    driver = None
    try:
        driver = webdriver.Remote("http://localhost:4723", options=options)
        print("Driver initialized successfully!")
    except Exception as e:
        print(f"Driver initialization failed: {e}")
        raise

    # return driver
    yield driver
    # 테스트 종료 후 Appium 서버와 연결 종료
    driver.quit()