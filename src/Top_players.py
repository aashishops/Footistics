import plotly.graph_objects as go
import pandas as pd

def top_players_table(data_path):
    # Read the data from the CSV file
    data = pd.read_csv(data_path)

    # Define the list of parameters and their corresponding desired labels
    parameter_labels = {
        'MP': 'Matches Played',
        'Min': 'Minutes',
        'Gls': 'Goals',
        'Ast': 'Assists',
        'xG': 'Expected Goals',
        'Saves': 'Saves',
        'CS': 'Clean Sheet',
        'CStp': 'Crosses Stopped',
        'SwOPA': "Sweeping Actions",
        'NPxG+xAG': 'Non-Penalty xG+xA',
        'LFTP': 'Passes Into Final Third',
        'LCrsPA': 'Crosses into Penalty Area',
        'LPrgP': 'Progressive Passes',
        'SCA': 'Shot-Creating Actions',
        'GCA': 'Goal-Creating Actions',
        'BInt': 'Ball Interceptions',
        'BTklInt': 'Successful Tackles+Interceptions',
        'BClr': 'Blocks and Clearances',
        'CTkl': 'Successful Tackles',
        'TOSucc': 'Take-Ons Successful'
    }

    # Create subplots (5 rows, 4 columns)
    fig = go.Figure()

    for i, param in enumerate(parameter_labels.keys(), start=1):
        top_5_players = data.nlargest(5, param)  # Select the top 5 players for the current parameter
        fig.add_trace(go.Table(
            header=dict(values=['Player', parameter_labels[param]],  # Use the label from the dictionary
                        fill_color='rgba(0, 0, 0, 0)',  # Change to your preferred dark mode color
                        font=dict(color='white'),  # Change font color to white
                        align='center'),
            cells=dict(values=[top_5_players['Player'], top_5_players[param]],
                       fill_color="rgba(0, 0, 0, 0)",  # Change to your preferred dark mode color
                       font=dict(color='white'),  # Change font color to white
                       align='center'),
            domain=dict(row=(i - 1) // 4, column=(i - 1) % 4)))

    # Update layout for better formatting
    fig.update_layout(
        height=1500,  # Increase the height to accommodate the extra row
        width=1200,
        showlegend=False,
        grid=dict(rows=5, columns=4, pattern='independent'),  # Change to 5 rows, 4 columns
        plot_bgcolor="rgba(0, 0, 0, 0)",  # Set the plot background color to black for dark mode
    )

    return fig


