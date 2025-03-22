from datetime import datetime, timedelta
from meteostat import Point, Daily
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def get_climate_data(lat, lon, start_year, end_year):
    location = Point(lat, lon)
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    
    data = Daily(location, start, end)
    df = data.fetch()
    
    return df

def prepare_data_for_ml(df):
    
    df['month'] = df.index.month
    df['day'] = df.index.day
    df['year'] = df.index.year
    
    
    features = ['month', 'day', 'year', 'tavg', 'tmin', 'tmax', 'prcp']
    target = 'tavg'
    
    X = df[features]
    y = df[target]
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
   
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


