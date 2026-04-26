import streamlit as st
from performance import PlayerPerformance
from agent import analyze

# 🎯 Page Config
st.set_page_config(page_title="AI Sports Analyzer", page_icon="🏏")

st.title("🏏 AI Sports Performance Calculator")

# 🧾 Inputs
st.header("Enter Player Stats")

runs = st.number_input("Runs Scored", min_value=0, step=1)
balls = st.number_input("Balls Faced", min_value=1, step=1)
wickets = st.number_input("Wickets Taken", min_value=0, step=1)
catches = st.number_input("Catches", min_value=0, step=1)

# 🚀 Button
if st.button("Analyze Performance"):

    player = PlayerPerformance(runs, balls, wickets, catches)
    result = analyze(player)

    st.subheader("📊 Performance Overview")

    # 📊 Metrics Panel
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Score", result["score"])
    col2.metric("Runs", runs)
    col3.metric("Strike Rate", round(player.strike_rate(), 2))
    col4.metric("Wickets", wickets)

    # 🧠 Analysis
    st.write("### 🧠 Analysis")
    st.write(result["analysis"])

    # 📌 Summary
    st.write("### 📌 Summary")
    st.write(result["summary"])

    # 💡 Suggestions
    st.write("### 💡 Suggestions")
    for s in result["suggestions"]:
        st.write(f"- {s}")