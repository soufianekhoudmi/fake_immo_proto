import numpy as np


def compute_absolute_error(data, predicted_column):
    error_column = f"{predicted_column}_error"
    data[error_column] = np.abs(data[predicted_column] - data["valeur_mc"])/data["valeur_mc"]
    return data