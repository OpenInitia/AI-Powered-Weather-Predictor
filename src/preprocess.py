import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data():
    df=pd.read_csv("weather_data.csv")
    df["timestamp"]=pd.to_datetime(df["timestamp"], unit="s")

    X=df[["temperature", "humidity", "pressure"]]
    y=df["temperature"].shift(-1)
    X=X[:-1]
    y=y[:-1]

    scaler=MinMaxScaler()
    X_scaled=scaler.fit_transform(X)
    return X_scaled, y, scaler
