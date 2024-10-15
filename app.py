from flask import Flask, request, jsonify
from data_aggregator import aggregate_data
from advanced_model import prepare_data, train_hybrid_model
from rl_model import RLAgent

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
