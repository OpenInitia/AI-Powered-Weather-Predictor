import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split
from src.preprocess import preprocess_data

def train_and_save_model():
    X, y, scaler = preprocess_data()
    X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)

    X_train_lstm=np.reshape(X_train,(X_train.shape[0], 1, X_train.shape[1]))
    X_test_lstm=np.reshape(X_test,(X_test.shape[0], 1, X_test.shape[1]))

    model=Sequential([
        LSTM(50, return_sequences=True, input_shape=(1, X_train.shape[1])),LSTM(50),Dense(1)
    ])

    model.compile(optimizer="adam", loss="mean_squared_error")
    model.fit(X_train_lstm, y_train, epochs=10, batch_size=16, validation_data=(X_test_lstm, y_test))

    model.save("weather_model.h5")
    print("Model trained and saved.")

def predict_weather(temp, humidity, pressure):
    model = tf.keras.models.load_model("weather_model.h5")
    _, _, scaler = preprocess_data()
    input_data = scaler.transform([[temp, humidity, pressure]])
    input_data = np.reshape(input_data, (1, 1, 3))
    predicted_temp = model.predict(input_data)
    return predicted_temp[0][0]
