
import dash_html_components as html
import dash_table
from datetime import timedelta, datetime
import pandas as pd


def string_date_to_datetime(date_str, sep='/'):
    dmy = date_str.split(sep)
    dt = datetime(int(dmy[2]), int(dmy[1]), int(dmy[0]), 0, 0)
    return dt

def get_days(date_to_check):
    date_dt = string_date_to_datetime(date_to_check)
    days_diff = (date_dt - datetime.today()).days
    return days_diff
    
def make_dash_table(df):
    table = dash_table.DataTable(
        id='table', 
        data=df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns if i != 'id'],#columns=[{"name": i, "id": i} for i in df.columns],
        sort_action='native',
        style_header={
            'backgroundColor': 'darkcyan',
            'color': 'white'
        },
        editable=True,
        export_format="xlsx",
        export_headers="display",
        #page_size=15
    )
    return table
