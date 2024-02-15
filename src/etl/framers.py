"""
Shape data to format (keys, columns) of interest
"""


def group_per_mutation(data):
    """
    Get data for each mutation
    Sometimes each appartement is a bundle (so value attached to the bundle, not to an appartement)
    """
    data = data.groupby("id_mutation").agg({"valeur_fonciere": "sum", 
                                            "longitude": "min", 
                                            "latitude": "min",
                                            "nombre_pieces_principales": "sum", 
                                            "surface_reelle_bati": "sum",
                                            "code_postal": "min",
                                            "nom_commune": "min"})
    return data


def compute_price_per_sqm(data):
    """
    We use price per SQM in RE
    TODO : maybe better in enhancer module ?
    """
    data['valeur_mc'] = data['valeur_fonciere'] / data['surface_reelle_bati']
    return data