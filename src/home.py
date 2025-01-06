from xml.etree.ElementPath import xpath_tokenizer

from src.pages.base import *

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)  # 부모 클래스의 초기화 메서드 호출

    def __scroll_mobile_app_type(self, location, type, value, scroll_amount, max_scroll_count):
        """
        요소가 화면에 보일때까지 스크롤
        :param (str) location : 스크롤하려는 방향 / 1: 아래에서 위로 스와이프 / 2: 위에서 아래로 스와이프
        :param (str) type : Object Type (id or xpath)
        :param (str) value: Object Value
        :param (int) scroll_amount: 한번 스크롤시 이동하는 정도(1~10 사이에서 결정하며 숫자가 클수록 많이 이동)
        :param (int) max_scroll_count: 최대 스크롤 횟수 (스크롤 횟수에 도달할때까지 요소를 찾지 못하면 raise 발생)
        :return: 없음
        :example: __scroll_mobile_app_type(self,"1",xpath,3,20) # 해당 요소를 찾을 때까지 아래에서 위로 최대 20번 스크롤 진행
        """
        scroll_count = 0
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        k = (height / 20) * scroll_amount
        time.sleep(5)

        while True:
            try:
                self.driver.implicitly_wait(5)

                if type == "xpath":
                    element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, value)))
                elif type == "id":
                    element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, value)))

                if element.location['y'] > (height * 2 / 3):
                    loc = element.location
                    new_y = loc['y']
                    self.driver.swipe(width / 2, height / 2, width / 2, (height / 2) - k / 2)
                    if element.location['y'] == new_y:
                        print("스와이프 끝부분 도달")
                        break
                    print("위치 조정")
                elif element.location['y'] < (height * 1 / 3):
                    loc = element.location
                    new_y = loc['y']
                    self.driver.swipe(width / 2, height / 2, width / 2, (height / 2) + k / 2)
                    if element.location['y'] == new_y:
                        print("스와이프 끝부분 도달")
                        break
                    print("위치 조정")
                else:
                    print("요소 발견됨")
                    break
            except:
                scroll_count += 1
                if scroll_count > max_scroll_count:
                    print("최대 스크롤 횟수 초과")
                    raise Exception("요소를 찾을 수 없음")

                print("스크롤 진행 중 ({}회)".format(scroll_count))
                if location == "1":
                    self.driver.swipe(width / 2, height / 2, width / 2, (height / 2) - k)
                elif location == "2":
                    self.driver.swipe(width / 2, height / 2, width / 2, (height / 2) + k)
                else:
                    print("#", "스와이프할 방향을 지정해주세요.")
                    raise

            finally:
                # try 블록 이후에 원래의 implicit_wait 값으로 복원
                self.driver.implicitly_wait(self.implicit_wait)

    def __event_popup_all_close(self):
        """
        팝업 모두 닫기
        :param : 없음
        :example: __event_popup_all_close(self)
        """
        time.sleep(10)
        self.driver.implicitly_wait(5)
        runtext = 'MyG > 빅스 초특가 팝업 닫기'
        print("#", runtext, "시작")
        try:
            xpath = '//android.widget.RelativeLayout[@content-desc="닫기"]/android.widget.ImageView'
            element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
        except:
            print("인증 경고 팝업 처리 > 빅스 초특가 팝업 없음")
        finally:
            # try 블록 이후에 원래의 implicit_wait 값으로 복원
            self.driver.implicitly_wait(self.implicit_wait)
        # 중복 쿠폰 & 멤버쉽 팝업 처리
        self.driver.implicitly_wait(5)
        runtext = '메인페이지 > 중복 쿠폰 & 멤버쉽 팝업 닫기'
        print("#", runtext, "시작")
        try:
            id = 'com.ebay.kr.gmarket:id/ivClose'
            element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.ID, id)))
            element.click()
        except:
            print("메인페이지 > 중복 쿠폰 & 멤버쉽 팝업 노출 없음")
        finally:
            # try 블록 이후에 원래의 implicit_wait 값으로 복원
            self.driver.implicitly_wait(self.implicit_wait)
        print("#", runtext, "종료")
        # 빅스마일데이 이벤트 (에스파 PICK)
        self.driver.implicitly_wait(5)
        runtext = '메인페이지 > 빅스마일데이 이벤트 (에스파 PICK) 팝업 닫기'
        print("#", runtext, "시작")
        try:
            id = 'com.ebay.kr.gmarket:id/rlBottomAdClose'
            element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.ID, id)))
            element.click()
        except:
            print("빅스마일데이 이벤트 (에스파 PICK) 팝업 노출 없음")
        finally:
            # try 블록 이후에 원래의 implicit_wait 값으로 복원
            self.driver.implicitly_wait(self.implicit_wait)
        # 빅스마일데이 이벤트 (에스파 PICK)
        self.driver.implicitly_wait(5)
        runtext = '메인페이지 > 빅스마일데이 이벤트 (에스파 PICK) 팝업 닫기'
        print("#", runtext, "시작")
        try:
            id = 'com.ebay.kr.gmarket:id/rlBottomAdClose'
            element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.ID, id)))
            element.click()
            print("#", runtext, "종료")
        except:
            print("빅스마일데이 이벤트 (에스파 PICK) 팝업 노출 없음")
        finally:
            # try 블록 이후에 원래의 implicit_wait 값으로 복원
            self.driver.implicitly_wait(self.implicit_wait)

    def __select_home_section(self, section_name):

        """
        메인 페이지 > 해당 섹션 진입
        :param(str): section_name
        :return 없음
        :example: __select_home_section(self,section_name)
        """

        # 메인 페이지 > 탭+버튼 클릭
        time.sleep(2)
        runtext = '메인 페이지 > 탭+버튼 클릭'
        print("#", runtext, "시작")
        xpath = '//android.widget.ImageButton[@content-desc="메뉴 편집"]'
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
        print("#", runtext, "종료")

        xpath = '//android.widget.TextView[@resource-id="com.ebay.kr.gmarket:id/tvTitle" and @text="{0}"]'.format(
            section_name)
        HomePage.__scroll_mobile_app_type(self, "1", "xpath", xpath, 3, 30)

        runtext = '해당섹션 클릭'
        print("#", runtext, "시작")
        xpath = '//android.widget.TextView[@resource-id="com.ebay.kr.gmarket:id/tvTitle" and @text="{0}"]'.format(
            section_name)
        time.sleep(10)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
        print("#", runtext, "종료")

    def input_move_login_screen(self, use_type):
        """
        Gmarket 팝업 처리
        :param: 없음
        :return: 없음
        :example: input_move_login_screen(2)
        """

        if use_type == 2:
            # 디바이스 접근 권한 허용 승인
            try:
                time.sleep(2)
                runtext = '디바이스 접근 권한 허용 승인'
                print("#", runtext, "시작")
                id = "com.ebay.kr.gmarket:id/appPermissionBtn"
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
                element.click()
                print("#", runtext, "종료")
            except:
                print("Not Permission popup")


            # 지마켓 Notification 허용 알림 승인
            try:
                time.sleep(2)
                runtext = '지마켓 Notification 허용 알림 승인'
                print("#", runtext, "시작")
                xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]"
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                element.click()
                print("#", runtext, "종료")
            except Exception as e:
                print("Not Notification popup", e)
                raise

            # 빅스마일데이 팝업 끄기
            try:
                time.sleep(2)
                runtext = '빅스마일데이 팝업 끄기'
                print("#", runtext, "시작")
                id = "com.ebay.kr.gmarket:id/ivClose"
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
                element.click()
                print("#", runtext, "종료")
            except Exception as e:
                print("Not Notification popup", e)
        else:
            print("#", "권한 팝업 처리하지 않음")


    def ss_1_2_1_1(self, use_type, *args):
        """
        1.2.1-1) 베스트 > 기본기능
        :param (int) use_type: 사용 여부 (1: 미사용 / 2:사용)
        :param (list) args[0]: 위로 가기 버튼
        :param (str) args[1]: 전체 베스트 버튼
        :return: 없음
        :example: home_page.ss_1_2_1_1(2,*args)
        """

        if use_type == 2:
            print("#", "LP 1.2.1-1 Test Case 실행")
            runtext = '메인페이지 > 베스트 섹션 으로 이동'
            print("#", runtext, "시작")
            HomePage.__select_home_section(self,"베스트")
            print("#", runtext, "종료")

            runtext = '메인페이지 > 베스트 섹션 탑버튼 노출 확인'
            time.sleep(2)
            print("#", runtext, "시작")
            id = "com.ebay.kr.gmarket:id/topButton"
            HomePage.__scroll_mobile_app_type(self, "1", "id", id, 5, 10)
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
            value = element.get_attribute('content-desc')
            assert_that(value).is_in(args[0])  # 위로 가기
            print("#", runtext, "종료")

            runtext = '메인페이지 > 베스트 섹션 탑버튼 클릭시 동작 확인'
            time.sleep(2)
            print("#", runtext, "시작")
            element.click()
            xpath = '//android.widget.TextView[@resource-id="com.ebay.kr.gmarket:id/tv_title" and @text="전체 베스트"]'
            HomePage.__scroll_mobile_app_type(self,"2", "xpath", xpath, 10,10)
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            value = element.text
            assert_that(value).is_in(args[1])  # 전체 베스트
            print("#", runtext, "종료")

            # 베스트 > 새로고침 동작 확인
            runtext = '베스트 > 새로고침 동작 확인'
            print("#", runtext, "시작")
            xpath = '//android.widget.TextView[@resource-id="com.ebay.kr.gmarket:id/tv_title" and @text="전체 베스트"]'
            HomePage.__scroll_mobile_app_type(self, "2", "xpath", xpath, 10, 10)
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            value = element.text
            assert_that(value).is_in(args[1])  # 전체 베스트
            print("#", runtext, "종료")

        else:
            print("#", "BEST 1.2.1-1 Test Case 실행 생략")

    def input_login_account_type(self, use_type, *args):
        """
        Gmarket 회원 타입별 로그인 진행
        :param (int) use_type: 1 : 사용 안함, 2: 사용
        :param (str) args[0]: Gmarket ID
        :param (str) args[1]: Password
        :return: 없음
        """

        if use_type == 2:
            # 로그인 버튼 클릭
            runtext = '로그인 버튼 클릭'
            print("#", runtext, "시작")
            id = "com.ebay.kr.gmarket:id/clSubTitle"
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
            element.click()
            print("#", runtext, "종료")

            runtext = 'log_on_page > 계정 입력'
            print("#", runtext, "시작")
            xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.EditText'
            element = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.send_keys(args[0])
            print("#", runtext, "종료")

            runtext = 'log_on_page > 비밀 번호 입력'
            print("#", runtext, "시작")
            xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.EditText'
            element = self.driver.find_element(By.XPATH, xpath)
            element.send_keys(args[1])
            print("#", runtext, "종료")

            runtext = 'log_on_page > 로그인 버튼 클릭'
            print("#", runtext, "시작")
            xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.Button'
            element = self.driver.find_element(By.XPATH, xpath)
            element.click()
            print("#", runtext, "종료")

            time.sleep(10)

        else:
            print("#", "로그인 회원 타입 선택 없음")
            raise

    def ss_1_5_1_1(self, use_type, *args):
        """
        1.2.1-1) 베스트 > 기본기능
        :param (int) use_type: 사용 여부 (1: 미사용 / 2:사용)
        :param (str) args[0]: 검색어
        :return: 없음
        :example: home_page.ss_1_5_1_1(2,*args)
        """

        if use_type == 2:
            print("#", "1.5.1-1 Test Case 실행")
            # 검색 페이지 진입
            runtext = '검색 페이지 진입'
            print("#", runtext, "시작")
            # id = 'com.ebay.kr.gmarket:id/tvSearchBar'
            # xpath = '//android.widget.RelativeLayout[@content-desc="무엇을 찾아드릴까요?"]'
            id = 'com.ebay.kr.gmarket:id/rlSearchBar'
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
            element.click()
            print("#", runtext, "종료")

            # 지마켓메인 검색창 텍스트 입력
            runtext = '메인 페이지 > 검색창 텍스트 입력'
            print("#", runtext, "시작")
            id = "com.ebay.kr.gmarket:id/searchEditText"
            goods_name = args[0]
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, id)))
            element.send_keys(goods_name)
            print("#", runtext, "종료")

            # 지마켓메인 검색창 리턴
            runtext = '메인 페이지 > 검색창 텍스트 리턴'
            print("#", runtext, "시작")
            xpath = '//android.widget.ImageView[@content-desc="입력된 단어로 검색"]'
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            print("#", runtext, "종료")

            # 입력 및 검색된 텍스트 비교
            runtext = '메인 페이지 > 검색창 텍스트 리턴 > 입력 및 검색된 텍스트 비교'
            print("#", runtext, "시작")
            id = "com.ebay.kr.gmarket:id/searchKeyword"
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
            value = element.text
            assert value in goods_name, f"'{value}' not found in '{goods_name}'"
            print("#", runtext, "종료")

        else:
            print("#", "1.5.1-1 Test Case 실행 생략")