import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def main():
    st.set_page_config(page_title="Ruit League 2023", page_icon=":trophy:", layout="wide")

    menu = ["Data Entry", "Data Visualization"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Data Entry":
        st.title("Ruit League Data Entry")

        team_names = st.text_input("Enter comma separated team names:")
        team_list = team_names.split(',')

        data = []
        for team in team_list:
            team = team.strip()
            player_1 = st.text_input(f"Enter player name for team {team}:", key=f"{team}_player_1")
            player1_cups = st.number_input(f"Enter the number of cups hit by {player_1}:", value=0, step=1, key=f"{team}_player1_cups")
            data.append({'team': team, 'player_name': player_1, 'player_cups': player1_cups})
            player_2 = st.text_input(f"Enter player name for team {team}:", key=f"{team}_player_2")
            player2_cups = st.number_input(f"Enter the number of cups hit by {player_2}:", value=0, step=1, key=f"{team}_player2_cups")
            data.append({'team': team, 'player_name': player_2, 'player_cups': player2_cups})

        # New additions to track additional data points
        ot = st.checkbox("Was there overtime?")
        final_score = st.text_input("Enter the final score (e.g. 1 - 0)")
        final_cup = st.text_input("Who hit the final cup?")

        df = pd.DataFrame(data)

        df["overtime"] = ot
        df["final_cup"] = final_cup
        df["final_score"] = final_score
        df["submission_time"] = str(datetime.datetime.now())

        if st.button("Submit"):
            st.write(df)

            # save the data to a file
            df.to_csv('ruit_league_data.csv', index=False)

            # display a success message
            st.success("Data submitted successfully!")
    else:
        # load the data from the file
        player_data = pd.read_csv('ruit_league_data.csv')

        st.write("Player Data:", player_data)

        if st.checkbox("Show Plot"):
            fig, ax = plt.subplots()
            ax.bar(player_data["player_name"], player_data["player_cups"])
            st.pyplot(fig)

if __name__ == "__main__":
    main()
