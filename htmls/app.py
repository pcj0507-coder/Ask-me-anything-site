import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="뭐든지 대답해주는 마법의 사이트",
    page_icon="🔮",
    layout="centered"
)

# 2. 페이지 타이틀 및 소개 문구
st.title("🔮 뭐든지 대답해주는 마법의 사이트")
st.markdown("명쾌하고 재미있는 해답이 필요하신가요? 아래 마법의 사이트에서 고민을 해결해 보세요!")

# 3. index.html 파일 경로 설정 (상대 경로)
html_file_path = Path(__file__).resolve().parent / "htmls" / "index.html"

# 4. 파일 존재 여부 확인 및 HTML 렌더링
if html_file_path.exists():
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # iframe을 통해 HTML 코드를 전체 화면 너비로 렌더링 (높이는 충분하게 설정)
    components.html(html_code, height=900, scrolling=True)
else:
    # 5. 파일이 없을 때의 친절한 에러 메시지
    st.error(f"앗! 마법의 주문서(HTML 파일)를 찾을 수 없습니다. 폴더 구조와 파일 위치를 다시 한번 확인해주세요. 🥲")
    st.info(f"예상 경로: `{html_file_path}`")
