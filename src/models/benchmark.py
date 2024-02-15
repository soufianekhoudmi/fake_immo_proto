"""
Compute prediction using mean per postal codes
"""


def compute_means_per_cp(data_train):

    cp_mean_prediction = data_train.groupby('code_postal')['valeur_mc'].mean().to_frame()\
        .rename(columns={'valeur_mc': 'cp_mean_prediction'})
    
    return cp_mean_prediction