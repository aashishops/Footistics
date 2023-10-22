import json
import pandas as pd
from copy import deepcopy
from bs4 import BeautifulSoup
from urllib.request import urlopen
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import streamlit as st
from Shot_map import create_full_pitch, plot_scatterplot, plot_kdeplot

# Load your shot data here
shots_df = pd.read_csv(r'E:\2nd year\3rd sem\Data science\Project\FInal_DF\Shots.csv')

x_lims = [0, 1.15]
y_lims = [0, 0.74]

x_mid = x_lims[1] / 2
y_mid = y_lims[1] / 2

background_color = "#1B1B1A"
line_color = "white"
line_width = 2.

full_pitch_shots_df = deepcopy(shots_df)
full_pitch_shots_df["X"] = full_pitch_shots_df["X"].multiply(x_lims[1])
full_pitch_shots_df["Y"] = full_pitch_shots_df["Y"].multiply(y_lims[1])

# Create a list of unique players from your data
players = full_pitch_shots_df["player"].unique()

# Use st.sidebar.selectbox to place it in the sidebar
selected_player = st.sidebar.selectbox("Select a player:", players)

st.title("Football Pitch Visualizations")

# Create the pitch
ax = create_full_pitch(x_lims, y_lims)

# Plot scatterplot for the selected player
plot_scatterplot(ax, full_pitch_shots_df, selected_player)

# Display the scatterplot in Streamlit
st.pyplot(plt)

# Create a new pitch
ax = create_full_pitch(x_lims, y_lims)

# Plot kdeplot for the selected player
plot_kdeplot(ax, full_pitch_shots_df, selected_player)

# Display the kdeplot in Streamlit
st.pyplot(plt)
