import pydata_google_auth
import gspread
import json
import os
import platform

# 구글 인증 및 스프레드시트 연결
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
credentials = pydata_google_auth.get_user_credentials(SCOPES, auth_local_webserver=True)
credentials.access_token = credentials.token
google_client = gspread.authorize(credentials)


def load_worksheet(spreadsheet_url, worksheet_name):
    """
    구글 스프레드시트에서 워크시트를 로드합니다.
    """
    spreadsheet = google_client.open_by_url(spreadsheet_url)
    return spreadsheet.worksheet(worksheet_name)

def update_test_result(worksheet, sheet_num, use_type, status=None, remarks=""):
    """
    테스트 결과를 업데이트합니다.
    :param worksheet: 구글 스프레드시트 워크시트 객체
    :param sheet_num: 테스트 케이스 번호
    :param use_type: JSON 데이터의 use_type 값
    :param status: 상태("pass", "fail", "untest") (기본값은 None)
    :param remarks: 추가 메모 (기본값은 빈 문자열)
    """
    # 상태가 명시되지 않은 경우 use_type에 따라 상태 결정
    if status is None:
        if use_type == 2:
            status = "pass"
            color = {"red": 0.0, "green": 0.5, "blue": 0.0}  # 초록색
        else:
            status = "untest"
            color = {"red": 0.5, "green": 0.5, "blue": 0.5}  # 회색
    elif status == "fail":
        color = {"red": 1.0, "green": 0.0, "blue": 0.0}  # 빨간색

    # 테스트 결과 기록
    worksheet.update([[status]], f"D{sheet_num + 2}")
    worksheet.format(f"D{sheet_num + 2}", {"textFormat": {"foregroundColor": color, "bold": True}})

    # 비고란 업데이트
    worksheet.update([[remarks]], f"E{sheet_num + 2}")

# def update_test_result(worksheet, sheet_num, status, remarks=""):
#     """
#     테스트 결과를 업데이트합니다.
#     """
#     if status == "pass":
#         color = {"red": 0.0, "green": 0.5, "blue": 0.0}
#     elif status == "fail":
#         color = {"red": 1.0, "green": 0.0, "blue": 0.0}
#     else:  # untest
#         color = {"red": 0.5, "green": 0.5, "blue": 0.5}
#
#     worksheet.update([["untest" if status == "untest" else status]], f"D{sheet_num + 2}")
#     worksheet.format(f"D{sheet_num + 2}", {"textFormat": {"foregroundColor": color, "bold": True}})
#     worksheet.update([[remarks]], f"E{sheet_num + 2}")
