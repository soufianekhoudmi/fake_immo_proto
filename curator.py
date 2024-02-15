import pandas as pd

from src.etl import filters, loaders, framers

RAW_DATA_34_PATH = "data/34.csv"
CURATED_DATA_34_PATH = "data/curated_34.csv"


def curate_data_pipeline(raw_data_path, curated_data_path):
    # Load data. 
    # TODO : Generalize name. For now keep it data_34 to make sur scope is clear
    data_34 = loaders.extract_data(raw_data_path)
    # Keep only sales
    data_34 = filters.filter_nature(data_34)
    # Keep only appartments
    data_34 = filters.filter_type(data_34)
    # Group per mutation
    data_34 = framers.group_per_mutation(data_34)
    # Compute price per sqm
    data_34 = framers.compute_price_per_sqm(data_34)
    # Filter abnormal transactions
    data_34 = filters.filter_abnormale(data_34)
    # Save curated
    loaders.save_data(data_34, curated_data_path)



if __name__ == "__main__":
    curate_data_pipeline(raw_data_path=RAW_DATA_34_PATH, curated_data_path=CURATED_DATA_34_PATH)