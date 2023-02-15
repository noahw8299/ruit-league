import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import boto3

def show_data_entry():
    st.title("Ruit League Data Entry")

    dict_data = {}

    dict_data["Date"] = datetime.datetime.now().strftime("%m/%d/%Y %H:%M")

    team_names = st.text_input("Enter comma separated team names:")
    team_list = team_names.split(',')

    col1, col2 = st.columns(2)

    data = []

    for i, team in enumerate(team_list):
        team = team.strip()
        data.append(team)
        with col1:
            player_1 = st.text_input(f"Enter player name for team {team}:", key=f"{team}_player_1")
            player_2 = st.text_input(f"Enter player name for team {team}:", key=f"{team}_player_2")           
        with col2:
            player1_cups = st.number_input(f"Enter the number of cups hit by {player_1}:", value=0, step=1, key=f"{team}_player1_cups")
            player2_cups = st.number_input(f"Enter the number of cups hit by {player_2}:", value=0, step=1, key=f"{team}_player2_cups")
        
        data.append(player_1)
        data.append(player1_cups)
        data.append(player_2)
        data.append(player2_cups)
        
        dict_data[f"Team {i + 1}"] = team
        dict_data[f"Player {i * 2 + 1}"] = player_1
        dict_data[f"Player {i * 2 + 1} Cups"] = player1_cups
        dict_data[f"Player {i * 2 + 2}"] = player_2
        dict_data[f"Player {i * 2 + 2} Cups"] = player2_cups

    # track additional data points
    ot = st.checkbox("Was there overtime?")
    # final_score = st.text_input("Enter the final score (e.g. 1 - 0)")
    final_cup = st.text_input("Who hit the final cup?")

    if st.button("Submit"):
        dict_data["Overtime"] = ot

        if "Player 3 Cups" not in dict_data:
            st.error("Must enter 2 teams")
        elif calc_final_score(dict_data) == "error":
            st.error("Incorrect score total. Please check inputed stats")
        else: 
            dict_data["Final Score"] = calc_final_score(dict_data)
            dict_data["Final Cup"] = final_cup

            new_df = pd.DataFrame(dict_data, index=[0])

            st.write(new_df)

            # Create a session and resource for S3
            # session = boto3.session.Session()
            # s3 = session.resource("s3")

            # Get the S3 bucket you want to write to or read from
            # bucket = s3.Bucket("ruit-league")

            # get existing data
            df = pd.read_csv("ruit_league_data.csv")

            df = pd.concat([df, new_df], ignore_index=True)

            # save the data to a file
            df.to_csv("ruit_league_data.csv", index=False)

            # write csv to s3 bucket
            # s3.Bucket(bucket).put_object(Key=file_name, Body=csv_str)

            # display a success message
            st.success("Data submitted successfully!")

def calc_final_score(dict_data):
    team1_score = 12 - (dict_data["Player 1 Cups"] + dict_data["Player 2 Cups"])
    team2_score = 12 - (dict_data["Player 3 Cups"] + dict_data["Player 4 Cups"])

    if team1_score > 0 and team2_score > 0:
        return "error"
    elif team1_score <= -2 or team2_score <= -2:
        return "error"
    else:
        if dict_data["Overtime"] == False:
            if team1_score >= 0 and team2_score >=0:
                return f"{team1_score} - {team2_score}"
            elif team1_score < 0 and team2_score == 0:
                return "0* - 0"
            elif team1_score == 0 and team2_score < 0:
                return "0 - 0*"
            else:
                if team1_score < 0:
                    team1_score = "0*"
                if team2_score < 0:
                    team2_score = "0*"
                return f"{team1_score} - {team2_score}"
