# alert_system.py
import numpy as np

def detect_anomalies(stock_prices, threshold=2.5):
    anomalies = []
    for i in range(1, len(stock_prices)):
        if abs(stock_prices[i] - stock_prices[i - 1]) > threshold:
            anomalies.append((i, stock_prices[i]))
    return anomalies

def send_alert(anomaly):
    # Send alert (could be email, SMS, or app notification)
    print(f"Alert: Significant price change detected at index {anomaly[0]} with price {anomaly[1]}")
