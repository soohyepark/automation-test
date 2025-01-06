## 프로젝트 이름
Automation-test

## 📖 프로젝트 소개
이 프로젝트는 **앱 UI 테스트 자동화**를 구현하기 위한 목적으로 만들어졌습니다.  
주요 목표는 테스트 효율성을 높이고, 안정적인 코드를 유지하는 것입니다.

---

## ✨ 주요 기능
- Appium을 사용한 모바일 앱 테스트
- Google Sheets와 연동한 테스트 결과 기록
- JSON 기반 테스트 케이스 관리
- 플랫폼별(OS)에 따른 경로 설정 자동화

---

## 📂 디렉토리 구조
automation/
├── config/                  # 설정 파일 디렉토리
│   └── google_sheet.py      # Google Sheets API 연동
├── src/                     # 소스 코드
│   ├── home.py              # 홈 화면 관련 자동화 로직
│   └── pages/               # 페이지 관련 모듈
│       ├── base.py          # 공통 페이지 동작 정의
├── json/                    # 테스트 케이스 JSON 파일
│   └── home_section.json    # 홈섹션 JSON 파일
├── tests/                   # 테스트 스크립트
│   ├── test_home_section.py # 홈섹션 테스트 케이스
│   ├── test_search.py       # 검색 테스트 케이스
└── conftest.py              # Pytest/Appium 설정 및 공통 픽스처

## 🛠️ 사용 기술 스택
- Python 3.11
- Pytest: 테스트 프레임워크
- Appium: 모바일 자동화 테스트 도구
- Google Sheets API: 테스트 결과 기록
