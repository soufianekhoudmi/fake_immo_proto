from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor


def define_rf_model():
    model = GridSearchCV(estimator=RandomForestRegressor(n_estimators=1000, random_state=42),
                         scoring='neg_root_mean_squared_error',
                         param_grid={'min_samples_leaf': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    return model


def fit_rf_model(data_train, features, target):
    model = define_rf_model()
    fitted_model = model.fit(data_train[features], data_train[target])
    return fitted_model