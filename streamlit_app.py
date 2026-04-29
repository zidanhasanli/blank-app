import streamlit as st
from strategy_advisor import run_strategy_session

st.title("AI Multi-Agent Strategy Advisor")

question = st.text_input(
    "Enter your strategy question",
    "We want high engagement with limited budget"
)

org = st.selectbox(
    "Select organization type",
    ["student", "business", "nonprofit", "university"]
)

if st.button("Generate Strategy"):

    result = run_strategy_session(question)

    st.subheader("Final Recommendation")
    st.write(result["winner"])

    st.subheader("Confidence")
    st.write(result["confidence"])

    st.subheader("Votes")
    st.write(result["votes"])
