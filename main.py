from flask import Flask, request, jsonify, render_template
import os
import tensorflow as tf
from src.model import train_and_save_model, predict_weather
from lib.openweather import fetch_weather_data

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

app = Flask(__name__)

# Step 1: Fetch the latest weather data
print("Fetching latest weather data...")
fetch_weather_data()

# Step 2: Check if the model exists, if not, train it
MODEL_PATH = "weather_model.h5"
if not os.path.exists(MODEL_PATH):
    print("Training model as no pre-trained model found...")
    train_and_save_model()
else:
    print("Pre-trained model found. Loading...")
    
# Step 3: Load the trained model
model = tf.keras.models.load_model(MODEL_PATH)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        temp = data["temperature"]
        humidity = data["humidity"]
        pressure = data["pressure"]
        prediction = predict_weather(temp, humidity, pressure)
        return jsonify({"predicted_temperature": round(prediction, 2)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
