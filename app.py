import ssl
import pickle 

import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from geopy.geocoders import Nominatim
import certifi


TRAINED_MODEL_34_PATH = "data/model_34"
full_rf_model = pickle.load(open(TRAINED_MODEL_34_PATH, 'rb'))

# Initialize the Dash app
app = dash.Dash(__name__)


def get_lat_lon(address):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    geolocator = Nominatim(user_agent="geoapiExercises", ssl_context=ssl_context)
    location = geolocator.geocode(address)
    if location:
        return (location.latitude, location.longitude)
    else:
        return (None, None)

# App layout
app.layout = html.Div([
    dcc.Input(id='address', type='text', placeholder='Addresse'),
    dcc.Input(id='surface', type='text', placeholder='Surface'),
    dcc.Input(id='rooms', type='number', placeholder='Nb Pièces'),
    html.Button('Prédire le prix', id='predict', n_clicks=0),
    html.Div(id='output')
])

# Callback to update output
@app.callback(
    Output('output', 'children'),
    [Input('predict', 'n_clicks')],
    [Input('address', 'value'), Input('surface', 'value'), Input('rooms', 'value')]
)
def update_output(n_clicks, address, surface, rooms):
    if n_clicks > 0:
        lat, lon = get_lat_lon(address)
        if lat is not None and lon is not None:
            # full_features = ["surface_reelle_bati", "nombre_pieces_principales", "longitude", "latitude"]

            predicted_price = full_rf_model.predict([[float(surface), int(rooms), lon, lat]])
            property_price = float(surface) * predicted_price[0]
            return f'Prix estimé: {property_price:,.2f}'
        else:
            return 'Adresse introuvable, réessayez.'
    return 'Entrez les caractéristiques du bien et prédisez.'

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
