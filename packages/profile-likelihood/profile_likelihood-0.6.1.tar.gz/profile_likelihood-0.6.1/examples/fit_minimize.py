import numpy as np
from scipy.optimize import minimize


class fit:
    def __init__(self, nreturned, **kwargs):
        self.nreturned = nreturned
        self.kwargs = kwargs

    def optimize(self, cost, initial_guess, idx, fixed_param):
        opt_results = minimize(
            cost,
            initial_guess,
            args=(
                idx,
                fixed_param,
            ),
            **self.kwargs
        )
        return opt_results

    def callback(self, opt_output, fixed_param, idx):
        error_code = opt_output.status
        opt_params = np.insert(opt_output.x, idx, fixed_param)
        cost = opt_output.fun
        results = np.hstack((error_code, opt_params, cost))
        return results
