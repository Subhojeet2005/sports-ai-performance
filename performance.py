import streamlit as st
from performance import PlayerPerformance
from agent import analyze

st.title("🏏 AI Sports Performance Calculator")

runs = st.number_input("Runs")
balls = st.number_input("Balls")
wickets = st.number_input("Wickets")
catches = st.number_input("Catches")

if st.button("Analyze"):
    player = PlayerPerformance(runs, balls, wickets, catches)
    score, analysis, suggestions = analyze(player)

    st.subheader(f"Score: {score}")
    st.write("Analysis:", analysis)

    st.write("Suggestions:")
    for s in suggestions:
        st.write("-", s)