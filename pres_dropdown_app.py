import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import pandas as pd

app = dash.Dash()

# app.scripts.config.serve_locally = True
# app.css.config.serve_locally = True

DF_PRES = pd.read_csv(
    'https://raw.githubusercontent.com/austinbrian/politics-dash/master/data/president_counties.csv'
)
clinton_counties= DF_PRES[DF_PRES['clinton'] > DF_PRES['trump']]
trump_counties = DF_PRES[DF_PRES['trump'] > DF_PRES['clinton']]
plurality_counties = DF_PRES[(DF_PRES['trump']/DF_PRES.total_votes < .5) & (DF_PRES['clinton']/DF_PRES.total_votes < .5)]

dataframes = {'CLINTON' : clinton_counties,
              'TRUMP'   : trump_counties,
              'PLURALITY': plurality_counties}


def get_data_object(user_selection):
    """
    For user selections, return the relevant in-memory data frame.
    """
    return dataframes[user_selection]


app.layout = html.Div([
    html.H4('DataTable'),
    html.Label('Report type:', style={'font-weight': 'bold'}),
    dcc.Dropdown(
        id='field-dropdown',
        options=[{'label': df, 'value': df} for df in dataframes],
        value='DF_GAPMINDER',
        clearable=False
    ),
    dt.DataTable(
        # Initialise the rows
        rows=[{}],
        row_selectable=True,
        filterable=True,
        sortable=True,
        selected_row_indices=[],
        id='table'
    ),
    html.Div(id='selected-indexes')
], className='container')


@app.callback(Output('table', 'rows'), [Input('field-dropdown', 'value')])
def update_table(user_selection):
    """
    For user selections, return the relevant table
    """
    df = get_data_object(user_selection)
    return df.to_dict('records')


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
