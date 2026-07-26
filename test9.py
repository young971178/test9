import streamlit as st
import random

st.set_page_config(layout="wide")

if 'user' not in st.session_state:
    st.session_state.user = random.choice(["박찬호", "박지성", "이영표", "류현진", "손흥민"])
if 'page' not in st.session_state:
    st.session_state.page = "main"

def go_subpage():
    st.session_state.page = "sub"

def go_main():
    st.session_state.page = "main"

if st.session_state.page == "sub":
    st.button("되돌아가기", on_click=go_main)
else:
    st.title(f"{st.session_state.user} 프로님 AXage에 오신 것을 환영합니다.")
    
    st.header("What's New!")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("GDX 과제 최신 소식")
        st.write("아라미드 생산2팀에서 A급율을 높이기 위한 극한 과제에 도전하고 있습니다. 함께 응원해 주세요")
        st.button("응원하러 바로가기", on_click=go_subpage, key="n1")
        st.divider()
        st.write("코오드 생산팀의 KIB 열수축응력 개선과제가 성공적으로 완료 되었습니다.")
        st.button("개선성과 보러가기", on_click=go_subpage, key="n2")
        st.divider()
        st.write("GDX 과제정의 Agent 가 새롭게 개발되었습니다. 과제정의서 작성은 이제 Agent 에게 맡기세요")
        st.button("'과제정의 Agent' 바로가기", on_click=go_subpage, key="n3")

    with col2:
        st.subheader("GDX 교육 On Air~!")
        st.write("미니탭 리터러시 오프라인 교육 과정이 새롭게 개설 되었습니다. 이론과 경험을 겸비한 엄유범 프로님의 강의를 만끽하세요")
        st.button("미니탭 리터러시 오프라인 교육 더 알아보기", on_click=go_subpage, key="e1")
        st.divider()
        st.write("기술통계 온라인 과정이 리뉴얼 되었습니다. 기존의 이론중심 교육이 아닌 코딩 위주의 실습형 교육을 체험해 보세요")
        st.button("기술통계 온라인 과정 더 알아보기", on_click=go_subpage, key="e2")
        st.divider()
        st.write("머신러닝-모델링 모듈의 강사진에 지덱수 프로님이 합류하셨습니다. 중합공정의 최적화 문제라면 이젠 지덱수 프로님의 강의가 딱이겠지요?")
        st.button("지덱수 프로님의 머신러닝모델링 강의 교안 보러가기", on_click=go_subpage, key="e3")

    with col3:
        st.subheader("새로운 배지 획득을 축하합니다.")
        st.write("지덱수 프로님이 머신러닝-모델링 모듈의 골드크라운 배지를 획득하셨습니다. 멋진 사내강사 활동 기대합니다.")
        st.button("좋아요", on_click=go_subpage, key="b1")
        st.divider()
        st.write("기냥 프로님이 파이썬리터러시 그린배지를 획득하셨습니다. 골드크라운을 획득하는 그날까지 쭈욱 응원합니다")
        st.button("좋아요", on_click=go_subpage, key="b2")
        st.divider()
        st.write("GDX 아카데미에서 AI Automation 사내강사로서 활동하실 인재를 모집합니다.")
        st.button("사내강사 등록신청 바로가기", on_click=go_subpage, key="b3")

    st.divider()
    
    r2_c1, r2_c2, r2_c3, r2_c4, r2_c5, r2_c6 = st.columns(6)
    
    with r2_c1:
        st.link_button("GDX 아카데미 수강신청 바로가기", "https://njptvnmnnutbylghv4zuu2.streamlit.app/")
    with r2_c2:
        st.write("AXage 는 인사 및 승진제도와 연계됩니다.")
        st.button("인사제도 확인 바로가기", on_click=go_subpage, key="hr")
    with r2_c3:
        st.link_button("온라인 교육 수강생 응시 바로가기", "https://fqjhmeynfrjdppf4f38vgb.streamlit.app/")
    with r2_c4:
        st.button("오프라인 교육 수강생 과제제출 바로가기", on_click=go_subpage, key="hw")
    with r2_c5:
        st.button("AXage 불편신고 및 개선건의", on_click=go_subpage, key="voc")
    with r2_c6:
        st.link_button("관리자 전용, 응시결과 확인", "https://mbpaucgnbv5d8syegjpqh6.streamlit.app/")

    st.divider()
    st.markdown("<h5 style='text-align: center;'>측정할 수 없는 것은 개선할 수 없습니다</h5>", unsafe_allow_html=True)
