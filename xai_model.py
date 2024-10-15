# xai_model.py
import shap
import matplotlib.pyplot as plt

def explain_model(model, X):
    explainer = shap.KernelExplainer(model.predict, X)
    shap_values = explainer.shap_values(X)
    
    # Summary plot to visualize feature importance
    shap.summary_plot(shap_values, X)
    
    return shap_values

def plot_shap_values(shap_values, X):
    shap.summary_plot(shap_values, X, plot_type="bar")
