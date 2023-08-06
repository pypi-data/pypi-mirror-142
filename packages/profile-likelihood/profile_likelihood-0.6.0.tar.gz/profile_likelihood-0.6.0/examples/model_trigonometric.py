import numpy as np


"""The model we will considere is the sum of sine functions,
    y(theta, t) = sin(theta0*t) + cos(theta1*t) + ....
"""

t = np.array([1.0, 1.2, 2.0])  # Time stamps of the observed data
best_fit = np.array([1.0, 2.5])  # Best-fit parameters
data = np.sin(best_fit[0] * t) + np.cos(best_fit[1] * t)  # Observed data
std = 0.3 * data  # Standard deviations
param_names = [r"$\theta_0$", r"$\theta_1$"]  # Name of the parameters
nparams = len(best_fit)  # Number of parameters
npred = len(t)  # Number of predictions


def predictions(theta):
    return np.sin(theta[0] * t) + np.cos(theta[1] * t)


def residuals(theta):
    return (predictions(theta) - data) / std


def cost(theta):
    return np.sum(residuals(theta) ** 2) / 2
