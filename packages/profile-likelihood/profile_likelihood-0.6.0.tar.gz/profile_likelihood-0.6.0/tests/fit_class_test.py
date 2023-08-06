import numpy as np
from scipy.optimize import leastsq


class fit:
    """This fitting class is used to create an error in the computation. The
    error comes because this class doesn't have `callback` method.
    """

    def __init__(self, nreturned, **kwargs):
        self.nreturned = nreturned
        self.kwargs = kwargs

    def optimize(self, residuals, initial_guess, idx, fixed_param):
        opt_results = leastsq(
            residuals,
            initial_guess,
            args=(
                idx,
                fixed_param,
            ),
            full_output=True,
            **self.kwargs
        )

        return opt_results
