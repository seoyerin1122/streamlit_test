import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="웹툰 취향 추천 테스트", layout="wide")


@st.cache_data
def load_data():
    time.sleep(2)  

    questions = [
        {
            "question": "새 웹툰을 볼 때 가장 먼저 보는 것은?",
            "options": ["인물 관계", "주인공 성장", "사건의 미스터리", "세계관 설정", "개그 코드"],
            "scores": ["로맨스", "액션", "스릴러", "판타지", "코미디"]
        },
        {
            "question": "다음 화가 가장 궁금해지는 순간은?",
            "options": ["관계 변화", "주인공 각성", "비밀 공개 직전", "새로운 세계관 등장", "웃긴 오해 발생"],
            "scores": ["로맨스", "액션", "스릴러", "판타지", "코미디"]
        },
        {
            "question": "가장 오래 기억에 남는 장면은?",
            "options": ["고백/이별", "전투/각성", "반전", "새로운 세계", "웃긴 대사"],
            "scores": ["로맨스", "액션", "스릴러", "판타지", "코미디"]
        },
        {
            "question": "웹툰을 고르는 기준에 가까운 것은?",
            "options": ["캐릭터 케미", "시원한 전개", "긴장감", "탄탄한 설정", "가볍게 보기"],
            "scores": ["로맨스", "액션", "스릴러", "판타지", "코미디"]
        },
        {
            "question": "친구에게 추천하고 싶은 웹툰 느낌은?",
            "options": ["설레는 작품", "통쾌한 작품", "끝까지 긴장되는 작품", "상상력이 돋보이는 작품", "웃긴 작품"],
            "scores": ["로맨스", "액션", "스릴러", "판타지", "코미디"]
        }
    ]

    descriptions = {
        "로맨스": "인물 간의 관계 변화와 감정선을 따라가며 몰입하는 유형입니다.",
        "액션": "주인공이 성장하고 강해지는 과정을 보며 통쾌함을 느끼는 유형입니다.",
        "스릴러": "예상하지 못한 반전과 긴장감 있는 전개를 좋아하는 유형입니다.",
        "판타지": "작품 속 세계관, 설정, 능력 체계에 흥미를 느끼는 유형입니다.",
        "코미디": "가볍게 웃으면서 볼 수 있는 작품을 선호하는 유형입니다."
    }

    recommendations = {
        "로맨스": [
            {"title": "유미의 세포들", "desc": "평범한 직장인 유미의 연애와 일상을 세포 시점으로 풀어낸 이야기"},
            {"title": "연애혁명", "desc": "고등학생들의 풋풋한 연애와 성장 이야기"},
            {"title": "바른연애 길잡이", "desc": "연애에 서툰 대학생들의 현실적인 연애 이야기"}
        ],
        "액션": [
            {"title": "화산귀환", "desc": "전설의 검객이 환생해 몰락한 문파를 다시 일으키는 이야기"},
            {"title": "외모지상주의", "desc": "외모와 힘, 학교생활을 중심으로 다양한 사건이 전개되는 이야기"},
            {"title": "나 혼자만 레벨업", "desc": "약한 헌터가 각성 후 점점 강해지는 성장형 액션 이야기"}
        ],
        "스릴러": [
            {"title": "스위트홈", "desc": "인간이 괴물로 변하는 세상에서 살아남기 위한 이야기"},
            {"title": "타인은 지옥이다", "desc": "이상한 이웃들과 함께 살며 벌어지는 공포 이야기"},
            {"title": "살인자ㅇ난감", "desc": "우연한 사건 이후 예상치 못한 방향으로 흘러가는 이야기"}
        ],
        "판타지": [
            {"title": "전지적 독자 시점", "desc": "소설 속 세계가 현실이 된 상황에서 살아가는 이야기"},
            {"title": "화산귀환", "desc": "무협 세계관과 성장 서사가 결합된 판타지 액션 이야기"},
            {"title": "나 혼자만 레벨업", "desc": "게임 시스템처럼 성장하는 헌터 이야기"}
        ],
        "코미디": [
            {"title": "마음의 소리", "desc": "일상 속 상황을 과장되게 풀어낸 개그 웹툰"},
            {"title": "놓지마 정신줄", "desc": "엉뚱한 가족과 주변 인물들이 만들어내는 코미디 이야기"},
            {"title": "대학일기", "desc": "대학생의 일상과 공감을 유쾌하게 풀어낸 이야기"}
        ]
    }

    return questions, descriptions, recommendations


st.title("웹툰 취향 추천 테스트")
st.write("학번: 2023508127")
st.write("이름: 서예린")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("로그인")

    user = st.text_input("아이디")
    pw = st.text_input("비밀번호", type="password")

    if st.button("로그인"):
        if user == "webtoon" and pw == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("아이디 또는 비밀번호가 올바르지 않습니다.")

else:
    questions, descriptions, recommendations = load_data()

    st.subheader("인기 웹툰")

    col_img1, col_img2 = st.columns(2)

    with col_img1:
        st.image("img1.jpg", caption="화산귀환", width=300)

    with col_img2:
        st.image("img2.jpg", caption="외모지상주의", width=300)

    st.subheader("취향 테스트")

    score = {
        "로맨스": 0,
        "액션": 0,
        "스릴러": 0,
        "판타지": 0,
        "코미디": 0
    }

    for i, q in enumerate(questions):
        st.write(f"{i + 1}. {q['question']}")
        selected = st.radio(
            "선택",
            q["options"],
            key=f"question_{i}",
            label_visibility="collapsed"
        )

        idx = q["options"].index(selected)
        score[q["scores"][idx]] += 1

    if st.button("결과 보기"):
        result = max(score, key=score.get)

        st.markdown("---")
        st.header("테스트 결과")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("나의 웹툰 취향", result)

        with col2:
            st.metric("최고 점수", score[result])

        st.success(descriptions[result])

        st.subheader("취향 점수 분석")

        df_score = pd.DataFrame({
            "유형": list(score.keys()),
            "점수": list(score.values())
        })

        st.dataframe(df_score, use_container_width=True)
        st.bar_chart(df_score.set_index("유형"))

        st.subheader("추천 웹툰")

        df_recommend = pd.DataFrame(recommendations[result])
        df_recommend = df_recommend.rename(columns={
            "title": "웹툰 제목",
            "desc": "줄거리"
        })

        st.table(df_recommend)

    st.markdown("---")
    st.subheader("캐싱 기능 시연")

    st.write("퀴즈 문항, 유형 설명, 추천 웹툰 데이터를 불러오는 load_data 함수에 캐싱을 적용했습니다.")

    col_cache1, col_cache2 = st.columns(2)

    with col_cache1:
        if st.button("퀴즈/추천 데이터 다시 불러오기"):
            start = time.time()
            load_data()
            end = time.time()

            st.success("퀴즈 문항과 추천 웹툰 데이터를 불러왔습니다.")
            st.write(f"실행 시간: {end - start:.2f}초")

    with col_cache2:
        if st.button("캐시 초기화"):
            load_data.clear()
            st.warning("캐시를 초기화했습니다.")

    