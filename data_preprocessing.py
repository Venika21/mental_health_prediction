# data_preprocessing.py

import pandas as pd

def load_and_preprocess_data():
    df = pd.read_csv('mental_health_data.csv')
    # Add cleaning, encoding etc. here
    return df
