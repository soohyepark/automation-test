import time

from config.appium_config import get_driver
from config.google_sheet import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search():
    """
    검색 기능 테스트
    """
    driver = get_driver()

    # 검색 테스트 로직 (예시)
    try:
        # 얼럿 닫기
        element = driver.find_element(By.ID, 'com.ebay.kr.gmarket:id/appPermissionBtn')
        element.click()
        # 알림 처리 allow 클릭
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'com.android.permissioncontroller:id/permission_allow_button')))
        element.click()
        # 하단 팝업 닫기
        runtext = '하단 팝업 닫기'
        print("#", runtext, "시작")
        id = 'com.ebay.kr.gmarket:id/ivClose'
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
        element.click()
        print("#", runtext, "종료")

        # 검색 페이지 진입
        runtext = '검색 페이지 진입'
        id = 'com.ebay.kr.gmarket:id/tvSearchBar'
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, id)))
        element.click()
        print("#", runtext, "종료")

        # element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//android.widget.EditText[@resource-id="com.ebay.kr.gmarket:id/searchEditText"]'))
        # )
        # element = driver.find_element(By.XPATH, "//android.widget.EditText")
        # 지마켓메인 검색창 텍스트 입력
        runtext = '메인 페이지 > 검색창 텍스트 입력'
        print("#", runtext, "시작")
        id = "com.ebay.kr.gmarket:id/searchEditText"
        goods_name = "test"
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, id)))
        element.send_keys(goods_name)
        print("#", runtext, "종료")

        # 지마켓메인 검색창 리턴
        runtext = '메인 페이지 > 검색창 텍스트 리턴'
        print("#", runtext, "시작")
        xpath = '//android.widget.ImageView[@content-desc="입력된 단어로 검색"]'
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
        print("#", runtext, "종료")

        # 입력 및 검색된 텍스트 비교
        runtext = '메인 페이지 > 검색창 텍스트 리턴 > 입력 및 검색된 텍스트 비교'
        print("#", runtext, "시작")
        id = "com.ebay.kr.gmarket:id/searchKeyword"
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
        value = element.text
        assert value in goods_name, f"'{value}' not found in '{goods_name}'"
        print("#", runtext, "종료")

        test_name = "Search Test"
        status = "PASS"
        remarks = "검색 성공"

    except Exception as e:
        test_name = "Search Test"
        status = "FAIL"
        remarks = f"검색 실패: {str(e)}"

    finally:
        # 구글 시트에 결과 기록
        json_file_path = "/Users/soohyepark/soohye-automation-test-98b439d0a39e.json"
        spreadsheet_url = "https://docs.google.com/spreadsheets/d/1FwTUfJCZB0IMdwToylHih5w8ej2lG_NzsNfJhyUbkA0/edit?gid=0#gid=0"
        worksheet_name = "시트1"

        worksheet = connect_google_sheet(json_file_path, spreadsheet_url, worksheet_name)
        log_result(worksheet, test_name, status, remarks)

test_search()