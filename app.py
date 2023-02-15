import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_entry import show_data_entry
from explore import show_explore_page

def main():
    st.set_page_config(page_title="Ruit League 2023", page_icon=":trophy:", layout="wide")

    menu = ["Data Entry", "Data Visualization"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Data Entry":
        show_data_entry()
    else:
        show_explore_page()

if __name__ == "__main__":
    main()
