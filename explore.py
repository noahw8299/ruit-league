import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_explore_page():
    # load the data from the file
    df = pd.read_csv('ruit_league_data.csv')
    team_data = pd.read_csv('team_data.csv')
    team_data = update_team_record(df, team_data)
    player_stats = summarize_player_stats(df, team_data)

    sorted_team_data = team_data.sort_values(by=['Win', 'Loss'], ascending=[False, True])

    st.write("Game Log:", df)

    col1, col2 = st.columns(2)

    with col1:
        st.write("Team Stats:", sorted_team_data)
    with col2:
        st.write("Player Stats", player_stats)

    # Set the style and color palette
    sns.set_style('darkgrid')

    display_stats(player_stats, 'Name', 'Total Cups', 'Total Cups Hit by Player', 'Player', 'Total Cups')
    display_stats(player_stats, 'Name', 'Cups/Game', 'Average Cups per Game', 'Player', 'Cups per Game')
    display_stats(player_stats, 'Name', 'Final Cups/Win', 'Final Cups Hit per Win', 'Player', 'Final Cups/Win')
    display_stats(player_stats, 'Name', 'Final Cups', 'Total Final Cups', 'Player', 'Final Cups')


def summarize_player_stats(df, team_data):
    # First, create a list of all player names in the DataFrame
    player_names = set(df[['Player 1', 'Player 2', 'Player 3', 'Player 4']].values.flatten())

    # Create an empty dictionary to store the player stats
    player_stats = {}
    
    # Iterate over each player in the player_names list
    for player_name in player_names:
        player_cups = 0
        num_games = 0
        
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            # Check if the player's name appears in the row
            if player_name in row.values:
                # Find the column in which the player's name appears
                cols = ['Player 1', 'Player 2', 'Player 3', 'Player 4']
                col_name = df[cols].columns[(df[cols].iloc[index] == player_name).argmax()]
                cups_col = f"{col_name} Cups"
                player_cups += row[cups_col]
                num_games += 1
        
        # Store the player's stats in the player_stats dictionary
        player_stats[player_name] = {'Total Cups': player_cups, 'Num Games': num_games}

    new_df = pd.DataFrame.from_dict(player_stats, orient='index')
    new_df.reset_index(inplace=True)
    new_df.rename(columns={'index': 'Name'}, inplace=True)
    new_df = new_df[['Name', 'Total Cups', 'Num Games']]
    new_df['Cups/Game'] = new_df['Total Cups'] / new_df['Num Games']
    new_df['Team'] = None
    new_df = get_team_name(new_df, team_data)

    cup_counts = df['Final Cup'].str.split(',', expand=True).stack().str.strip().value_counts()
    new_df['Final Cups'] = new_df['Name'].apply(lambda x: cup_counts.get(x, 0))
    
    merged_df = pd.merge(new_df, team_data, on='Team')
    # Calculate Final Cups/Win
    merged_df['Final Cups/Win'] = merged_df['Final Cups'] / merged_df['Win'].apply(lambda x: max(1, x))
    merged_df['Final Cups/Win'] = merged_df['Final Cups/Win'].fillna(0)

    return merged_df 

def get_team_name(df, team_data):
    for index, row in df.iterrows():
        name = row['Name']
        for i, r in team_data.iterrows():
            if name == r['Player 1'] or name == r['Player 2']:
                df.at[index, 'Team'] = r['Team']
                break
    return df

def update_team_record(df, team_data):
    team_data['Win'] = 0
    team_data["Loss"] = 0
    for index, row in df.iterrows():
        final_score = df.iloc[index]['Final Score']
        if final_score[-1] == "*":
            winner = df.iloc[index]['Team 2']
            loser = df.iloc[index]['Team 1']
            team_data.loc[team_data['Team'] == winner, 'Win'] += 1
            team_data.loc[team_data['Team'] == loser, 'Loss'] += 1
        elif final_score[1] == "*" or final_score[0] == "0":
            winner = df.iloc[index]['Team 1']
            loser = df.iloc[index]['Team 2']
            team_data.loc[team_data['Team'] == winner, 'Win'] += 1
            team_data.loc[team_data['Team'] == loser, 'Loss'] += 1
        else:
            winner = df.iloc[index]['Team 2']
            loser = df.iloc[index]['Team 1']
            team_data.loc[team_data['Team'] == winner, 'Win'] += 1
            team_data.loc[team_data['Team'] == loser, 'Loss'] += 1

    team_data['Win Rate'] = (team_data['Win'] / (team_data['Win'] + team_data['Loss']) * 100).apply(lambda x: '{:.1f}%'.format(x))
    team_data = team_data.sort_values(by=['Win', 'Loss'], ascending=[False, True]).reset_index(drop=True)

    team_data.to_csv("team_data.csv", index=False)
    return team_data

def my_sort_key(df):
    # Define your own logic for sorting the dataframe
    # For example, sorting by the difference between Wins and Losses
    return df['Win'] - df['Loss']

def display_stats(data, x, y, title, xaxis, yaxis):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=x, y=y, data=data, ax=ax, order=data.sort_values(by=y, ascending=False)[x])
    ax.set_title(title, color='white')
    ax.set_xlabel(xaxis, color='white')
    ax.set_ylabel(yaxis, color='white')
    plt.xticks(rotation=90, color='white')

    # Add labels to the top of the bars
    for p in ax.patches:
        ax.annotate('{:.1f}'.format(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=11, color='black', xytext=(0, 5),
                    textcoords='offset points')

    # Change the background color of the plot
    fig.patch.set_facecolor('black')

    # Display plot in Streamlit app
    st.pyplot(fig)

# def cal_winning_margin()
