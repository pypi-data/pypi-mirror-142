import numpy as np
import inspect

from . import save_load
from . import misc

from .compute import Compute
from .plot import Plots


class profile_likelihood(Compute, Plots):
    """Compute and present profile likelihood.

    Parameters
    ----------
    model: callable
        Function that is used in the optimization. This can be the residuals
        (which is required if we use Levenberg-Marquardt algorithm) or just
        the cost function (which is needed for other algorithm, such as
        conjugate-gradient).
    nparams: int
        Number of parameters the model accepts.
    npred: int
        Number of predictions the model returns.
    param_names: list of strings (optional)
        List of name of the parameters of the model. This list is used as the
        dictionary keys and the labels on the profile likelihood plots.
        default: ``['parameter0', 'parameter1', ....]``

    Attributes
    ----------
    model
        Function which is used in the optimization.
    nparams
        Number of parameters.
    npred
        Number of predictions.
    param_names
        Names of the parameters.
    results
        Results of the profile likelihood computation.
    """

    def __init__(self, model, nparams: int, npred: int, param_names=None):
        self.model = model

        assert isinstance(nparams, (int, np.int64))
        assert isinstance(npred, (int, np.int64))
        self.nparams = nparams
        self.npred = npred

        self._param_names = param_names
        self.results = None

    def save_results(self, filename):
        """Save ``self.results`` dictionary as a JSON file.

        Parameters
        ----------
        filename: str
            Path and filename destination to save ``self.results``
        """
        save_load.save_results(filename, self.results)

    def save_best_results(self, filename):
        """Save ``self.best_results`` dictionary as a JSON file.

        Parameters
        ----------
        filename: str
            Path and filename destination to save ``self.best_results``
        """
        save_load.save_results(filename, self.best_results)

    def load_results(self, filename, center, verbose=False, **kwargs):
        """Load ``self.results`` from the previously saved calculation. The
        arguments here are similar to ``self.compute``. However, arguments
        bounds, dt, and points are not needed as the internal mechanism will
        load thosse information from the loaded results.

        Parameters
        ----------
        filename: str
            Path to the result file.
        center: {1D ndarray, 2D ndarray}
            Points in parameter space where the computation uses as the center
            to create points in the profile likelihood computation, i.e. the
            computation will start with fixed parameter specified by the center,
            then move the fixed parameter to the left of the center, then to the
            right.
        verbose: bool, optional
            Value of the ``verbose`` flag, which is an option to print out some
            information  during computation to track the progress. This
            argument will be use if further calculation is to be done next.

        **kwargs
            Specifying custom classes to use.

            * start_class (see :meth:`~profile_likelihood.compute`)
            * fit_class (see :meth:`~profile_likelihood.compute`)

        Returns
        -------
        results: dict
            See :meth:`profile_likelihood.compute`.
        """
        # Load file
        self.results, self.param_names = save_load.load_results(
            filename, param_names=self.param_names
        )
        self._load_setup(center, verbose, **kwargs)  # Set attributes
        return self.results

    @property
    def param_names(self):
        """List of the names of the parameters in the model."""
        if np.ndim(self._param_names) == 0 and self._param_names is None:
            param_names = [
                "parameter" + str(ii) for ii in np.arange(self.nparams)
            ]
        else:
            misc.check_array_shape(
                self._param_names, (self.nparams,), "param_names"
            )
            param_names = self._param_names
        return param_names

    @param_names.setter
    def param_names(self, names):
        """Set parameters' names"""
        if np.ndim(names) == 0 and names == "default":
            self._param_names = [
                "parameter" + str(ii) for ii in np.arange(self.nparams)
            ]
        else:
            misc.check_array_shape(names, (self.nparams,), "param_names")
            self._param_names = names

    @property
    def model_info(self):
        """Name and location of the model class"""
        name = self.model.__name__
        path = inspect.getfile(self.model)
        return {"name": name, "location": path}
