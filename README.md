# AI-Powered-Weather-Predictor
A LSTM model based AI-Powered Weather Predictor

### Maintainer - @Deadpool2000

This project is an AI-powered weather prediction system that fetches real-time weather data using the OpenWeatherMap API and predicts future temperatures using an **LSTM (Long Short-Term Memory) neural network**.

## 🚀 Features
- Fetches real-time weather data from OpenWeatherMap API 🌍  
- Trains an **LSTM-based deep learning model** for temperature prediction 🔥  
- Provides weather predictions via a **Flask API** 🖥️  
- Stores trained models for faster inference ⚡  
- Fully modular **directory structure** 🏗️  

---

## 📁 Project Directory Structure

```
weather-predictor/
│── lib/                         # External helper functions
│   ├── openweather.py            # Fetch weather data from OpenWeatherMap API
│
│── src/                         # Core logic of the project
│   ├── model.py                  # LSTM model training and prediction
│   ├── preprocess.py             # Data preprocessing
│
│── templates/                    # HTML templates (for Flask UI)
│   ├── index.html                 # Frontend UI (Optional)
│
│── static/                        # Static files (CSS, JS, Images)
│
│── main.py                        # Flask app (Runs API & triggers training)
│── requirements.txt                # Python dependencies
│── README.md                       # Project documentation
```

---

## 🔧 Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/weather-predictor.git
cd weather-predictor
```

### 2️⃣ **Set Up a Virtual Environment**
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Set Up OpenWeatherMap API Key**
1. Get your API key from [OpenWeatherMap](https://openweathermap.org/api)  
2. Create a `.env` file in the root directory:
   ```ini
   OPENWEATHER_API_KEY=your_api_key_here
   ```

---

## 🎯 Running the Project

### **1️⃣ Run the Flask Server**
```bash
python main.py
```
- This will:
  ✅ **Fetch the latest weather data**  
  ✅ **Train the model (if not already trained)**  
  ✅ **Start the Flask server at** `http://127.0.0.1:5000/`  

### **2️⃣ Predict Weather via API**
Send a POST request with JSON data:
```bash
curl -X POST http://127.0.0.1:5000/predict      -H "Content-Type: application/json"      -d '{"temperature": 30, "humidity": 70, "pressure": 1013}'
```
✅ **Response Example:**
```json
{
  "predicted_temperature": 31.2
}
```

---

## 📌 API Endpoints

| **Endpoint**    | **Method** | **Description**                         |
|----------------|-----------|-----------------------------------------|
| `/`            | GET       | Returns the homepage (Optional UI)     |
| `/predict`     | POST      | Predicts the future temperature based on inputs |

---

## 🛠️ Technologies Used
- **Flask** - Web framework for API development  
- **TensorFlow/Keras** - LSTM-based machine learning model  
- **Scikit-learn** - Data preprocessing  
- **NumPy & Pandas** - Data handling  
- **Requests** - Fetching weather data from OpenWeatherMap  

---

## 🌟 Future Improvements
- ✅ Add support for predicting **rainfall & wind speed** 🌧️  
- ✅ Deploy on a cloud platform like **AWS / Heroku** ☁️  
- ✅ Improve **UI with charts** 📊  

---

## 🤝 Contributing
Feel free to fork this project and submit a pull request!  
If you find any bugs, open an issue. 🚀  

---
