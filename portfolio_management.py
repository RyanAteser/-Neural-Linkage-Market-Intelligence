# portfolio_management.py
import numpy as np
from scipy.optimize import minimize

def portfolio_optimizer(returns, cov_matrix, target_return):
    num_assets = len(returns)

    # Define the objective (minimize risk)
    def objective(weights):
        return np.dot(weights.T, np.dot(cov_matrix, weights))

    # Constraints: weights must sum to 1, and target return
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1},
                   {'type': 'eq', 'fun': lambda weights: np.dot(weights, returns) - target_return})
    
    # Bounds for weights
    bounds = tuple((0, 1) for asset in range(num_assets))

    # Initial guess (equal weight allocation)
    init_guess = num_assets * [1. / num_assets,]

    # Optimization
    result = minimize(objective, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)

    return result.x  # Optimal weights
