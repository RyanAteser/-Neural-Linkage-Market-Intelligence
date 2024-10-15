# historical_accuracy.py
import numpy as np

def evaluate_model(predictions, actual_values):
    mape = np.mean(np.abs(predictions - actual_values) / actual_values) * 100  # MAPE
    return mape

# For Flask API
@app.route('/evaluate', methods=['POST'])
def evaluate():
    predictions = np.array(request.json['predictions'])
    actual_values = np.array(request.json['actual_values'])

    # Calculate the MAPE
    mape = evaluate_model(predictions, actual_values)

    return jsonify({'mape': mape})
