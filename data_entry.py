import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import boto3

def show_data_entry():
    st.title("Ruit League Data Entry")

    data_entry()

def data_entry():

    team_data = pd.read_csv("team_data.csv")

    col1, col2 = st.columns(2)

    dict_data = {}

    dict_data["Date"] = datetime.datetime.now().strftime("%m/%d/%Y %H:%M")

    with col1:
        team1 = st.selectbox("Team 1", team_data['Team'])
    with col2:
        team2 = st.selectbox("Team 2", team_data[team_data['Team'] != team1]['Team'])

    team_list = [team1, team2]

    data = []

    for i, team in enumerate(team_list):
        team = team.strip()
        data.append(team)
        with col1:
            player_1 = team_data.loc[team_data['Team'] == team1][f"Player {i + 1}"].iloc[0]
            player1_cups = st.number_input(f"Enter the number of cups hit by {player_1}:", value=0, step=1, key=f"{team}_player1_cups")        
        with col2:
            player_2 = team_data.loc[team_data['Team'] == team2][f"Player {i + 1}"].iloc[0]   
            player2_cups = st.number_input(f"Enter the number of cups hit by {player_2}:", value=0, step=1, key=f"{team}_player2_cups")
        
        data.append(player_1)
        data.append(player1_cups)
        data.append(player_2)
        data.append(player2_cups)
        
        dict_data[f"Team {i + 1}"] = team
        dict_data[f"Player {i + 1}"] = player_1
        dict_data[f"Player {i + 1} Cups"] = player1_cups
        dict_data[f"Player {i + 3}"] = player_2
        dict_data[f"Player {i + 3} Cups"] = player2_cups

    #dict_data = organize_data(dict_data)
    # track additional data points
    ot = st.checkbox("Was there overtime?")
    dict_data["Overtime"] = ot

    # final_score = st.text_input("Enter the final score (e.g. 1 - 0)")

    score = calc_final_score(dict_data)
    final_score = score[2]

    if final_score[0] == "0" and final_score[1] is "*":
        players = list(team_data[team_data['Team'] == team1][['Player 1', 'Player 2']].iloc[0])
        final_cup = st.selectbox("Who hit the final cup?", [f"{players[0]}, {players[1]} (Iced the game)"])
        final_cup = final_cup.replace("(Iced the game)", "").strip()
    elif final_score[0] == "0" and final_score[-1] is not "*":
        players = list(team_data[team_data['Team'] == team1][['Player 1', 'Player 2']].iloc[0])
        final_cup = st.selectbox("Who hit the final cup?", players)
    elif final_score[-1] == "*":
        players = list(team_data[team_data['Team'] == team2][['Player 1', 'Player 2']].iloc[0])
        final_cup = st.selectbox("Who hit the final cup?", [f"{players[0]}, {players[1]} (Iced the game)"])
        final_cup = final_cup.replace("(Iced the game)", "").strip()
    elif final_score[-1] == "0":
        players = list(team_data[team_data['Team'] == team2][['Player 1', 'Player 2']].iloc[0])
        final_cup = st.selectbox("Who hit the final cup?", players)
    else:
        final_cup = st.write("")

    if st.button("Submit"):
        if calc_final_score(dict_data) == "error":
            st.error("Incorrect score total. Please check inputed stats")
        else: 
            dict_data["Final Score"] = final_score
            dict_data["Final Cup"] = final_cup

            dict_data = organize_data(dict_data)

            new_df = pd.DataFrame(dict_data, index=[0])

            # get existing data
            df = pd.read_csv("ruit_league_data.csv")

            df = pd.concat([df, new_df], ignore_index=True)

            # save the data to a file
            df.to_csv("ruit_league_data.csv", index=False)

            # display a success message
            st.success("Data submitted successfully!")

def calc_final_score(dict_data):
    if dict_data["Overtime"] == False:
        team1_score = 12 - (dict_data["Player 1 Cups"] + dict_data["Player 2 Cups"])
        team2_score = 12 - (dict_data["Player 3 Cups"] + dict_data["Player 4 Cups"])
    else:
        team1_score = 16 - (dict_data["Player 1 Cups"] + dict_data["Player 2 Cups"])
        team2_score = 16 - (dict_data["Player 3 Cups"] + dict_data["Player 4 Cups"])

    if team1_score > 0 and team2_score > 0:
        return "error"
    elif team1_score == 0 and team2_score == 0:
        return "error"
    elif team1_score == -1 and team2_score == -1:
        return "error"
    elif team1_score <= -2 or team2_score <= -2:
        return "error"
    else:
        if team1_score >= 0 and team2_score >=0:
            return [team1_score, team2_score, f"{team1_score} - {team2_score}"]
        elif team1_score < 0 and team2_score == 0:
            return [team1_score, team2_score, "0* - 0"]
        elif team1_score == 0 and team2_score < 0:
            return [team1_score, team2_score, "0 - 0*"]
        else:
            if team1_score < 0:
                team1_score = "0*"
            if team2_score < 0:
                team2_score = "0*"
            return [team1_score, team2_score, f"{team1_score} - {team2_score}"]

def organize_data(dict_data):
    new_order = ["Date", "Team 1", "Player 1", "Player 1 Cups", "Player 2", 
                "Player 2 Cups", "Team 2", "Player 3", "Player 3 Cups", 
                "Player 4", "Player 4 Cups", "Overtime", "Final Score", "Final Cup"]
    dict_data = {k: dict_data[k] for k in new_order}
    return dict_data