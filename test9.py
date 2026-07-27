import streamlit as st
import random

st.set_page_config(page_title="AXage", layout="wide")

if 'user' not in st.session_state:
    st.session_state.user = random.choice(["박찬호", "박지성", "이영표", "류현진", "손흥민"])
if 'page' not in st.session_state:
    st.session_state.page = "main"

def go_subpage():
    st.session_state.page = "sub"

def go_main():
    st.session_state.page = "main"

if st.session_state.page == "sub":
    st.button("🔙 되돌아가기", on_click=go_main)
else:
    st.markdown(f"### 👋 **{st.session_state.user}** 프로님, AXage에 오신 것을 환영합니다.")
    st.write("")
    
    st.header("✨ What's New!")
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.subheader("📢 GDX 과제 소식")
        with st.container(border=True):
            st.markdown("**아라미드 생산2팀**\n\nA급율을 높이기 위한 극한 과제에 도전하고 있습니다.")
            st.button("응원하러 바로가기 🚀", on_click=go_subpage, key="n1", use_container_width=True)
        with st.container(border=True):
            st.markdown("**코오드 생산팀**\n\nKIB 열수축응력 개선과제가 성공적으로 완료되었습니다.")
            st.button("개선성과 보러가기 📊", on_click=go_subpage, key="n2", use_container_width=True)
        with st.container(border=True):
            st.markdown("**과제정의 Agent**\n\n새롭게 개발되었습니다. 과제정의서 작성은 이제 맡기세요.")
            st.button("Agent 바로가기 🤖", on_click=go_subpage, key="n3", use_container_width=True)

    with col2:
        st.subheader("📺 GDX 교육 On Air")
        with st.container(border=True):
            st.markdown("**미니탭 리터러시 오프라인**\n\n이론과 경험을 겸비한 엄유범 프로님의 강의를 만끽하세요.")
            st.button("오프라인 교육 알아보기 🔍", on_click=go_subpage, key="e1", use_container_width=True)
        with st.container(border=True):
            st.markdown("**기술통계 온라인 과정**\n\n코딩 위주의 실습형 교육으로 리뉴얼되었습니다.")
            st.button("온라인 과정 알아보기 🔍", on_click=go_subpage, key="e2", use_container_width=True)
        with st.container(border=True):
            st.markdown("**머신러닝-모델링 모듈**\n\n지덱수 프로님 합류! 중합공정의 최적화 문제에 딱 맞습니다.")
            st.button("강의 교안 보러가기 📑", on_click=go_subpage, key="e3", use_container_width=True)

    with col3:
        st.subheader("🏆 배지 획득 축하")
        with st.container(border=True):
            st.markdown("**지덱수 프로님**\n\n머신러닝-모델링 모듈 **골드크라운** 👑 획득!")
            st.button("👍 좋아요", on_click=go_subpage, key="b1", use_container_width=True)
        with st.container(border=True):
            st.markdown("**기냥 프로님**\n\n파이썬리터러시 **그린배지** 🌿 획득!")
            st.button("👍 좋아요", on_click=go_subpage, key="b2", use_container_width=True)
        with st.container(border=True):
            st.markdown("**사내강사 모집**\n\nGDX 아카데미에서 AI Automation 사내강사 활동하실 인재를 모집합니다.")
            st.button("등록신청 바로가기 📝", on_click=go_subpage, key="b3", use_container_width=True)

    st.divider()
    
    st.subheader("🔗 퀵 링크")
    r2_c1, r2_c2, r2_c3 = st.columns(3)
    
    with r2_c1:
        st.link_button("🎓 GDX 아카데미 수강신청", "https://njptvnmnnutbylghv4zuu2.streamlit.app/", use_container_width=True)
        st.button("🏢 인사 및 승진제도 연계 확인", on_click=go_subpage, key="hr", use_container_width=True)
        
    with r2_c2:
        st.link_button("💻 온라인 교육 수강생 응시", "https://fqjhmeynfrjdppf4f38vgb.streamlit.app/", use_container_width=True)
        st.button("📝 오프라인 교육 과제제출", on_click=go_subpage, key="hw", use_container_width=True)
        
    with r2_c3:
        st.button("💡 덱수의 와이낫 몰아보기", on_click=go_subpage, key="voc", use_container_width=True)
        st.link_button("⚙️ 관리자 전용 응시결과 확인", "https://mbpaucgnbv5d8syegjpqh6.streamlit.app/", use_container_width=True)

    st.divider()
    st.markdown("<h4 style='text-align: center; color: gray; font-weight: normal;'>GDX, 측정할 수 없는 것은 개선할 수 없습니다</h4>", unsafe_allow_html=True)
