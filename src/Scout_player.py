import pandas as pd
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

def find_and_plot_similar_players(player_df, player_name, k=5):
    # Check if "Position" column exists in the DataFrame
    if "Position" in player_df.columns:
        # Drop the "Position" column
        player_df = player_df.drop("Position", axis=1, errors='ignore')
        player_df = player_df.drop("SDist", axis=1, errors='ignore')

    # Check if "Unnamed: 0" column exists in the DataFrame
    if "Unnamed: 0" in player_df.columns:
        # Drop the "Unnamed: 0" column
        player_df = player_df.drop("Unnamed: 0", axis=1, errors='ignore')

    # Exclude non-numeric columns like player names
    numeric_columns = player_df.select_dtypes(include=['number'])

    # Check if you have any missing values and handle them if needed
    numeric_columns.fillna(0, inplace=True)  # You can replace NaN values with zeros or handle them differently

    # Standardize the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(numeric_columns)

    # Choose the number of neighbors (k) - adjust this based on your preference
    knn_model = NearestNeighbors(n_neighbors=k, algorithm='auto', metric='euclidean')
    knn_model.fit(X_scaled)

    # Find the index of the player with the given name
    player_index = player_df[player_df['Player'] == player_name].index[0]

    # Replace 'query_player_index' with the index of the player you want to find similar players for
    query_player = [X_scaled[player_index]]
    distances, indices = knn_model.kneighbors(query_player)

    # 'indices' contains the indices of similar players, and 'distances' contains their distances
    similar_player_indices = indices[0]

    # You can then use these indices to retrieve the similar players from your original DataFrame
    similar_player_knn = player_df.iloc[similar_player_indices]

    # Plot the radar graph
    if 'Position' in similar_player_knn.columns and 'Unnamed: 0' in similar_player_knn.columns:
        # Exclude unnecessary columns
        similar_player_data = similar_player_knn.drop(columns=['Position', 'Unnamed: 0'])

        similar_player_comp = pd.melt(similar_player_data, id_vars=['Player'], value_vars=similar_player_data.columns[1:], var_name='Stat')
    else:
        # If 'Position' and 'Unnamed: 0' columns are not found, use the DataFrame as is
        similar_player_comp = pd.melt(similar_player_knn, id_vars=['Player'], value_vars=similar_player_knn.columns[1:], var_name='Stat')

    # Create a radar plot using Plotly Express
    fig = px.line_polar(similar_player_comp, r='value', theta='Stat', line_close=True, color='Player',
                        color_discrete_sequence=["#00eb93","#eb0093", "#4ed2ff","#9300eb","#eb9300"], template="plotly_dark")

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
    return similar_player_knn[['Player']], fig
