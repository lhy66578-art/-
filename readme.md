# 🎰 Streamlit 로또 번호 생성기 (Lotto Number Generator)

Streamlit을 활용하여 실제 로또 공 색상 스타일을 반영한 6자리 중복 없는 로또 번호 생성기 웹 애플리케이션입니다.

## 📌 주요 기능

* **로또 번호 자동 생성**: 1부터 45 사이의 중복 없는 번호 6개를 무작위 추출하여 오름차순으로 정렬합니다.
* **최대 5세트 누적**: 버튼을 누를 때마다 번호 세트가 아래로 누적되며, 최대 5개 세트까지 동시에 확인할 수 있습니다.
* **실제 로또 공 색상 적용**: 동행복권의 실제 번호 대역별 공 색상을 원형 배지로 표시합니다.
  * 🟡 **1 ~ 10번**: 노란색 (`#fbc400`)
  * 🔵 **11 ~ 20번**: 파란색 (`#69c6f0`)
  * 🔴 **21 ~ 30번**: 빨간색 (`#ff7272`)
  * ⚪ **31 ~ 40번**: 회색 (`#aaa`)
  * 🟢 **41 ~ 45번**: 초록색 (`#b0d840`)
* **초기화 기능**: `🔄 번호 초기화` 버튼을 눌러 생성된 세트를 지우고 다시 시작할 수 있습니다.

---

## 🛠️ 기술 스택

* **Language**: Python 3.8+
* **Framework**: Streamlit

---

## 🚀 실행 방법

### 1. 가상환경 생성 및 활성화 (선택 사항)
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 2. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. Streamlit 앱 실행
```bash
streamlit run app.py
```
> *(실행할 파이썬 코드 파일명이 `app.py`가 아닌 경우 해당 파일명으로 변경하여 실행해 주세요.)*