import streamlit as st
import pandas as pd
from Scout_player import find_and_plot_similar_players  

# Create a Streamlit app
st.title("Find Similar Players")


data_file = r"FInal_DF/wi.csv"  
player_df = pd.read_csv(data_file)
player_names = player_df['Player'].tolist()
player_name = st.sidebar.selectbox("Select a player:", player_names)


if player_name:
    similar_players, radar_plot = find_and_plot_similar_players(data_file, player_name)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Similar players:")
        st.write(similar_players['Player'])

    with col2:
        st.plotly_chart(radar_plot)
