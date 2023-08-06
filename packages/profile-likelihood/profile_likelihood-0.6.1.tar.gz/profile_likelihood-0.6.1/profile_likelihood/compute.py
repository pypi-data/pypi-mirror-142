import numpy as np
import multiprocessing as mp
import queue
from collections import OrderedDict
import copy
import warnings
import traceback

from .setup import Setup
from . import misc


class Compute(Setup):
    """Collections of methods to run the profile likelihood
    computation.

    Attributes
    ----------
    results
        Results of the profile likelihood computation.
    """

    def compute(
        self,
        center,
        idx="all",
        points=None,
        bounds=[-10, 10],
        dt=0.1,
        verbose=False,
        dumpfile=None,
        processes=1,
        ignore_error=False,
        **kwargs,
    ):
        """Run profile likelihood computation.

        Parameters
        ----------
        center: {1D ndarray, 2D ndarray}
            Points in parameter space where the computation uses as the center
            to create points in the profile likelihood computation, i.e. the
            computation will start with fixed parameter specified by the center,
            then move the fixed parameter to the left of the center, then to the
            right.

        idx: {int, 1D ndarray,"all"}, optional
            Index of the parameter to compute the profile likelihood.
            default: ``'all'``, that is compute profile likelihood for all
            parameters.

        points: {1D ndarray, 2D ndarray}, optional
            Each element of this point will be used as the value of the fixed
            parameter. If a 1D ndarray is given, the profle likelihood
            computation for every ``idx`` will use the same list. Otherwise,
            the computation for every ``idx`` uses list from every row. If None,
            then linearly spaced points will be created using ``bounds``,
            ``dt``, and the best-fit parameter values.
            default: None

        bounds: {1D ndarray, 2D ndarray}, optional
            If 1D ndarray is given, then every parameter will have the same
            bounds. If 2D ndarray is given, every row gives the bounds of each
            parameter.
            default: [0, 10]

        dt: {float, 1D ndarray}, optional
            Spacing between points. If a scalar number is given, profile
            likelihood computation for each parameter uses the same spacing. If
            a 1D ndarray is given, each element of the array is used as spacing
            in the computation with its respective order.
            default: 0.1

        verbose: bool, optional
            An option to print out some information  during computation to track
            the progress. Information printed::

                name: "parameter's name",
                fix: "fixed parameter's value"
                error: "error code from the optimization routine"
                cost: "cost value at the optimized parameters"

            default: False

        dumpfile: str, optional
            If dumpfile is not None, the result of optimization on each point
            will be dumped into this file. This works like a backend to retrieve
            the computation results as it runs.
            The format of information dumped::

                idx:{idx}; error:{error_code}; parameters:{parameters};
                cost:{cost}

            * ``idx`` - Refering to index of parameter in of which the profile
              likelihood computation is performed
            * ``error_code`` - Error code returned by the optimization
              algorithm.
            * ``parameters`` - Optimized parameters from the optimization
              process, with the fixed parameter value placed in its correct
              position.
            * ``cost`` - Cost value evaluated at the optimized parameters.

            default: None

        processes: int, optional
            Number of processes used in the computation. Each process computes
            profile likelihood for different parameter. This parameter will be
            useful if the model has many parameters.
            default: 1

        ignore_error: bool, optional
            A flag to ignore the error that happens during computation. If this
            is set to be True, then when some error happens the computation will
            still running, but the error message will be stored in the result
            dictionary for the parameter(s) of which the error occurs.
            Otherwise, the computation will terminate whenever an error occurs.
            default: False

        **kwargs
            Specify custom classes. See below for the classes available.

        start_class: object, kwargs
            Class object to handle the initial guesses of the optimization.
            As the default, there will be 1 initial guess, which is the
            previous optimized parameters. Requirements for user-define
            ``start_class``:

            * Attributes: ``self.nguess`` - Number of different initial guess'.
            * Methods:

              * ``self.set_points_0()`` - Reset initial starting points to
                starting point. The profile likelihood computation will start
                from ``center`` then moves to the left, and then it will go
                back to the ``center`` and move to the right this time. This
                method is called when the computation move back to the
                ``center``.
              * ``self.get_points()`` - Get initial guesses to use in the
                optimization.
              * ``self.update()`` -  Update the next starting points.

            default: None, which uses
            :class:`~profile_likelihood.default.single_starting_point`

        fit_class: object, kwargs
            Class object that contains the optimization routine. Requirements
            for user-define ``fit_class``:

            * Attributes: ``self.nreturned`` - number of things returned by the
              by the fitting class. This is translated as the number of columns
              of the array to store the results temporarily. This will be used
              to create the matrix to store the results temporarily.
            * Methods:

              * ``self.optimize(residuals, initial_guess, idx,
                fixed_param)`` - This method contains the optimization routine
                to use.
              * ``self.callback(opt_output, fixed_param, idx)`` - Method to
                process raw results from ``fit_class.optimize``
                (``opt_output`` parameter) to match the format used by
                ``profile_likelihood`` class. This method returns a 1D array,
                with element 0 be ``error_code``, elements 1 to n be
                ``opt_params``, and element n+1 be ``cost``. The array can have
                more element to return, if user wishes to return more
                information.

            default: None, which uses
            :class:`~profile_likelihood.default.fit_leastsq`

        Returns
        -------
        results: dict
            Dictionary of the results of the calculation. The format of the
            dictionary is ::

                results = {"parameter0": {"error_code": error_code,
                                          "parameters": opt_params,
                                          "others": other_information,
                                          "cost": cost_values},
                           "parameter1": {...},
                           ...}
        """

        self._compute_setup(
            center, idx, points, bounds, dt, verbose, dumpfile, **kwargs
        )
        self._ignore_error = ignore_error
        if self._dumpfile:
            with open(self._dumpfile, "w+") as _:  # Overwrite the old file
                pass

        Results = OrderedDict()
        if processes == 1:
            return_dict = self._run_serial()
        else:
            return_dict = self._run_parallel(processes)

        for nn in np.array(self.param_names):
            try:
                Results.update({nn: dict(return_dict)[nn]})
            except KeyError:
                Results.update({nn: {}})

        self.results = Results
        return self.results

    ##################################################################
    ##################################################################
    ##################################################################

    def _run_serial(self):
        """Run the profile likelihood computation in series."""
        return_dict = {}
        for ii, ix in enumerate(self.idx):
            iname = self.param_names[ix]
            try:
                result = self._compute_one(
                    ix,
                    center=self.center[ii],
                    points=self._points[ii],
                    bounds=self.bounds[ii],
                    dt=self.dt[ii],
                )[iname]
            except Exception as ex:
                message = (
                    f'Error occured, check results["{iname}"]["traceback"]'
                )
                warnings.warn(misc.error_print_style(message))
                result = self._error_dict()
                if not self._ignore_error:
                    raise ex

            return_dict.update({iname: result})

        return return_dict

    def _run_parallel(self, processes):
        """Run the profile likelihood computation in parallel."""
        nprocesses = processes
        task_to_accomplish = mp.Queue()
        task_done = mp.Queue()
        Processes = []
        manager = mp.Manager()
        return_dict = manager.dict()

        for ii, ix in enumerate(self.idx):
            task_to_accomplish.put(f"Task no. {ii} for parameter index {ix}")

        # creating processes
        for _ in range(nprocesses):
            Proc = mp.Process(
                target=self._likelihood_wrapper,
                args=(return_dict, task_to_accomplish, task_done),
            )
            Processes.append(Proc)
            Proc.start()

        for Proc in Processes:
            Proc.join()

        while not task_done.empty():
            print(task_done.get())

        return return_dict

    def _likelihood_wrapper(self, return_dict, task_to_accomplish, task_done):
        """Wrapper to ``_compute_one``. This is done so that multiprocessing
        can work.

        Parameters
        ----------
        return_dict: dict
            ``multiprocessing.Manager.dict`` used to store the results.
        task_to_accomplish: str
            Task to accomplish.
        task_done: str
            Tasks that are done.
        """
        name = self.param_names
        while True:
            try:
                task = task_to_accomplish.get_nowait()
            except queue.Empty:
                break
            else:
                ii, idx = np.array(task.split(" "))[[2, -1]].astype(int)

                iname = name[idx]
                try:
                    return_dict[iname] = self._compute_one(
                        self.idx[ii],
                        center=self.center[ii],
                        points=self._points[ii],
                        bounds=self.bounds[ii],
                        dt=self.dt[ii],
                    )[iname]
                    task_done.put(
                        f"Task for {iname} "
                        "is done by "
                        f"{mp.current_process().name}"
                    )
                except Exception as ex:
                    message = (
                        f'Error occured, check results["{iname}"]["traceback"]'
                    )
                    warnings.warn(misc.error_print_style(message))
                    return_dict[iname] = self._error_dict()
                    if not self._ignore_error:
                        raise ex

    def _compute_one(self, idx: int, center, points, bounds, dt):
        """Compute profile likelihood of one of the parameters.

        Parameters
        ----------
        idx: int
            Index of parameter requested.
        center: ndarray
            Center points of the list of fixed parameters.
        points: list
            Fixed parameter values to use.
        bounds: ndarray
            Bounds of the parameter to evaluate. `points` will be prioritized.
        dt: float
            Spacing between fixed parameter value.

        Returns
        -------
        results: dict
            Dictionary result for one parameter.

        Note
        ----
            User needs to specify either `points` or `bounds` and `dt` together.
        """

        # Create parameter list
        params_left, params_right = self._create_params_list(
            idx, center, points, bounds, dt
        )

        # Do calculation for parameters in params_left
        results_left = self._loop_optimization(idx, params_left)

        # Do calculation for parameters in params_right
        results_right = self._loop_optimization(idx, params_right)

        # Combine results
        results_left = self._flip_results_vertical(
            results_left
        )  # Flip result_left
        temp = np.row_stack((results_left, results_right))

        # Store in dictionary
        results = {self.param_names[idx]: self._results_dict(temp)}
        return results

    def _create_params_list(self, idx: int, center, points, bounds, dt):
        """Create list of fixed parameters to the left and right
        of the best-fit parameters.

        Parameters
        ----------
        idx: int
            Index of parameter requested.
        center: ndarray
            Center points of the list of fixed parameters.
        points: list
            Fixed parameter values to use.
        bounds: ndarray
            Bounds of the parameter to evaluate. `points` will be prioritize.
        dt: float
            Spacing between fixed parameter value.

        Returns
        -------
        params_left, params_right: ndarray
            List of parameters to the left and to the right of best-fit.
        """
        # If points are not specified, use bounds and dt
        if np.ndim(points) == 0:
            params_left, params_right = self._create_params_linspace(
                idx, center, bounds, dt
            )
        # If points are specified, use points
        else:
            params_left, params_right = self._split_points(idx, center, points)
        return params_left, params_right

    def _create_params_linspace(self, idx: int, center, bounds, dt):
        """Create linearly spaced parameters to the left and right of
        the best-fit parameters.

        Parameters
        ----------
        idx: int
            Index of parameter requested.
        center: ndarray
            Center points of the list of fixed parameters.
        bounds: ndarray
            Bounds of the parameter to evaluate.
        dt: float
            Spacing between fixed parameter value.

        Returns
        -------
        param_list_left, param_list_right: ndarray
            Linearly spaced points to the left and to right left of best-fit.
        """
        param_list_left = self._linspace_left(idx, center, bounds, dt)
        param_list_right = self._linspace_right(idx, center, bounds, dt)

        return param_list_left, param_list_right

    @staticmethod
    def _linspace_left(idx: int, center, bounds, dt):
        """Generate linearly spaced parameters to the left of the best-fit
        parameters.

        Parameters
        ----------
        idx: int
            Index of parameter requested.
        center: ndarray
            Center points of the list of fixed parameters.
        bounds: ndarray
            Bounds of the parameter to evaluate.
        dt: float
            Spacing between fixed parameter value.

        Yields
        ------
        n: float
            Point to the left of best-fit.
        """
        n = copy.copy(center[idx])
        while n >= bounds[0]:
            yield n
            n -= dt

    @staticmethod
    def _linspace_right(idx: int, center, bounds, dt):
        """Generate linearly spaced parameters to the right of the best-fit
        parameters.

        Parameters
        ----------
        idx: int
            Index of parameter requested.
        center: ndarray
            Center points of the list of fixed parameters.
        bounds: ndarray
            Bounds of the parameter to evaluate.
        dt: float
            Spacing between fixed parameter value.

        Yields
        ------
        n: float
            Point to the right of best-fit.
        """
        n = copy.copy(center[idx]) + dt
        while n <= bounds[1]:
            yield n
            n += dt

    @staticmethod
    def _split_points(idx: int, center, points):
        """Split the list of points at the point nearest to the best-fit.

        Parameters
        ----------
        idx: int
            Index of parameter requested.
        center: ndarray
            Center points of the list of fixed parameters.
        points: list
            Fixed parameter values to use.

        Returns
        -------
        left, right: ndarray
            List of parameters to the left and to the right of best-fit.
        """
        value = center[idx]
        idx_split = (np.abs(points - value)).argmin()
        left = points[: idx_split + 1][::-1]
        right = points[idx_split + 1 :]
        return left, right

    def _loop_optimization(self, idx: int, params_list):
        """Loop the optimization process over the params_list.

        Parameters
        ----------
        idx: int
            Index of parameter requested.
        params_list: list
            List of fixed parameter values.

        Returns
        -------
        mat_store: 2D ndarray
            Matrix containing results of the optimizations.
        """
        self.start.set_points_0()
        mat_store = np.empty((0, self.nreturned))
        ii = np.argwhere(self.idx == idx)[0, 0]
        for fixed_params in params_list:
            starting_points = self.start.get_points(ii)
            results_opt = self._optimize_block(
                idx, fixed_params, starting_points
            )
            mat_store = np.row_stack((mat_store, results_opt))
            self.start.update(results_opt, ii)
        return mat_store

    def _optimize_block(self, idx: int, fixed_params: float, starting_points):
        """Do optimization for all starting points for one block with a single
        fixed parameter value.

        Parameters
        ----------
        idx: int
            Index of parameter requested.
        fixed_params: float
            Value of parameter that is held fixed.
        starting_points: 2d-ndarray
            Matrix of starting points.

        Returns
        -------
        results_mat: 2D ndarray
            Matrix containing results of the optimizations.
        """
        results_mat = np.empty((self.nguess, self.nreturned))
        for ii, params in enumerate(starting_points):
            params_to_fit = np.delete(params, idx)
            if self._verbose:
                print(
                    "Optimizing parameter name: {}, fixed value: {}".format(
                        self.param_names[idx],
                        fixed_params,
                    )
                )
            results = self.fit.optimize(
                self._model_wrapper, params_to_fit, idx, fixed_params
            )
            results_mat[ii] = self.fit.callback(results, fixed_params, idx)

            if self._verbose:
                print("Optimization terminated:")
                print(
                    "error code: {}, final cost: {}\n".format(
                        int(results_mat[ii][0]),
                        results_mat[ii][-1],
                    )
                )
            if self._dumpfile:
                self._write_dumpfile(results_mat[ii], idx)
        return results_mat

    def _model_wrapper(self, params_to_fit, idx: int, fixed_params: float):
        """Wrapper to the ``model``. It handles the reduction of the
        model by 1 parameter.This function will be fed into
        ``fit_class.optimize``.

        Parameters
        ----------
        params_to_fit: list
            Free variable in the function.
        idx: int
            Index of parameter held fixed.
        fixed_params: float
            Value of parameter held fixed.

        Returns
        -------
        residuals: callable
            Reduced residuals of the model.
        """
        parameters = misc.insert_parameters(params_to_fit, idx, fixed_params)
        return self.model(parameters)

    def _flip_results_vertical(self, results_array):
        """Used to flip the results array vertically from the calculation to
        the left.

        Parameters
        ----------
        results_array: ndarray
            Array to flip.

        Returns
        -------
        results_flipped: ndarray
            Flipped array.
        """
        nguess = self.nguess
        results_array = results_array[::-1]
        results_flipped = copy.copy(results_array)
        for ii in range(nguess):
            results_flipped[ii::nguess] = results_array[
                nguess - 1 - ii :: nguess
            ]
        return results_flipped

    def _results_dict(self, results_mat):
        """Convert the results array into dictionary.

        Parameters
        ----------
        results_mat: 2d-ndarray
            Matrix containing the results of optimization

        Returns
        -------
        results: dict
            Dictionary of the results.
        """
        N = self.nparams
        error_code = results_mat[:, 0]
        parameters = results_mat[:, 1 : N + 1]
        costs = results_mat[:, -1]
        others = results_mat[:, N + 1 : -1]

        # Construct dictionary
        results = {
            "error_code": error_code,
            "parameters": parameters,
            "others": others,
            "cost": costs,
        }
        return results

    def _error_dict(self):
        """Create dictionary store in place if some errors happened
        during profile likelihood computation.

        Returns
        -------
        errDict: dict
            Dictionary to store when an error occured.
        """
        errDict = {
            "error_code": "Some error happened",
            "parameters": self.center,
            "cost": [0],
            "traceback": traceback.format_exc(),
        }
        if self._verbose:
            print(errDict["traceback"])
        return errDict

    def _write_dumpfile(self, results_vec, idx):
        """Write the result from one optimization process to fixed parameter
        index ``idx`` using one of the starting points.

        Parameters
        ----------
        results_vec: ndarray
            1D array containing the result from the optimization process.
        idx: int
            Index of fixed parameter.
        """
        dump_text = "idx:{}; error:{}; parameters:{}; cost:{}\n".format(
            idx,
            int(results_vec[0]),
            ",".join([str(f) for f in results_vec[1 : self.nparams + 1]]),
            results_vec[-1],
        )
        with open(self._dumpfile, "a") as f:
            f.write(dump_text)

    @property
    def fixed_params(self):
        """List of values of the parameters that are set fixed."""
        names = np.array(self.param_names)[self.idx]
        points = [[] for _ in range(self.nparams)]
        for name, ii in zip(names, self.idx):
            points[ii] = self.results[name]["parameters"][:, ii]
        return points

    @property
    def best_results(self):
        """The best results from ``self.results``. This will be the same as
        ``self.results`` if only 1 initial guess is used. If the computation is
        done using multiple initial guesses, then this will get the best result
        (lowest cost) for each fixed parameter value.
        """
        if self.nguess == 1:
            best_results = self.results
        else:
            keys = list(self.results)
            best_results = {}

            for key in keys:
                res = self.results[key]  # Results for each parameter
                try:
                    best_results[key] = self._filter_best(res, key)
                except KeyError:
                    best_results[key] = self.results[key]

        return best_results

    def _filter_best(self, results_dict, param_name):
        """Filter the results to only return the best cost for each fixed
        parameters.

        Parameters
        ----------
        results_dict: dict
            Results dictionary of one of the parameter.
        key: str
            Name of parameters that is processed.

        Returns
        -------
        results_dict: dict
            Filtered results dictionary.
        """
        # Convert dict to array
        results_mat = misc.dict_to_array(results_dict)
        _, ncolumns = np.shape(results_mat)

        # nguess = self.nguess
        idx_param = list(self.param_names).index(param_name)
        fixed_points = self.fixed_params[idx_param]
        fixed_params = results_mat[:, idx_param + 1]

        # filtered_mat = np.empty((nrows, ncolumns))
        filtered_mat = np.empty((0, ncolumns))

        for point in fixed_points:
            # Get results from the same fixed point
            idx_fixed_params = np.where(fixed_params == point)[0]
            if idx_fixed_params.size:
                # Get results corresponding to the same fixed parameter value
                temp_mat = results_mat[idx_fixed_params]
                cost = temp_mat[:, -1]
                try:
                    idx_min = np.nanargmin(cost)
                    filtered_mat = np.row_stack(
                        (filtered_mat, temp_mat[idx_min])
                    )
                except ValueError:
                    # Print warnin
                    message = (
                        f"Results for parameter {param_name} with fixed value "
                        + f"{point} contain all nan costs"
                    )
                    warnings.warn(misc.error_print_style(message))

        # convert the results back to dictionary
        return self._results_dict(filtered_mat)

    @property
    def compute_info(self):
        """Information of the compute method the user sets, which will show the
        list of fixed parameter values, number of initial guess, and the name
        and location of the start and fit classes.
        """
        return {
            "fixed_params": self.fixed_params,
            "nguess": self.nguess,
            "start_class": self.start_info,
            "fit_class": self.fit_info,
        }

    def print_error(self, parameter):
        """Print error message.

        Parameters
        ----------
        parameter: str
            Name of parameter requested.
        """
        try:
            msg = self.results[parameter]["traceback"]
            print(msg)
        except KeyError:
            print("No error occured")
