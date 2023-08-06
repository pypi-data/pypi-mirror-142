import numpy as np
import scipy.optimize as opt

__all__ = ["fit_leastsq"]


class fit_leastsq:
    """The default fit class used to calculate the profile
    likelihood. The fitting/optimization uses
    ``scipy.optimize.least_squares``.

    Parameters
    ----------
    nreturned: int
        (Required) Number of things returned by the by the fitting class. This
        is translated as the number of columns of the array to store the results
        temporarily. This will be used to create the matrix to store the results
        temporarily. For this fit class, `nreturned` should be `num_params + 2`,
        since the error code and the cost are also stored in addition to the
        optimized parameters.
    **kwargs
        (Optional) Keyword arguments to pass on to optimization routine.
    """

    def __init__(self, nreturned, **kwargs):
        self.nreturned = nreturned
        self.kwargs = kwargs

    def optimize(self, residuals, initial_guess, idx, fixed_param):
        """Do the optimization using `scipy.optimize.least_squares`. It takes
        arguments ``residuals, initial_guess, idx, fixed_param``. This method
        contains the optimization routine to use.

        Parameters
        ----------
        residuals: callable
            Function to be optimized. This will be a wrapper to
            ``model.residuals``
            (see :meth:`~profile_likelihood.compute._model_wrapper`).

        initial_guess: 1D array
            Initial guess for the optimization. This will be a
            vector of length n-1, where n is the number of model's
            parameters

        idx: int
            Index of parameter that is fixed. This is needed to
            insert ``fixed_param`` in to it's proper location.

        fixed_param: float
            Value of parameter that is held fixed.

        Returns
        -------
            Result of optimization in any format. Further processing
            will be done by ``return_class``.
        """
        opt_results = opt.least_squares(
            residuals,
            initial_guess,
            args=(
                idx,
                fixed_param,
            ),
            **self.kwargs
        )

        return opt_results

    def callback(self, opt_output, fixed_param, idx):
        """(Required) Process the results from ``fit_class.optimize``. It takes
        ``(opt_output, fixed_param, idx)`` as arguments. This method
        processes raw results from ``fit_class.optimize``
        (``opt_output`` parameter) to match the format used by
        ``profile_likelihood`` class. This method returns a 1D array, with
        element 0 be ``error_code``, elements 1 to n be ``opt_params``, and
        element n+1 be ``cost``. The array can have more element to return,
        if user wishes to return more information. For reference, also see
        :meth:`~profile_likelihood.compute._result_dict` for the construction
        of the final results dictionary from the array returned by this
        method.

        Parameters
        ----------
        opt_output:
            Output from ``fit_class.optimize``.

        fixed_param: float
            Value of parameter that is held fixed.

        idx: int
            Index of fixed parameter. Together with ``fixed_param``,
            this is used to insert the fixed parameter into the
            parameter result from the optimization.

        Returns
        -------
        1D array
            Array in the format
            ``[error_code, *opt_params, *others, cost]``.
        """
        error_code = opt_output.status
        opt_params = np.insert(opt_output.x, idx, fixed_param)
        cost = opt_output.cost
        results = np.hstack((error_code, opt_params, cost))

        return results
