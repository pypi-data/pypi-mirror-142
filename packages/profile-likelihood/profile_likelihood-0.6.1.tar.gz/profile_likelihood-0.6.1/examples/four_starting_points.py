import numpy as np
import copy

__all__ = ["starting_points"]


# Default choose_starting_point
class four_points:
    def __init__(self, start0):
        self.start0 = start0
        self.nparams = len(start0)
        self.nguess = 4

    def set_points_0(self):
        # Reset the starting points after calculations
        self.start = copy.copy(self.start0)
        self.best = copy.copy(self.start0)

    def get_points(self, _):
        # Return 2D array of starting points for each optimization
        starting = np.row_stack((self.start, self.best, [-5, -5], [5, 5]))
        return starting

    def update(self, results_opt, _):
        # Call after optimization
        # Control whether to update starting points
        # Update the internal to get the next starting point
        if results_opt[0, 0] != 0:
            # Update the next starting poit if the optimization converges
            self.start = results_opt[0, 1 : self.nparams + 1]

            # Get the best results
            residuals = results_opt[:, 3:8]
            sqrt_cost = np.linalg.norm(residuals, axis=1)
            results_temp = np.hstack((results_opt, sqrt_cost.reshape((-1, 1))))
            results_temp = results_temp[np.argsort(results_temp[:, -1])]
            self.best = results_temp[0, 1 : self.nparams + 1]
