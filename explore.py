import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_explore_page():
    # load the data from the file
    df = pd.read_csv('ruit_league_data.csv')

    st.write("Player Data:", df)

    player_stats = summarize_player_stats(df)
    team_stats = summarize_player_stats(df)

    # Set the style and color palette
    sns.set_style('darkgrid')
    # sns.set_palette('dark', color_codes=True)

    col1, col2 = st.columns(2)

    # with col1:
        # Create bar plot of cups hit for each player
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Name', y='Total Cups', data=player_stats, ax=ax)
    ax.set_title('Total Cups Hit by Player', color='white')
    ax.set_xlabel('Player', color='white')
    ax.set_ylabel('Total Cups', color='white')
    plt.xticks(rotation=90, color='white')

    # Add labels to the top of the bars
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=11, color='black', xytext=(0, 5),
                    textcoords='offset points')
    # Change the background color of the plot
    fig.patch.set_facecolor('black')
    # Display plot in Streamlit app
    st.pyplot(fig)

    # with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Name', y='Cups/Game', data=player_stats, ax=ax)
    ax.set_title('Average Cup Hit by Player per Game', color='white')
    ax.set_xlabel('Player', color='white')
    ax.set_ylabel('Cups per Game', color='white')
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




def summarize_player_stats(df):
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

    
    return new_df  

def summarize_team_stats(df):
    team_names = set(df[['Team 1', 'Team 2']].values.flatten())
    st.write(team_names)