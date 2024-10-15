from flask import Flask, request, jsonify
from data_aggregator import aggregate_data
from advanced_model import prepare_data, train_hybrid_model
from rl_model import RLAgent

app = Flask(__name__)
# app.py
from alert_system import detect_anomalies, send_alert

@app.route('/monitor', methods=['POST'])
def monitor():
    stock_prices = np.array(request.json['stock_prices'])
    
    # Detect anomalies in stock price
    anomalies = detect_anomalies(stock_prices)
    
    # Send alerts if anomalies are found
    for anomaly in anomalies:
        send_alert(anomaly)

    return jsonify({'anomalies': anomalies})

@app.route('/predict', methods=['GET'])
def predict():
    ticker = request.args.get('ticker')
    location = request.args.get('location')

    # Aggregate data
    data = aggregate_data(ticker, location)

    # Prepare the data for model training
    X, y, scaler = prepare_data(data)

    # Train hybrid model (LSTM + Transformer)
    model = train_hybrid_model(X, y)

    # Reinforcement Learning
        # Reinforcement Learning agent to adjust predictions
    rl_agent = RLAgent(state_size=60, action_size=1)
    adjusted_prediction = rl_agent.act(X[0][-1].reshape(1, 60))  # RL agent adjusts based on current state

    # Predict and scale back to original price
    prediction = model.predict([X[0][-1].reshape(1, 60, 1), X[1][-1].reshape(1, 60, -1)])
    predicted_price = scaler.inverse_transform(prediction)[0][0]

    # Apply RL adjustment to prediction
    final_predicted_price = predicted_price + adjusted_prediction

    return jsonify({'predicted_price': final_predicted_price})
# app.py
from xai_model import explain_model

@app.route('/explain', methods=['POST'])
def explain():
    # Get the input features
    data = request.json['data']
    
    # Convert to numpy array (example data)
    X = np.array(data)
    
    # Load the trained model
    model = load_trained_model()  # Placeholder for model loading
    
    # Explain the prediction using SHAP
    shap_values = explain_model(model, X)
    
    # Return the SHAP values
    return jsonify({'shap_values': shap_values.tolist()})


if __name__ == '__main__':
    app.run(debug=True)
