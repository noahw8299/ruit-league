import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit import components

game_1 = pd.DataFrame({
    'Round 1': ["Free Palenstine", "Ur mum"]
})

game_2 = pd.DataFrame({
    'Round 1': ["Free Palenstine", "Ur mum"]
})


def show_tournament_page():
    st.write(game_1)
    st.write(game_2)






