import streamlit as st

# Set the title of the page
st.title("Ruit League 2023")

# Get the names of the two teams and split them by a comma
team_names = st.text_input("Enter the names of the two teams separated by a comma:").split(',')

if len(team_names) < 2:
    st.error("Please enter the names of two teams separated by a comma.")
else:
    # Get the final score of the game
    final_score = st.text_input("Enter the final score (e.g. 1 - 0)")

    # Check if there was overtime
    ot = st.checkbox("Was there overtime?")

    # Get the name and number of cups hit by the first player on team 1
    player_1_name = st.text_input("Enter the name of the first player for {}".format(team_names[0]), key='player_1_name')
    player_1_cups = st.text_input("How many cups did {} hit?".format(player_1_name), key='player_1_cups')

    # Get the name and number of cups hit by the second player on team 1
    player_2_name = st.text_input("Enter the name of the second player for {}".format(team_names[0]), key='player_2_name')
    player_2_cups = st.text_input("How many cups did {} hit?".format(player_2_name), key='player_2_cups')

    # Get the name and number of cups hit by the third player on team 1
    player_3_name = st.text_input("Enter the name of the first player for {}".format(team_names[1]), key='player_3_name')
    player_3_cups = st.text_input("How many cups did {} hit?".format(player_3_name), key='player_3_cups')

    # Get the name and number of cups hit by the fourth player on team 1
    player_4_name = st.text_input("Enter the name of the second player for {}".format(team_names[1]), key='player_4_name')
    player_4_cups = st.text_input("How many cups did {} hit?".format(player_4_name), key='player_4_cups')


    # Get the name of the player who hit the final cup
    final_cup = st.text_input("Who hit the final cup?")

    # Calculate the total number of cups hit by each team
    team_1_cups = int(player_1_cups) + int(player_2_cups)
    team_2_cups = int(player_3_cups) + int(player_4_cups)

    # Check if the total number of remaining cups equals 12
    if int(final_score.split(' - ')[0]) + int(final_score.split(' - ')[1]) != 12:
        st.error("The total number of remaining cups must add up to 12.")

    # Check if the total number of cups hit by team 1 equals 12 minus their final score
    if team_1_cups != 12 - int(final_score.split(' - ')[0]):
        st.error("The total number of cups hit by {} players must equal 12 - their final score.".format(team_names[0]))

    if team_2_cups != 12 - int(final_score.split(' - ')[1]):
        st.error("The total number of cups hit by {} players must equal 12 - their final score.".format(team_names[1]))

    # st.write("The game was played between {} and {}".format(team_names[0], team_names[1]))
    # st.write("Final Score: {}".format(final_score))
    # st.write("Overtime: {}".format(ot))
    # st.write("{} hit {} cups".format(player_1_name, player_1_cups))
    # st.write("{} hit {} cups".format(player_2_name, player_2_cups))
    # st.write("{} hit {} cups".format(player_3_name, player_3_cups))
    # st.write("{} hit {} cups".format(player_4_name, player_4_cups))
    # st.write("The final cup was hit by {}".format(final_cup))

