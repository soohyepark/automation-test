from src.home import HomePage
from config.google_sheet import *

def load_json_config():
    """
    운영체제에 따라 JSON 설정 파일을 로드합니다.
    """
    os_version = platform.platform()
    if 'Windows' in os_version:
        param_json_path = os.path.dirname(__file__) + '\\json\\'
    else:
        param_json_path = os.path.dirname(__file__) + '/json/'

    current_json = param_json_path.replace('/tests', '') + os.path.splitext(os.path.basename(__file__))[0] + '.json'

    try:
        with open(current_json, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {current_json}")
    except json.JSONDecodeError:
        raise ValueError(f"JSON 파일 형식이 올바르지 않습니다: {current_json}")
    except Exception as e:
        raise Exception(f"예상치 못한 오류 발생: {e}")

# 설정 정보
SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1FwTUfJCZB0IMdwToylHih5w8ej2lG_NzsNfJhyUbkA0/edit?gid=0#gid=0"
WORKSHEET_NAME = "tc2"

# Google Sheet 데이터 로드
worksheet = load_worksheet(SPREADSHEET_URL, WORKSHEET_NAME)
json_data = load_json_config()

def input_pass(sheet_num):
    """
    테스트 케이스가 성공한 경우 결과를 스프레드시트에 기록합니다.
    :param sheet_num: 테스트 케이스 번호
    """
    cell_position = f"D{sheet_num + 2}"
    remarks_position = f"E{sheet_num + 2}"
    use_type = json_data[0][f"tc{sheet_num}"]["use_type"]

    if use_type == 2:
        # 성공: "pass" 기록 및 초록색으로 포맷
        worksheet.update([["pass"]], cell_position)
        worksheet.format(cell_position, {
            "textFormat": {
                "foregroundColor": {"red": 0.0, "green": 0.5, "blue": 0.0},
                "bold": True
            }
        })
    else:
        # 테스트 안함: "untest" 기록 및 회색으로 포맷
        worksheet.update([["untest"]], cell_position)
        worksheet.format(cell_position, {
            "textFormat": {
                "foregroundColor": {"red": 0.5, "green": 0.5, "blue": 0.5},
                "bold": True
            }
        })

    # 비고란 초기화
    worksheet.update([[" "]], remarks_position)

def input_fail(sheet_num, error_reason):
    """
    테스트 케이스가 실패한 경우 결과를 스프레드시트에 기록합니다.
    :param sheet_num: 테스트 케이스 번호
    :param error_reason: 실패 원인
    """
    cell_position = f"D{sheet_num + 2}"
    remarks_position = f"E{sheet_num + 2}"

    # 실패: "fail" 기록 및 빨간색으로 포맷
    worksheet.update([["fail"]], cell_position)
    worksheet.format(cell_position, {
        "textFormat": {
            "foregroundColor": {"red": 1.0, "green": 0.0, "blue": 0.0},
            "bold": True
        }
    })

    # 비고란에 실패 원인 기록
    worksheet.update([[str(error_reason)]], remarks_position)

def test_search(driver):
    home_page = HomePage(driver)
    # 검색 테스트 로직 (예시)
    try:
        home_page.input_move_login_screen(2)
        home_page.ss_1_5_1_1(
            json_data[0]["tc1"]["use_type"],
            json_data[0]["tc1"]["value1"]
        )
        input_pass(1)

    except Exception as e:
        input_fail(1, e)