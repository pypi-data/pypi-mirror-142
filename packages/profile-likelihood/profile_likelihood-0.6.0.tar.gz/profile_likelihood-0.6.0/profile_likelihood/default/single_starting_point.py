import numpy as np
import copy


__all__ = ["single_starting_point"]


class single_starting_point:
    """Default class to get and process initial guesses used in the
    optimization.

    Parameters
    ----------
    start0
        (Optional) Initial guess used when the optimization is done around the
        best-fit parameter.

    Attributes
    ----------
    nguess
        (Required) Number of different initial guess.

    start0
        (Optional) Initial guess used when the optimization is done around the
        best-fit parameter.

    nparams
        (Optional) Number of parameters.

    start
        (Optional) Values of the starting points.
    """

    def __init__(self, start0):
        self.start0 = start0
        self.nparams = len(start0)
        self.nguess = 1

    def set_points_0(self):
        """(Required) Reset the starting points to ``self.start0``. The profile
        likelihood computation will start from ``best_fit`` then moves to the
        left, and then it will go back to the ``best_fit`` and move to the right
        this time. This method is called when the computation move back to the
        ``best_fit``.
        """
        self.start = copy.copy(self.start0)

    def get_points(self, ii):
        """(Required) Return 2D array of starting points for optimizations
        corresponding to each fixed parameter value.

        Parameters
        ----------
        ii: int
            Location of index of parameters held fixed in the list of index
            given.

        Returns
        -------
        ndarray
            Array of initial starting points used in the optimization when
            parameter idx is held fixed.
        """
        return np.array([self.start[ii]])

    def update(self, results_opt, ii):
        """(Required) Update the initial guesses. This method will be called
        every time after an optimization for 1 fixed parameter value.

        Parameters
        ----------
        results_opt:
            Output from ``fit_class.optimize``.
        ii: int
            Location of index of parameters held fixed in the list of index
            given.
        """
        if 0 < results_opt[0, 0] < 5:
            # Update the next starting point
            # if the optimization converges
            self.start[ii] = results_opt[0, 1 : self.nparams + 1]
