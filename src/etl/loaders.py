"""
Connections with data
For now csv files in data/path
TODO : move this files to database, persist storage. No file should remain in repo
"""

import pandas as pd  




def extract_data(path):
    return pd.read_csv(path)

def save_data(data, path):
    data.to_csv(path, index=None)