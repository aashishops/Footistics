from comparison import single_player_comparison
import pandas as pd
import streamlit as st 
from abbrevation import fb_df,dm_df,gk_df,cm_df,am_df,striker_df,cb_df,wi_df
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


st.title("Single Player Comparison")

player_names = ps_df["Player"].tolist()
with st.sidebar:
    player_name = st.selectbox("Select a player:", player_names)

# Get the player's position from the DataFrame
player_position = ps_df.loc[ps_df["Player"] == player_name, "Position"].iloc[0]

# Get the corresponding abbreviation dictionary for the player's position
abbreviation_dict = position_to_df.get(player_position, {})


# Perform the rest of your code for single player comparison
fig = single_player_comparison(player_name, ps_df, position_to_df)
st.plotly_chart(fig)

# Print the abbreviation dictionary in a readable format
st.write(f"Abbreviations for {player_position}:\n")
for key, value in abbreviation_dict.items():
    st.write(f"{key} - {value}")
