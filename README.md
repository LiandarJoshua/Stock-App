
# Realtime Stock Prediction

Utilizes machine learning and deep learning models and implements it into a flask api. The model takes the company ticker as input and displays the predicted closing price for the next day.


## About LSTM
Long Term Short Term Memory Algorithm:

Long Short-Term Memory (LSTM) is a type of recurrent neural network (RNN) architecture designed to overcome the limitations of traditional RNNs in capturing long-term dependencies in sequential data. It was introduced by Hochreiter & Schmidhuber in 1997.
The key feature of LSTM networks is their ability to maintain a "memory" of previous inputs over long sequences, allowing them to effectively learn and remember patterns in sequential data. This is achieved through the use of special units called "memory cells," which have three gates: input gate, forget gate, and output gate. These gates control the flow of information into and out of the memory cell, allowing the LSTM to selectively retain or discard information based on its relevance to the current task.
LSTMs have been widely used in various applications such as natural language processing, speech recognition, time series prediction, and more, where modeling temporal dependencies is crucial. They have shown superior performance compared to traditional RNNs in tasks involving long sequences or complex patterns, making them a popular choice for sequential data modeling.
## Introduction
The project uses a flask api web application which serves as a frontend and a trained lstm deep learning model as the backend to predict the price for the next day.
## Setup
## File Overview
-app.py:Contains the flask application code

-utilities.py:Includes functions for loading data,preprocessing,training models and making predictions.

-stock.html:HTML template for web interface

-MLdemo.ppk: Key for amazon instance

-lstm_model.h5 : Trained LSTM model file

-requirements.txt : Dependencies/modules required for this program

-Dockerfile : Docker file to be run as a container.

-docker-compose.yml :Docker compose file.


## Tools/Tech Used

-Python

-Flask

-HTML

-Javascript

-Yahoo Finance API

-Postman

-Docker
## Model Accuracy
This is the predicted vs actual price vs the amazon stock price.

<img width="740" alt="image" src="https://github.com/LiandarJoshua/Stock-App/assets/160778757/6998dd99-08a5-452f-9b49-0b2bb939987a">

Mean Absolute Accuracy:3.6%

r2 score:0.9774996390278032


## API Deployment and Testing

To deploy the LSTM model as an API:

1. Use frameworks like Flask or FastAPI in Python to create a RESTful API.
2. Host your model on a server or a cloud platform such as AWS, Google Cloud, or Azure.
3. Define an API endpoint where clients can send requests to make predictions.
4. Implement error handling, input data validation, and logging in your API.
## API testing with postman
To test the LSTM model API using Postman:

1. Install Postman from [postman.com](https://www.postman.com/).
2. Open Postman and create a new request.
3. Set the request method (GET, POST, etc.) and enter the API endpoint URL.
4. Add request headers, body, and parameters as required by the API.
5. Send the request and verify the response received from the API.
6. Use Postman's testing features to validate the response data, status codes, and headers.
7. Test various scenarios, including edge cases and error handling, to ensure robustness.
8. Monitor API performance and track test results using Postman's collection runner and monitoring tools.

<img width="968" alt="image" src="https://github.com/LiandarJoshua/Stock-App/assets/160778757/fc32bb89-6821-44d8-bc5c-201d3463f17b">



Add a header for content-type and put the value as application/json

Body:

{
    "ticker":"AAPL"
}

On Posting:

{
    
    "closing_prices": [
        192.4199981689453,
        191.72999572753906,
        188.0399932861328,
        184.39999389648438,
        186.86000061035156,
        185.85000610351562,
        187.67999267578125,
        189.3000030517578,
        189.41000366210938,
        188.32000732421875,
        188.85000610351562,
        187.14999389648438,
        185.0399932861328,
        184.14999389648438,
        183.86000061035156,
        182.30999755859375,
        181.55999755859375,
        182.32000732421875,
        184.3699951171875,
        182.52000427246094,
        181.16000366210938,
        182.6300048828125,
        181.4199981689453,
        180.75,
        179.66000366210938,
        175.10000610351562,
        170.1199951171875,
        169.1199951171875,
        169.0,
        170.72999572753906
    ],
    
    "predictions": [
        [
            169.5373992919922
        ]
    ],
    
    "ticker": "AAPL"
}


## Deployment On Amazon EC2

1. **Create an EC2 Instance**: Launch a new EC2 instance on AWS. Choose an appropriate instance type and configure security groups to allow inbound traffic on port 5000 (or any other port you choose for the API).

2. **SSH into the Instance**: Connect to your EC2 instance using SSH. Use the key pair associated with the instance to authenticate.

3. **Clone the Repository**: Clone this repository onto your EC2 instance. You can use Git to clone the repository or manually transfer the code files.

4. **Install Dependencies**: Install the necessary dependencies for running the application. This may include Python packages, web servers (e.g., Nginx), and other libraries required by your application.

5. **Configure Environment**: Set up the environment variables required for your application, such as API keys, database connection strings, and any other configuration parameters.

6. **Run the Application**: Start the Flask application on your EC2 instance. Make sure it listens on the appropriate port and is accessible to external clients.

7. **Set up a Domain (Optional)**: If you have a custom domain, configure DNS settings to point to your EC2 instance's public IP address. You may also need to set up SSL/TLS certificates for HTTPS encryption.

8. **Test the API**: Once the application is running, test the API endpoints to ensure they are working correctly. You can use tools like Postman or cURL to send requests to the API.

9. **Monitor and Maintain**: Monitor the performance of your application and EC2 instance. Set up logging and monitoring tools to track API usage, errors, and other metrics. Perform regular maintenance tasks such as security updates and backups.
## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with any improvements or additional features you'd like to see.
