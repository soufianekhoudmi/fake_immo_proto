import pickle

from src.models import rf
from src.etl import loaders

CURATED_DATA_34_PATH = "data/curated_34.csv"
TRAINED_MODEL_34_PATH = "data/model_34"

target = "valeur_mc"
full_features = ["surface_reelle_bati", "nombre_pieces_principales", "longitude", "latitude"]

curated_data_34 = loaders.extract_data(CURATED_DATA_34_PATH)

# We dont split here, we train on all the data
full_rf_model = rf.fit_rf_model(data_train=curated_data_34, features=full_features, target=target)
pickle.dump(full_rf_model, open(TRAINED_MODEL_34_PATH, 'wb'))
