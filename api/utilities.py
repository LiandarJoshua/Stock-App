import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from datetime import date  # Import date module
import yfinance as yf  # Import yfinance module for downloading stock data
import pickle

def load_data(ticker):
    START = "2010-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

def preprocess_data(data):
    df = data.drop(['Date', 'Adj Close'], axis=1)
    train = pd.DataFrame(data[0:int(len(data)*0.70)])
    test = pd.DataFrame(data[int(len(data)*0.70):])
    
    scaler = MinMaxScaler(feature_range=(0,1))
    train_close = train.iloc[:, 4:5].values
    test_close = test.iloc[:, 4:5].values
    data_training_array = scaler.fit_transform(train_close)
    
    x_train, y_train = [], [] 
    for i in range(100, data_training_array.shape[0]):
        x_train.append(data_training_array[i-100: i])
        y_train.append(data_training_array[i, 0])
    x_train, y_train = np.array(x_train), np.array(y_train)
    
    return x_train, y_train, scaler, test_close

def train_model(x_train, y_train):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.LSTM(50, return_sequences=True, input_shape=(x_train.shape[1],1)))
    model.add(tf.keras.layers.LSTM(units=50))
    model.add(tf.keras.layers.Dense(50))
    model.add(tf.keras.layers.Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])
    model.fit(x_train, y_train, batch_size=64, epochs=100)
    return model

def predict_next_day(model, scaler, test_data):
    test_value = scaler.fit_transform(test_data[-100:].reshape(-1, 1))  # Use 100 time steps
    test = np.array([test_value])
    test = np.reshape(test, (test.shape[0], test.shape[1], 1))
    prediction = model.predict(test)
    tomorrow_prediction = scaler.inverse_transform(prediction)
    return tomorrow_prediction

def save_model(model, model_name):
    model.save(model_name + '.h5')
    
def main():
    # Define the ticker symbol for the stock data
    ticker = "AAPL"

    # Load data
    data = load_data(ticker)

    # Preprocess data
    x_train, y_train, scaler, test_close = preprocess_data(data)

    # Train model
    model = train_model(x_train, y_train)

    # Save model
    model_name = 'lstm_model'
    save_model(model, model_name)

    # Predict next day
    tomorrow_prediction = predict_next_day(model, scaler, test_close)
    print("Tomorrow's prediction:", tomorrow_prediction)

if __name__ == "__main__":
    main()

