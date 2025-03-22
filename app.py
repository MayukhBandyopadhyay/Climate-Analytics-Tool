from flask import Flask, render_template, request,jsonify,url_for
from data_collection import get_climate_data, prepare_data_for_ml
from ml_model import train_model, predict_future
from visualization import plot_climate_indicators, plot_precipitation
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lat = float(request.form['latitude'])
        lon = float(request.form['longitude'])
        start_year = int(request.form['start_year'])
        end_year = int(request.form['end_year'])
        
        df = get_climate_data(lat, lon, start_year, end_year)
        X_train_scaled, X_test_scaled, y_train, y_test, scaler = prepare_data_for_ml(df)
        
        model = train_model(X_train_scaled, y_train)
        
        future_dates = pd.date_range(start=df.index[-1] + timedelta(days=1), periods=365)
        predictions = predict_future(model, scaler, future_dates)
        
        plot_climate_indicators(df, predictions)
        plot_precipitation(df)
        
        return render_template('results.html')
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
