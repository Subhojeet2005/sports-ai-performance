
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def show_visuals(player, runs, wickets, catches):

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

    # Normalize
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

 96ff8d4 (added visualization for stable deploy)
    st.pyplot(fig2)