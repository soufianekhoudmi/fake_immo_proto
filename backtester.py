from sklearn.model_selection import train_test_split

from src.etl import loaders
from src.models import benchmark, analysis, rf

CURATED_DATA_34_PATH = "data/curated_34.csv"
TEST_DATA_34_PATH = "data/test_34.csv"

target = "valeur_mc"
full_features = ["surface_reelle_bati", "nombre_pieces_principales", "longitude", "latitude"]
gps_features = ["longitude", "latitude"]

if __name__ == "__main__":

    curated_data_34 = loaders.extract_data(CURATED_DATA_34_PATH)

    data_train, data_test = train_test_split(
        curated_data_34, test_size=0.33, random_state=42)
    
    print(data_train.columns)

    # Compute benchmark predictions
    cp_mean_prediction = benchmark.compute_means_per_cp(data_train=data_train)
    # Append benchmark and compute errors
    data_test = data_test.merge(cp_mean_prediction, on="code_postal", how="left")
    data_test = analysis.compute_absolute_error(data=data_test, predicted_column="cp_mean_prediction")


    # Estimate full RF model
    full_rf_model = rf.fit_rf_model(data_train=data_train, features=full_features, target=target)
    # Compute full RF predictions
    rf_predictions = full_rf_model.predict(data_test[full_features])
    # Append benchmark and compute errors
    data_test['full_rf_predictions'] = rf_predictions
    data_test = analysis.compute_absolute_error(data=data_test, predicted_column="full_rf_predictions")



    # Estimate GPS rf model
    gps_rf_model = rf.fit_rf_model(data_train=data_train, features=gps_features, target=target)
    # Compute GPS rf predictions
    gps_predictions = gps_rf_model.predict(data_test[gps_features])
    # Append benchmark and compute errors
    data_test['gps_rf_predictions'] = rf_predictions
    data_test = analysis.compute_absolute_error(data=data_test, predicted_column="gps_rf_predictions")


    # save test_data with different predictions
    loaders.save_data(data_test, TEST_DATA_34_PATH)



