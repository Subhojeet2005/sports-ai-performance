import streamlit as st
import pandas as pd
from performance import PlayerPerformance
from agent import analyze
from visualization import show_visuals   # keep if using charts

# 🎯 Page Config
st.set_page_config(page_title="AI Sports Analyzer", page_icon="🏏")

st.title("🏏 AI Sports Performance Calculator")

# 🧾 Inputs
st.header("Enter Player Stats")

runs = st.number_input("Runs Scored", min_value=0, step=1)
balls = st.number_input("Balls Faced", min_value=1, step=1)  # fixed (no 0)
wickets = st.number_input("Wickets Taken", min_value=0, step=1)
catches = st.number_input("Catches", min_value=0, step=1)

# 📂 CSV Upload
st.write("## 📂 Upload Match Data (Optional)")
file = st.file_uploader("Upload CSV", type=["csv"])

if file is not None:
    try:
        df = pd.read_csv(file)
        st.write("### 📊 Data Preview")
        st.dataframe(df)

        required_cols = {"runs", "balls", "wickets", "catches"}

        if not required_cols.issubset(df.columns):
            st.error("CSV must contain: runs, balls, wickets, catches")
        else:
            row = df.iloc[0]

            runs = int(row["runs"])
            balls = int(row["balls"])
            wickets = int(row["wickets"])
            catches = int(row["catches"])

            st.success("Using uploaded data ✅")

    except Exception as e:
        st.error(f"Error reading file: {e}")

# 🚀 Button
if st.button("Analyze Performance"):

    player = PlayerPerformance(runs, balls, wickets, catches)
    result = analyze(player)

    st.subheader("📊 Performance Overview")

    # 📊 Metrics
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

    # 📊 Visualization (ONLY inside button)
 show_visuals(player, runs, wickets, catches)