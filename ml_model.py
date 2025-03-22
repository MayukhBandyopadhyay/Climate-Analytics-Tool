from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    return rmse

def predict_future(model, scaler, future_dates):
    future_features = pd.DataFrame({
        'month': future_dates.month,
        'day': future_dates.day,
        'year': future_dates.year,
        'tavg': np.nan,
        'tmin': np.nan,
        'tmax': np.nan,
        'prcp': np.nan
    })
    
    future_features_scaled = scaler.transform(future_features)
    predictions = model.predict(future_features_scaled)
    
    return predictions
