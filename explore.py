import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_explore_page():
    # load the data from the file
    df = pd.read_csv('ruit_league_data.csv')

    st.write("Player Data:", df)

    grouped = df.groupby("Player 1").sum()["Player 1 Cups"]
    games = df.groupby("Player 1")
    st.write(games)
    st.write(grouped)

    # apply the Seaborn theme
    sns.set_style("dark")

    fig, ax = plt.subplots()
    ax.bar(grouped.index, grouped.values, color=sns.color_palette())

    ax.set_xlabel("Player Name")
    ax.set_ylabel("Number of Cups Hit")
    ax.set_title("Cups Hit by Player")

    st.pyplot(fig)