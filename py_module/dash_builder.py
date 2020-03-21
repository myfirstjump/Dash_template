import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

class DashBuilder(object):
    
    ### 特色:
    # 0. Reference: https://dash.plot.ly/
    # 1. hot-reloading
    # 2. dash語法可直接轉換至html
    # 3. pandas dataframe可快速轉換成html table
    # 4. dcc.Graph renders interactive data visualizations, over 35 chart types
    # 5. 可以利用Markdown語法編寫html by dcc.Markdown

    def __init__(self):
        
        self.df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

        self.external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
        self.app = dash.Dash(__name__, external_stylesheets=self.external_stylesheets)
        self.colors = {
            'background': '#111111',
            'text': '#7FDBFF'
        }

        # html.H1即生成 <h1> </h1>格式的html物件
        # Children 屬性永遠都是第一個參數，故可省略
        # Components(例如H1) property(例如style) use camelCased寫法，例如'textAlign'
        self.app.layout = html.Div(
            style={'backgroundColor': self.colors['background']}, 
            children=[
                # 1. Head1
                html.H1(
                    children='Hello Dash',
                    style={
                        'textAlign': 'center',
                        'color': self.colors['text']
                    }
                ),
                # 2. Div 
                html.Div(
                    children='''Dash: A web application framework for Python.''', 
                    style={
                        'textAlign': 'center',
                        'color': self.colors['text']
                    }
                ),
                # 3. Div
                html.Div(
                    children=[
                        html.H4(children='US Agriculture Exports (2011)'),
                        generate_table(self.df)
                    ]
                ),

                # 4. dcc.Graph
                dcc.Graph( # dcc物件是可互動式圖表
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 0.5, 2], 'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'plot_bgcolor': self.colors['background'],
                            'paper_bgcolor': self.colors['background'],
                            'font': {
                                'color': self.colors['text']
                            }
                        }
                    }
                ),
                # 5. dcc.Graph
                dcc.Graph(
                    id='life-exp-vs-gdp',
                    figure={
                        'data': [
                            dict(
                                x=self.df[self.df['continent'] == i]['gdp per capita'],
                                y=self.df[self.df['continent'] == i]['life expectancy'],
                                text=self.df[self.df['continent'] == i]['country'],
                                mode='markers',
                                opacity=0.7,
                                marker={
                                    'size': 15,
                                    'line': {'width': 0.5, 'color': 'white'}
                                },
                                name=i
                            ) for i in self.df.continent.unique()
                        ],
                        'layout': dict(
                            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                            yaxis={'title': 'Life Expectancy'},
                            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                            legend={'x': 0, 'y': 1},
                            hovermode='closest'
                        )
                    }
                )
            ]   #   Children
        )   # </div>

        self.app.run_server(debug=True, dev_tools_hot_reload=True)

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])