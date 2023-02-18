import streamlit as st
import pandas as pd

def show_new_user_page():
    team_name = st.text_input("Enter Team Name. Leave blank if undecided")
    player1 = st.text_input("Enter First Team Member Name")
    player2 = st.text_input("Enter Second Team Member Name")

    if team_name == "":
        team_name = f"{player1}/{player2}"

    team_data = pd.read_csv("team_data.csv")

    if st.button("Add New Team"):
        if player1 == "":
            st.error("Enter name for player 1")
        elif player2 == "":
            st.error("Enter name for player 2")
        else:
            new_team = {
            "Team": team_name,
            "Player 1": player1,
            "Player 2": player2
            }

            new_df = new_df = pd.DataFrame(new_team, index=[0])
            team_data = pd.concat([team_data, new_df], ignore_index=True)

            team_data.to_csv("team_data.csv", index=False)

            st.success("New Team Added successfully!")

