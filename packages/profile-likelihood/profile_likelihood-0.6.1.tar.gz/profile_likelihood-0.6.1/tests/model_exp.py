import numpy as np

# Setup variables needed to define the model
t = np.array([1.0, 1.2, 2.0])
best_fit = np.array([1, 2])
data = np.exp(-1 * t) + np.exp(-2 * t)
std = 1


def __basis(theta):
    return np.exp(-theta * t)


def __basis_J(theta):
    return -t * np.exp(-theta * t)


def predictions(p):
    return np.sum(np.array(list(map(__basis, p))), axis=0)


def residuals(p):
    return (predictions(p) - data) / std


def cost(p):
    return np.sum(residuals(p) ** 2) / 2


def jacobian(p):
    return np.array(list(map(__basis_J, p))).T
