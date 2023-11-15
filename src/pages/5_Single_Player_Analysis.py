from comparison import single_player_comparison
import pandas as pd
import streamlit as st
from abbrevation import position_to_df

st.set_page_config(
    page_title="Footistcs",
    page_icon="⚽",
)


# Sample DataFrames and dictionary for testing
fb_df=pd.read_csv(r"FInal_DF/fb.csv")
dm_df=pd.read_csv(r"FInal_DF/dm.csv")
gk_df=pd.read_csv(r"FInal_DF/gk.csv")
cm_df=pd.read_csv(r"FInal_DF/cm.csv")
am_df=pd.read_csv(r"FInal_DF/am.csv")
striker_df=pd.read_csv(r"FInal_DF/strikers.csv")
cb_df=pd.read_csv(r"FInal_DF/cb.csv")
wi_df=pd.read_csv(r"FInal_DF/wi.csv")
ps_df=pd.read_csv(r"Web scrapping/Final Data/position.csv")
# Create a dictionary to map player positions to their respective DataFrames
st.title("Single Player Comparison")

player_names = ps_df["Player"].tolist()
with st.sidebar:
    player_name = st.selectbox("Select a player:", player_names)

# Get the player's position from the DataFrame
player_position = ps_df.loc[ps_df["Player"] == player_name, "Position"].iloc[0]

# Get the corresponding abbreviation dictionary for the player's position
abbreviation_dict = position_to_df.get(player_position, {})

# Print the abbreviation dictionary
st.write(f"Abbreviations for {player_position}:\n")
st.write(abbreviation_dict)

# Perform the rest of your code for single player comparison
fig = single_player_comparison(player_name, ps_df, position_to_df)
st.plotly_chart(fig)
