from config.appium_config import get_driver
from config.google_sheet import connect_google_sheet, log_result
from selenium.webdriver.common.by import By

def test_login():
    """
    로그인 기능 테스트
    """
    driver = get_driver()

    # 로그인 테스트 로직 (예시)
    try:
        # 로그인 페이지 진입
        element = driver.find_element(By.ID, 'com.ebay.kr.gmarket:id/tvSubTitle')
        element.click()

        username_field = driver.find_element_by_id("username")
        password_field = driver.find_element_by_id("password")
        login_button = driver.find_element_by_id("login_button")

        username_field.send_keys("pooh302730")
        password_field.send_keys("1q2w3e4R")
        login_button.click()

        # 로그인 성공 확인 (예시)
        success_message = driver.find_element_by_id("login_success")
        assert success_message.is_displayed(), "로그인 실패"

        test_name = "Login Test"
        status = "PASS"
        remarks = "로그인 성공"

    except Exception as e:
        test_name = "Login Test"
        status = "FAIL"
        remarks = f"로그인 실패: {str(e)}"

    finally:
        # 구글 시트에 결과 기록
        json_file_path = "/Users/soohyepark/soohye-automation-test-98b439d0a39e.json"
        spreadsheet_url = "https://docs.google.com/spreadsheets/d/1FwTUfJCZB0IMdwToylHih5w8ej2lG_NzsNfJhyUbkA0/edit?gid=0#gid=0"
        worksheet_name = "시트1"

        worksheet = connect_google_sheet(json_file_path, spreadsheet_url, worksheet_name)
        log_result(worksheet, test_name, status, remarks)

        driver.quit()
