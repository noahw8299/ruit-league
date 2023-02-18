import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_entry import show_data_entry
from explore import show_explore_page
from add_new_user import show_new_user_page

def main():
    st.set_page_config(page_title="Ruit League 2023", page_icon=":trophy:", layout="wide")

    menu = ["Data Entry", "Add New Team", "Data Visualization"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Data Entry":
        show_data_entry()
    elif choice == "Add New Team":
        show_new_user_page()
    else:
        show_explore_page()

if __name__ == "__main__":
    main()
