import streamlit as st
from performance import PlayerPerformance
from agent import analyze

st.title("🏏 AI Sports Performance Calculator")

runs = st.number_input("Runs", 0)
balls = st.number_input("Balls", 1)
wickets = st.number_input("Wickets", 0)
catches = st.number_input("Catches", 0)

if st.button("Analyze"):
    player = PlayerPerformance(runs, balls, wickets, catches)
    result = analyze(player)

    st.write("Score:", result["score"])
    st.write("Analysis:", result["analysis"])
    st.write("Summary:", result["summary"])

    st.write("Suggestions:")
    for s in result["suggestions"]:
        st.write("-", s)