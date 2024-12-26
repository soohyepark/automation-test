from config.google_sheet import connect_google_sheet, log_result

# 인증 정보 및 스프레드시트 정보
json_file_path = "/Users/soohyepark/soohye-automation-test-98b439d0a39e.json"
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1FwTUfJCZB0IMdwToylHih5w8ej2lG_NzsNfJhyUbkA0/edit?gid=0#gid=0"
worksheet_name = "시트1"

# 구글 시트 연결
worksheet = connect_google_sheet(json_file_path, spreadsheet_url, worksheet_name)

# 테스트 결과 기록
log_result(worksheet, "Test Case 1", "PASS", "테스트 성공")
log_result(worksheet, "Test Case 2", "FAIL", "오류 발생")
