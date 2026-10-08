import random
import streamlit as st

# 페이지 제목 설정
st.title("🎰 Streamlit 로또 번호 생성기")

# 세션 상태 초기화 (번호 세트를 최대 5개까지 저장하는 리스트)
if "lotto_sets" not in st.session_state:
    st.session_state.lotto_sets = []

# 로또 공 색상 스타일 반환 함수 (실제 동행복권 색상 기준)
def get_ball_style(num):
    if 1 <= num <= 10:
        color = "#fbc400"  # 노란색
    elif 11 <= num <= 20:
        color = "#69c6f0"  # 파란색
    elif 21 <= num <= 30:
        color = "#ff7272"  # 빨간색
    elif 31 <= num <= 40:
        color = "#aaa"      # 회색
    else:
        color = "#b0d840"  # 초록색

    return f"""
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 45px;
        height: 45px;
        border-radius: 50%;
        background-color: {color};
        color: white;
        font-weight: bold;
        font-size: 18px;
        margin: 4px;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    """

# 버튼 및 초기화 영역
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🎲 로또번호 생성"):
        if len(st.session_state.lotto_sets) >= 5:
            st.warning("최대 5개 세트까지만 생성할 수 있습니다. 초기화 후 다시 시도해 주세요.")
        else:
            # 1~45 중 중복 없는 6개 추출 후 정렬
            numbers = sorted(random.sample(range(1, 46), 6))
            st.session_state.lotto_sets.append(numbers)

with col2:
    if st.button("🔄 번호 초기화"):
        st.session_state.lotto_sets = []
        st.rerun()

st.markdown("---")

# 생성된 번호 세트 화면 출력 (최대 5세트)
if st.session_state.lotto_sets:
    for idx, lotto_set in enumerate(st.session_state.lotto_sets, 1):
        # 공들을 한 줄로 표시하기 위해 HTML 변환
        balls_html = "".join(
            f'<div style="{get_ball_style(n)}">{n}</div>' for n in lotto_set
        )
        st.markdown(f"**게임 {idx}:** &nbsp; {balls_html}", unsafe_allow_html=True)
else:
    st.info("버튼을 눌러 로또 번호를 생성해 보세요. (최대 5세트)")