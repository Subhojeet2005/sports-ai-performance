import streamlit as st
from performance import PlayerPerformance
from agent import analyze

# 🎯 Page config
st.set_page_config(page_title="AI Sports Analyzer", page_icon="🏏")

st.title("🏏 AI Sports Performance Calculator")

# 🧾 Inputs
runs = st.number_input("Runs Scored", min_value=0, step=1)
balls = st.number_input("Balls Faced", min_value=1, step=1)
wickets = st.number_input("Wickets Taken", min_value=0, step=1)
catches = st.number_input("Catches", min_value=0, step=1)

# 🚀 Button
if st.button("Analyze Performance"):

    player = PlayerPerformance(runs, balls, wickets, catches)
    result = analyze(player)

    # 📊 Output
    st.subheader("📊 Performance Result")

    st.write(f"**Score:** {result['score']}")
    st.write(f"**Analysis:** {result['analysis']}")
    st.write(f"**Summary:** {result['summary']}")

    st.write("### 💡 Suggestions")
    for s in result["suggestions"]:
        st.write(f"- {s}")