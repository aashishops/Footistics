import streamlit as st
from Top_players import top_players_table

st.set_page_config(
    page_title="Footistcs",
    page_icon="⚽",
)

st.title("Stats Center")

# File path to your CSV data
Top_charts_path = r'e:\2nd year\3rd sem\Data science\Project\FInal_DF\Topping_the_charts.csv'

# Create the Plotly figure
fig = top_players_table(Top_charts_path)

# Display the figure using Streamlit
st.plotly_chart(fig)