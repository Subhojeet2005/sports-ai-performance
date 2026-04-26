import streamlit as st
from performance import PlayerPerformance
from agent import analyze
import matplotlib.pyplot as plt
import numpy as np

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

    st.write("### 📌 Summary")
    st.write(result["summary"])

    st.write("### 💡 Suggestions")
    for s in result["suggestions"]:
        st.write(f"- {s}")

    # 📊 Bar Chart
    st.write("### 📊 Performance Breakdown")

    labels = ["Runs", "Strike Rate", "Wickets", "Catches"]
    values = [
        runs,
        player.strike_rate(),
        wickets * 10,
        catches * 5
    ]

    fig1, ax1 = plt.subplots()
    ax1.bar(labels, values)
    ax1.set_title("Player Performance Metrics")

    st.pyplot(fig1)

    # 🕸 Radar Chart
    st.write("### 🕸 Skill Radar")

    categories = ["Runs", "Strike Rate", "Wickets", "Catches"]

    values_radar = [
        runs,
        player.strike_rate(),
        wickets * 20,
        catches * 10
    ]

    # Normalize values
    max_vals = [100, 200, 100, 50]
    norm_values = [v/m for v, m in zip(values_radar, max_vals)]

    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    norm_values += norm_values[:1]
    angles += angles[:1]

    fig2 = plt.figure()
    ax2 = plt.subplot(111, polar=True)

    ax2.plot(angles, norm_values)
    ax2.fill(angles, norm_values, alpha=0.25)

    ax2.set_xticks(angles[:-1])
    ax2.set_xticklabels(categories)

    st.pyplot(fig2)