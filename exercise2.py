# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.

# Data used in visualization
app = dash.Dash(__name__, static_folder='static')
file = pd.read_csv('static/cereal.csv')

app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='Sugar in Each Serving of Cereal'),

    # set the description underneath the heading
    html.Div(children='''
        A demo to show the amount of sugar in a serving of cereal
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                go.Scatter(
                    x=file['cups'],
                    y=file['sugars'],
                    mode='markers',
                    text=file['name'],  # This line sets the cereal name as the points' labels.
                    marker={
                        'size': 10,
                        'color': 'red',
                        'opacity': 0.7
                    }
                )
            ],
            'layout': {
                'title': 'Sugar in a Serving of Cereal',
                'xaxis': {'title': 'Cups'},
                'yaxis': {'title': 'Sugars'},
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)


