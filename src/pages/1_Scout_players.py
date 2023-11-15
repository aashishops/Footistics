import streamlit as st
import pandas as pd
from Scout_player import find_and_plot_similar_players  
from abbrevation import fb, dm, gk, cm, am, striker, cb, wi, position_to_abbrevations

# Create a Streamlit app
st.title("Find Similar Players")
 
fb_df = pd.read_csv(r"FInal_DF/fb.csv")
dm_df = pd.read_csv(r"FInal_DF/dm.csv")
gk_df = pd.read_csv(r"FInal_DF/gk.csv")
cm_df = pd.read_csv(r"FInal_DF/cm.csv")
am_df = pd.read_csv(r"FInal_DF/am.csv")
striker_df = pd.read_csv(r"FInal_DF/strikers.csv")
cb_df = pd.read_csv(r"FInal_DF/cb.csv")
wi_df = pd.read_csv(r"FInal_DF/wi.csv")
ps_df = pd.read_csv(r"Web scrapping/Final Data/position.csv")

player_names = ps_df['Player'].tolist()
player_name = st.sidebar.selectbox("Select a player:", player_names)

position_to_df = {
    'Right-Back': fb_df,
    'Left-Back': fb_df,
    'Left WingBack': fb_df,
    'Right WingBack': fb_df,
    'Defensive Midfield': dm_df,
    'Goalkeeper': gk_df,
    'Central Midfield': cm_df,
    'Attacking Midfield': am_df,
    'Centre-Forward': striker_df,
    'Second Striker': striker_df,
    'Centre-Back': cb_df,
    'Right Winger': wi_df,
    'Left Winger': wi_df
}

player_position = ps_df.loc[ps_df["Player"] == player_name, "Position"].iloc[0]

abbreviation_dict = position_to_abbrevations.get(player_position, {})

if player_name:
    similar_players, radar_plot = find_and_plot_similar_players(position_to_df, player_name)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Similar players:")
        st.write(similar_players['Player'])

    with col2:
        st.plotly_chart(radar_plot)

    st.write(f"\nAbbreviations for {player_position}:\n")
    for key, value in abbreviation_dict.items():
        st.write(f"{key} - {value}")
