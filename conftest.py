import pytest
from config.appium_config import get_driver
import psutil

@pytest.fixture(scope="session")
def driver():
    """
    WebDriver Fixture: 테스트에서 사용할 Appium WebDriver를 반환
    """
    driver = get_driver()  # appium_config.py의 get_driver() 호출
    yield driver
    driver.quit()  # 테스트 종료 시 WebDriver 종료

@pytest.fixture(scope="session", autouse=True)
def kill_appium_on_exit():
    """
    테스트 세션 종료 시 Appium 관련 프로세스를 종료
    """
    yield
    # Appium 관련 프로세스 종료
    for proc in psutil.process_iter(['pid', 'name']):
        if "appium" in proc.info['name'].lower():
            proc.kill()
            print(f"Appium 프로세스 종료: PID={proc.info['pid']}")
