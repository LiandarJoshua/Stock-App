import tensorflow as tf
from flask import Flask, jsonify, request, render_template
from utilities import load_data, preprocess_data, predict_next_day
import plotly.graph_objs as go  # Import Plotly for graph plotting

app = Flask(__name__)

# Specify the full path to the saved LSTM model
model_path = 'lstm_model.h5'
loaded_model = tf.keras.models.load_model(model_path)

@app.route('/')
def home():
    return render_template('stock.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        ticker = data['ticker']
    except KeyError:
        return jsonify({'error': 'Invalid input data. Make sure you provide "ticker".'}), 400
    
    # Load data and preprocess
    try:
        data = load_data(ticker)
        x_train, y_train, scaler, test_close = preprocess_data(data)
        closing_prices = data['Close'].tail(30).tolist()  # Extract last 30 days closing prices
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    # Preprocess the sample data and make predictions
    try:
        tomorrow_prediction = predict_next_day(loaded_model, scaler, test_close)
        return jsonify({'ticker': ticker, 'predictions': tomorrow_prediction.tolist(), 'closing_prices': closing_prices}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
