import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import os

def plot_climate_indicators(df, predictions=None):
    
    os.makedirs('static', exist_ok=True)
    
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['tavg'], label='Average Temperature')
    plt.title('Average Temperature Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(os.getcwd(), 'static', 'avg_temp_plot.png'))
    plt.close()
    
    
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['tmin'], label='Minimum Temperature')
    plt.title('Minimum Temperature Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(os.getcwd(), 'static', 'min_temp_plot.png'))
    plt.close()
    
    
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['tmax'], label='Maximum Temperature')
    plt.title('Maximum Temperature Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(os.getcwd(), 'static', 'max_temp_plot.png'))
    plt.close()
    
    
    if predictions is not None:
        future_dates = pd.date_range(start=df.index[-1] + timedelta(days=1), periods=len(predictions))
        plt.figure(figsize=(12, 6))
        plt.plot(future_dates, predictions, label='Predicted Average Temperature')
        plt.title('Predicted Average Temperature')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(os.getcwd(), 'static', 'predicted_temp_plot.png'))
        plt.close()

def plot_precipitation(df):
    plt.figure(figsize=(12, 6))
    
    plt.bar(df.index, df['prcp'], label='Precipitation')
    
    plt.title('Precipitation Over Time')
    plt.xlabel('Date')
    plt.ylabel('Precipitation (mm)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('static/precipitation_plot.png')
    plt.close()
