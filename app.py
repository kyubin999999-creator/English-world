import streamlit as st
import pandas as pd
import random

st.title("📚 단어 암기 앱")

# ---------------------------
# 단어장 불러오기
# ---------------------------
try:
    vocab_df = pd.read_csv("vocab.csv")
except FileNotFoundError:
    # CSV 없으면 기본 리스트
    vocab_list = [
        {"word": "apple", "meaning": "사과"},
        {"word": "banana", "meaning": "바나나"},
        {"word": "cat", "meaning": "고양이"},
        {"word": "dog", "meaning": "개"},
        {"word": "sun", "meaning": "태양"},
        {"word": "moon", "meaning": "달"},
    ]
    vocab_df = pd.DataFrame(vocab_list)

# ---------------------------
# 단어 랜덤 선택
# ---------------------------
if st.button("단어 뽑기"):
    selected = vocab_df.sample(1).iloc[0]
    st.session_state.current_word = selected["word"]
    st.session_state.current_meaning = selected["meaning"]
    st.session_state.user_answer = ""

# ---------------------------
# 단어 맞추기
# ---------------------------
if "current_word" not in st.session_state:
    st.write("버튼을 눌러 단어를 뽑으세요!")
else:
    st.subheader(f"단어: {st.session_state.current_word}")
    user_input = st.text_input("뜻을 입력하세요", value=st.session_state.get("user_answer", ""))

    if st.button("확인"):
        st.session_state.user_answer = user_input
        correct = st.session_state.current_meaning.strip().lower()
        answer = user_input.strip().lower()

        if answer == correct:
            st.success("✅ 정답입니다!")
        else:
            st.error(f"❌ 틀렸습니다. 정답: {st.session_state.current_meaning}")
