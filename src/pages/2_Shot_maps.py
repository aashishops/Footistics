import pandas as pd
from copy import deepcopy
import matplotlib.pyplot as plt
import streamlit as st
from Shot_map import create_full_pitch, plot_scatterplot, plot_kdeplot

# Load your shot data here
shots_df = pd.read_csv(r'FInal_DF/player_shots2022_2023.csv')

pitch_width = 105  
pitch_length = 68  
background_color = "#0E1117"  
line_color = "white"  
line_width = 2.0  

x_lims = [0, 1.15]
y_lims = [0, 0.74]

x_mid = x_lims[1] / 2
y_mid = y_lims[1] / 2

full_pitch_shots_df = deepcopy(shots_df)
full_pitch_shots_df["X"] = full_pitch_shots_df["X"].multiply(x_lims[1])
full_pitch_shots_df["Y"] = full_pitch_shots_df["Y"].multiply(y_lims[1])

# Create a list of unique players from your data
players = full_pitch_shots_df["player"].unique()

# Use st.sidebar.selectbox to place it in the sidebar
selected_player = st.sidebar.selectbox("Select a player:", players)

st.title("Football Pitch Visualizations")

# Create the pitch
ax = create_full_pitch(x_lims, y_lims, background_color="#0E1117", line_color="white", line_width=2.0)
st.pyplot(plt)
# Plot scatterplot for the selected player
plot_scatterplot(ax, full_pitch_shots_df, selected_player)

# Display the scatterplot in Streamlit
st.pyplot(plt)

ax = create_full_pitch(x_lims, y_lims, background_color="#0E1117", line_color="white", line_width=2.0)
st.pyplot(plt)
# Create a new pitch
ax = create_full_pitch(x_lims, y_lims, background_color="#0E1117", line_color="white", line_width=2.)

# Plot kdeplot for the selected player
plot_kdeplot(ax,full_pitch_shots_df, selected_player)



st.pyplot(plt)
