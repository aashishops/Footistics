import streamlit as st
import pandas as pd
from Scout_player import find_and_plot_similar_players  # Replace 'your_module' with the actual name of the module where you defined the functions

# Create a Streamlit app
st.title("Find Similar Players")

# Sidebar to select the player's name from a dropdown box
data_file = r"E:\2nd year\3rd sem\Data science\Project\FInal_DF\am.csv"  # Replace with the actual path to your data file
player_df = pd.read_csv(data_file)
player_names = player_df['Player'].tolist()
player_name = st.sidebar.selectbox("Select a player:", player_names)

# Button to trigger the search and radar plot comparison
if player_name:
    similar_players, radar_plot = find_and_plot_similar_players(data_file, player_name)
    # st.write(similar_players['Player'])  # Display only the names of similar players

    # Display the radar plot to the right of the similar player names
    col1, col2 = st.columns(2)
    with col1:
        st.write("Similar players:")
        st.write(similar_players['Player'])

    with col2:
        st.plotly_chart(radar_plot)
