import plotly.express as px
import pandas as pd
import streamlit as st

def single_player_comparison(player_name, ps_df, position_to_df):
    # Search for the player's position in ps_df
    player_data = ps_df[ps_df['Player'] == player_name]

    if not player_data.empty:
        player_position = player_data['Position'].values[0]

        # Check if the player's position exists in the dictionary
        if player_position in position_to_df:
            player_df = position_to_df[player_position]

            # Extract the player's data from the position-specific DataFrame
            player_data = player_df[player_df['Player'] == player_name]

            if not player_data.empty:
                player_data = player_data.drop(columns=['Position', 'Unnamed: 0', '90s'])  # Exclude unnecessary columns

               

                # Print the DataFrame
                st.write(player_data)

                player_comp = pd.melt(player_data, id_vars=['Player'], value_vars=player_data.columns[1:], var_name='Stat')

                # Create a radar plot using Plotly Express
                fig = px.line_polar(player_comp, r='value', theta='Stat', line_close=True, color='Player',
                                    color_discrete_sequence=["#4ed2ff"], template="plotly_dark")

                # Customize the layout
                fig.update_polars(
                    angularaxis_showgrid=False,
                    radialaxis_gridwidth=0,
                    gridshape='linear',
                    bgcolor="#494b5a",
                    radialaxis_showticklabels=False
                )

                fig.update_layout(
                    paper_bgcolor="rgba(0, 0, 0, 0)",
                    plot_bgcolor="rgba(0, 0, 0, 0)"
                )

                # Fill the area under the radar lines
                fig.update_traces(fill='toself')

                # Show the radar plot
                return fig

def player_vs_player_comparison(player1_name, player2_name, ps_df, position_to_df):
    # Search for the positions of both players in ps_df
    player1_data = ps_df[ps_df['Player'] == player1_name]
    player2_data = ps_df[ps_df['Player'] == player2_name]

    if not player1_data.empty and not player2_data.empty:
        player1_position = player1_data['Position'].values[0]
        player2_position = player2_data['Position'].values[0]

        # Check if the positions of both players are the same
        if player1_position == player2_position:
            if player1_position in position_to_df:
                player_df = position_to_df[player1_position]

                # Extract the data for both players from the position-specific DataFrame
                player1_data = player_df[player_df['Player'] == player1_name]
                player2_data = player_df[player_df['Player'] == player2_name]

                if not player1_data.empty and not player2_data.empty:
                    # Exclude unnecessary columns
                    player1_data = player1_data.drop(columns=['Position', 'Unnamed: 0','90s'])
                    player2_data = player2_data.drop(columns=['Position', 'Unnamed: 0','90s'])
                    player_data = pd.concat([player1_data, player2_data], ignore_index=True)
                    st.write(player_data)

                   
                    

                    # Melt the data for both players to create a DataFrame suitable for plotting
                    player_comp = pd.melt(player_data, id_vars=['Player'], value_vars=player1_data.columns[1:], var_name='Stat')

                    # Create radar plots for both players using Plotly Express
                    fig = px.line_polar(player_comp, r='value', theta='Stat', line_close=True, color='Player',
                                        color_discrete_sequence=["#f7ff00", "#eb0093"], template="plotly_dark",
                                        title=f"{player1_name} vs. {player2_name} Comparison")

                    # Customize the layout
                    fig.update_polars(
                        angularaxis_showgrid=False,
                        radialaxis_gridwidth=0,
                        gridshape='linear',
                        bgcolor="#494b5a",
                        radialaxis_showticklabels=False
                    )

                    fig.update_layout(
                        paper_bgcolor="rgba(0, 0, 0, 0)",
                        plot_bgcolor="rgba(0, 0, 0, 0)"
                    )

                    # Fill the area under the radar lines
                    fig.update_traces(fill='toself')

                    # Show the radar plot
                    return fig
