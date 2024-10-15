import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dense, Input, Dropout, MultiHeadAttention, Conv2D, Flatten
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Model

# LSTM + Transformer Model
def create_hybrid_model(input_shape):
    # LSTM Branch
    lstm_input = Input(shape=input_shape)
    lstm_branch = LSTM(64, return_sequences=True)(lstm_input)
    lstm_branch = LSTM(64)(lstm_branch)
    lstm_branch = Dense(32, activation='relu')(lstm_branch)

    # Transformer Branch
    transformer_input = Input(shape=input_shape)
    transformer_branch = MultiHeadAttention(num_heads=4, key_dim=64)(transformer_input, transformer_input)
    transformer_branch = Dense(64, activation='relu')(transformer_branch)
    transformer_branch = Dense(32, activation='relu')(transformer_branch)

    # Merge both branches
    combined = tf.keras.layers.Concatenate()([lstm_branch, transformer_branch])
    combined = Dense(64, activation='relu')(combined)
    combined = Dropout(0.3)(combined)
    output = Dense(1, activation='linear')(combined)

    model = Model(inputs=[lstm_input, transformer_input], outputs=output)
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')
    return model

def prepare_data(df, target_column='Close'):
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(df)

    X_lstm, X_transformer, y = [], [], []
    for i in range(60, len(data_scaled)):
        X_lstm.append(data_scaled[i-60:i, 0])  # LSTM for historical stock price
        X_transformer.append(data_scaled[i-60:i, :])  # Transformer for all features
        y.append(data_scaled[i, 0])
    
    X_lstm, X_transformer, y = np.array(X_lstm), np.array(X_transformer), np.array(y)
    X_lstm = np.reshape(X_lstm, (X_lstm.shape[0], X_lstm.shape[1], 1))  # Reshape for LSTM input
    return [X_lstm, X_transformer], y, scaler

def train_hybrid_model(X, y):
    model = create_hybrid_model((X[0].shape[1], X[0].shape[2]))  # Input shapes for both LSTM and Transformer
    model.fit(X, y, epochs=20, batch_size=32, verbose=1)
    return model
