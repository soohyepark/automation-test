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
