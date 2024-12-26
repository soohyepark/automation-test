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

# # 디바이스 및 앱 정보 설정
# options = UiAutomator2Options()
# options.platformName = "Android"
# options.deviceName = "AOS14"  # 에뮬레이터 또는 실제 장치의 이름
# options.app = "/Users/soohyepark/apk/GmarketMobile-debugFinal-20241202_160338.apk"  # 앱의 APK 파일 경로
# options.appPackage = "http://com.ebay.kr.gmarket"  # 앱 패키지 이름
# options.appActivity = "http://com.ebay.kr.gmarket.eBayKoreaGmarketActivity"  # 시작 액티비티 이름
#
# # Appium 서버와 연결
# driver = webdriver.Remote('http://localhost:4723', options=options)

# # 요소 클릭
# element = driver.find_element(By.ID, 'com.ebay.kr.gmarket:id/appPermissionBtn')
# element.click()
# # 알림 처리 allow?
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'com.android.permissioncontroller:id/permission_allow_button')))
# element.click()
# # 알림 처리 don't allow
# # element = driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button')
# # element.click()
# # 하단 팝업 닫기
# element = driver.find_element(By.ID, 'com.ebay.kr.gmarket:id/iv_plus')
# element.click()
# # 검색 버튼 클릭
# time.sleep(2)
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'com.ebay.kr.gmarket:id/btn_search')))
# element.click()
# print("검색버튼 누르기 실패")

# # 테스트 종료
# driver.quit()