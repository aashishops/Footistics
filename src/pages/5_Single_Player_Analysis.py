from comparison import single_player_comparison
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Footistcs",
    page_icon="⚽",
)


# Sample DataFrames and dictionary for testing
fb_df=pd.read_csv(r"E:\2nd year\3rd sem\Data science\Project\FInal_DF\fb.csv")
dm_df=pd.read_csv(r"E:\2nd year\3rd sem\Data science\Project\FInal_DF\dm.csv")
gk_df=pd.read_csv(r"E:\2nd year\3rd sem\Data science\Project\FInal_DF\gk.csv")
cm_df=pd.read_csv(r"E:\2nd year\3rd sem\Data science\Project\FInal_DF\cm.csv")
am_df=pd.read_csv(r"E:\2nd year\3rd sem\Data science\Project\FInal_DF\am.csv")
striker_df=pd.read_csv(r"E:\2nd year\3rd sem\Data science\Project\FInal_DF\strikers.csv")
cb_df=pd.read_csv(r"E:\2nd year\3rd sem\Data science\Project\FInal_DF\cb.csv")
wi_df=pd.read_csv(r"E:\2nd year\3rd sem\Data science\Project\FInal_DF\wi.csv")
ps_df=pd.read_csv(r"E:\2nd year\3rd sem\Data science\Project\2022_2023 Top 5 leagues Data\position.csv")
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

fig = single_player_comparison(player_name, ps_df, position_to_df)
st.plotly_chart(fig)