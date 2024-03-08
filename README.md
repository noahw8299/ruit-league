# Ruit League

Welcome to Ruit League, a web application developed for the Tufts Theta Chi Fraternity's 2023 season. This web application, hosted on AWS EC2 service, serves as a centralized platform for real-time input of game statistics and provides comprehensive player and team performance insights throughout the season. This project is currently not in use as the season has ended and I graduated Tufts in 2023. The web app can be accessed at the following IP address hosted by an AWS remote server: http://35.172.109.115:8501/

Context: 'Ruit League' is a brotherhood game help each semester for the brothers of Theta Chi. I built this app to help encourage members of the Fraternity to participate as well as to facilinate friendly competition over the course of the semester. The results were amazing as during this season as member engagement improved by 70%.

## Important Note
All current data and stats are a real reflection of user input from the 2023 season. There is currently no system in place to handle the creation of new seasons or to delete the current data unless done on the backend. Please keep this in mind when playing around with the application.


## Features

### Real-time Game Stats Input

The `Data_entry.py` module facilitates real-time data entry for Ruit League. Leveraging Streamlit for an intuitive user interface, users can input game statistics as they happen. The data is validated and organized, ensuring accuracy and consistency in the recorded information. The final data is stored in the `ruit_league_data.csv` file.

### Comprehensive Player and Team Statistics

The `explore.py` module provides users with detailed statistical insights. Utilizing Seaborn and Matplotlib, this module visualizes key metrics, such as total cups, average cups per game, final cups hit per win, and total final cups. The presentation is user-friendly and offers a holistic view of player and team performance over time.

### New Team and Player Addition

The `add_new_user.py` module allows for the dynamic addition of new teams and players to the system. Users can input team names and player information, updating the `team_data.csv` file seamlessly. This feature ensures the application remains flexible and adaptable to changes in team composition.

## Technologies Used

This project leverages the following technologies:

- **Streamlit:** For creating an interactive and user-friendly web application.
- **Pandas:** For data manipulation and management.
- **Matplotlib and Seaborn:** For data visualization, offering insights into player and team performance.
- **DateTime:** For capturing and formatting timestamps.
- **Boto3:** For seamless integration with AWS services.

## Usage

To access the application, visit [Ruit League Web App](http://35.172.109.115:8501/). The application is developed using Python and is hosted on AWS services.

## Contribution

If you are interested in contributing to the project, please reach out to the developers for guidance on how to get involved.

## Dependencies

- Python 3.7 or above

## Getting Started

To start working on the project locally, ensure you have Python 3.7 or above installed on your machine. Clone the repository, and execute the `app.py` script to run the application.

## Code Structure

### `Data_entry.py`

This module facilitates real-time data entry for Ruit League. It utilizes Streamlit for the user interface, Pandas for data manipulation, and Boto3 for AWS integration. The data is organized, validated, and stored in a CSV file (`ruit_league_data.csv`).

### `explore.py`

The `explore.py` module is responsible for presenting comprehensive statistical insights. It uses Seaborn and Matplotlib for data visualization and integrates with the existing data stored in `ruit_league_data.csv`.

### `add_new_user.py`

This module allows the addition of new teams and players to the system. The user can input team names and player information, and the data is updated in the `team_data.csv` file.
