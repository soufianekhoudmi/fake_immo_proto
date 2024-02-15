"""
Operations that filter dataset with respect to :
- Abnormal (outliers, impact on model, etc)
- Scope (business, product, etc)
"""

ABNORMAL_FILTER = {
    "valeur_mc" : {"min": 500, "max": 8000},
    "surface_reelle_bati" : {"min": 10, "max": 200},
    "nombre_pieces_principales" : {"min": 1, "max": 10},

}



def filter_nature(data):
    """
    Keep only sales
    """
    mutation_mask = data["nature_mutation"] == "Vente"
    data = data[mutation_mask]
    return data


def filter_type(data):
    mutation_only_appartments = data.groupby("id_mutation")["type_local"].apply(lambda x: all([local == "Appartement" for local in list(x)]))
    mutation_only_appartments_ids = mutation_only_appartments[mutation_only_appartments].index
    data = data[data['id_mutation'].isin(mutation_only_appartments_ids)]
    return data


def filter_abnormale(data):
    """
    Filter abnormal or out of scope prices, surfaces and rooms 
    TODO : Make it smarter
    - ex : define business scope
    - ex : define abnormal price w.r.t to closest neighbors (KNN)
    - ex : define abnormal jointly abnormal rooms and area
    """

    valeur_mc_min = ABNORMAL_FILTER["valeur_mc"]["min"]
    valeur_mc_max = ABNORMAL_FILTER["valeur_mc"]["max"]

    surface_reelle_bati_min = ABNORMAL_FILTER["surface_reelle_bati"]["min"]
    surface_reelle_bati_max = ABNORMAL_FILTER["surface_reelle_bati"]["max"]

    nombre_pieces_principales_min = ABNORMAL_FILTER["nombre_pieces_principales"]["min"]
    nombre_pieces_principales_max = ABNORMAL_FILTER["nombre_pieces_principales"]["max"]

    # A loop would through dictionnary items would have been cleaner but nor readble
    filter_mask = \
        (data["valeur_mc"] <= valeur_mc_max ) & (data["valeur_mc"] >= valeur_mc_min ) \
        & (data["surface_reelle_bati"] <= surface_reelle_bati_max ) & (data["surface_reelle_bati"] >= surface_reelle_bati_min ) \
        & (data["nombre_pieces_principales"] <= nombre_pieces_principales_max ) & (data["nombre_pieces_principales"] >= nombre_pieces_principales_min )
    data = data[filter_mask]
    return data

