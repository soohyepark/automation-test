import gspread

def connect_google_sheet(json_file_path, spreadsheet_url, worksheet_name):
    """
    구글 스프레드시트에 연결하여 원하는 워크시트를 반환합니다.
    :param json_file_path: 서비스 계정 JSON 파일 경로
    :param spreadsheet_url: 구글 스프레드시트 URL
    :param worksheet_name: 워크시트 이름
    :return: 워크시트 객체
    """
    # gspread를 사용한 서비스 계정 인증
    client = gspread.service_account(json_file_path)

    # 스프레드시트 URL로 문서 열기
    spreadsheet = client.open_by_url(spreadsheet_url)

    # 워크시트 선택
    worksheet = spreadsheet.worksheet(worksheet_name)

    return worksheet


def log_result(worksheet, test_name, status, remarks=""):
    """
    테스트 결과를 구글 시트에 기록합니다.
    :param worksheet: 워크시트 객체
    :param test_name: 테스트 이름
    :param status: PASS 또는 FAIL
    :param remarks: 추가 메모
    """
    # 데이터를 기록할 위치 설정 (현재 시트의 마지막 행에 추가)
    # 워크시트에서 마지막 행 번호 찾기
    last_row = len(worksheet.get_all_values()) + 1  # 마지막 행 번호 (헤더 제외)

    # 기록할 데이터 준비
    row_data = [test_name, status, remarks]

    # 데이터 업데이트 (A열부터 C열까지 업데이트)
    worksheet.update(f'A{last_row}:C{last_row}', [row_data])
    print(f"✅ 테스트 결과 기록됨: {test_name} - {status}")
