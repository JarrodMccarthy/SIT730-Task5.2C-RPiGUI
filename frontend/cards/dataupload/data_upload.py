import dash_bootstrap_components as dbc
import dash_html_components as html

class DataUploadCard:
    def __init_(self):
        self.file_name = None
        self.file_size = None
    
    def get_card(self):
        return html.Div(
            [
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("50% width card", className="card-title"),
                            html.P(
                                [
                                    "This card uses the ",
                                    html.Code("w-50"),
                                    " class to set the width to 50%",
                                ],
                                className="card-text",
                            ),
                        ]
                    ),
                    className="w-50",
                ),
            ]
        )