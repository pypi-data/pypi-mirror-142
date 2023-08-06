import numpy as np
import inspect

from .misc import error_print_style
from .default.fit_leastsq import fit_leastsq
from .default.single_starting_point import single_starting_point

tol = np.finfo(float).eps


class Setup:
    """Collections of methods to setup stuffs for either the
    computation and loading the results.
    """

    def _compute_setup(
        self, center, idx, points, bounds, dt, verbose, dumpfile, **kwargs
    ):
        """Set variables before computing profile likelihood.

        Parameters
        ----------
        center: ndarray
            List of points that will be the center of lists of fixed parameters.
        idx: list
            List of indices requested.
        points: ndarray
            List of fixed parameter values.
        bounds: ndarray
            Bounds of parameter to calculate.
        dt: {float, ndarray}
            Spacing between fixed parameter.
        verbose: bool
            Flag to print some information.
        dumpfile: str
            Name of dump file to monitor the progress.
        **kwargs
            Specifying custom classes.
        """
        self._points_or_bounds_specified(bounds, points)

        self.idx, self._nidx = self._set_idx(idx)

        self._points, bounds, dt = self._set_points(points, bounds, dt)
        self.bounds = self._set_bounds(bounds)
        self.dt = self._set_dt(dt)

        self.center = self._set_center(center)

        self._verbose = verbose
        self._dumpfile = dumpfile
        self._set_optimization_objects(**kwargs)

    def _load_setup(self, center, verbose, **kwargs):
        """Set variables from the loaded profile likelihood results.

        Parameters
        ----------
        **kwargs
            Specifying custom classes.
        """
        self._verbose = verbose
        self.idx = self._load_idx()
        self._nidx = len(self.idx)

        self._points = self._load_points()
        self.bounds = self._load_bounds(self._points)
        self.dt = self._load_dt(self._points)

        self.center = self._set_center(center)
        self._set_optimization_objects(**kwargs)

    @staticmethod
    def _points_or_bounds_specified(bounds, points):
        """Check if bounds and points are not both None. In most cases, this
        will not raise an assertion error since most likely that bounds have
        some values.

        Parameters
        ----------
        bounds: list
            Bounds of parameters.
        points: ndarray
            List of fixed parameter values.
        """
        tocheck = np.ndim(bounds) + np.ndim(points)
        msg = "Need to specify either the points or the bounds."
        assert tocheck > 0, msg

    def _set_idx(self, idx):
        """Process the argument idx and set `self.idx`.

        Parameters
        ----------
        idx: int or list
            Index of parameter requested.

        Returns
        -------
        ndarray, int
            Array of sorted parameter indices and number of indices.

        Raises
        ------
        ValueError
            If dimension of the input array is greater than 1.

        """
        ndim = np.ndim(idx)
        if ndim == 0:
            if idx == "all":
                idx = np.arange(self.nparams)
            else:
                idx = [idx]
        elif ndim > 1:
            raise ValueError("Only accept idx as int or 1D array")
        return np.sort(idx), len(idx)

    def _set_points(self, points, bounds, dt):
        """Process the argument points and set `self._points`.

        Parameters
        ----------
        points: ndarray
            List of fixed parameter values.

        Returns
        -------
        points: ndarray
            Argument `points` in the correct format.
        bounds: ndarray
            Updated bounds from the points data. If there is no point data,
            then this will just be the original bounds specified.
        dt: {ndarray, None}
            Updated dt from the points data. This will be the original value
            given if there is no points data or None if points data is given.

        Raises
        ------
        ValueError
            If dimension of the input array is not 1 or 2.

        """
        ndim = np.ndim(points)

        if isinstance(points, type(None)):
            points = np.repeat(None, self._nidx)
        elif ndim in [1, 2]:
            points = np.asarray(points)
            dtype = points.dtype

            # If list of points for every parameter is specified
            if dtype == "object" or ndim == 2:
                msg = "Number of rows needs to be equal to number of indices"
                assert len(points) == self._nidx, msg
            # If one list is specified for all parameters
            elif ndim == 1:
                points = np.tile(points, (self._nidx, 1))

            bounds = np.array([[p[0], p[-1]] for p in points])
            dt = None
        else:
            raise ValueError("Can only accept 1D or 2D array")

        return points, bounds, dt

    def _set_bounds(self, bounds):
        """Process the argument bounds and set `self.bounds`.

        Parameters
        ----------
        bounds: list
            Bounds of parameters.

        Returns
        -------
        bounds: ndarray
            Argument `bounds` in the correct format.

        Raises
        ------
        ValueError
            If dimension of the input array is not 1 or 2.

        """
        ndim = np.ndim(bounds)

        if bounds is None:
            pass
        elif ndim == 1:
            bounds = np.tile(bounds, (self._nidx, 1))
        elif ndim == 2:
            msg = "Number of rows needs to be equal to number of indices"
            assert len(bounds) == self._nidx, msg
        else:
            raise ValueError("Can only accept 1D or 2D array")

        return bounds

    def _set_dt(self, dt):
        """Process the argument dt and set `self.dt`.

        Parameters
        ----------
        dt: {float, ndarray}
            Parameter spacing.

        Returns
        -------
        dt: ndarray
            Argument `dt` in the correct format.

        Raises
        ------
        ValueError
            If dimension of the input array is greater than 1.

        """
        ndim = np.ndim(dt)

        if ndim == 0:
            dt = np.tile(dt, (self._nidx, 1))
        elif ndim == 1:
            msg = "Number of elements needs to be equal to number of indices"
            assert len(dt) == self._nidx, msg
        else:
            raise ValueError("Can only accept float or 1D array")

        return dt

    def _set_center(self, center):
        """Process the argument center and set `self.center`

        Parameters
        ----------
        center : {1D ndarray, 2D ndarray}
            Array of the center points of the list of fixed
            parameters.

        Returns
        -------
        ndarray
            Array of center points in the correct format, where each element is
            inside the bounds.

        Raises
        ------
        ValueError
            If dimension of the input array is not 1 or 2.

        """
        center = np.asarray(center)

        if center.ndim == 1:  # If all have the same center
            msg = "Number of elements needs to be equal to number of parameters"
            assert len(center) == self.nparams, msg
            center = np.tile(center, (self._nidx, 1))
        elif center.ndim == 2:  # They might have different center points
            msg = f"Array must be {self._nidx} by {self.nparams}"
            assert center.shape == (self._nidx, self.nparams), msg
        else:
            raise ValueError("Can only accept 1D or 2D array")

        return self._check_center_in_bounds(center)

    def _check_center_in_bounds(self, center):
        """Check if the ith coordinate of the ith center is inside the bound,
        if not then push the coordinate to the bound.

        Parameters
        ----------
        center : np.ndarray
            Center points to check if it is inside the bounds

        Returns
        -------
        ndarray
            Modified center points with all points inside the bounds.

        """
        center = np.asarray(center, dtype=float)
        msg = "Center point outside bounds, change center point: "
        # center and bounds already have rows equal to nidx
        for ii, (crow, brow) in enumerate(zip(center, self.bounds)):
            if crow[ii] < brow[0]:  # center point < lower bound
                center[ii, ii] = brow[0]
                print(msg + f"{crow[ii]} -> {center[ii, ii]}")
            elif crow[ii] > brow[1]:  # center point > upper bound
                center[ii, ii] = brow[1]
                print(msg + f"{crow[ii]} -> {center[ii, ii]}")
        return center

    def _set_optimization_objects(self, **kwargs):
        """Set optimization objects to use.

        Parameters
        ----------
        **kwargs
            Specifying custom classes.

        """
        if "fit_class" in kwargs:
            self.fit = kwargs.pop("fit_class")
        else:
            self.fit = fit_leastsq(self.nparams + 2)

        if "start_class" in kwargs:
            self.start = kwargs.pop("start_class")
        else:
            self.start = single_starting_point(self.center)

        if bool(kwargs):
            print(
                error_print_style(f"Unknown keyword arguments: {list(kwargs)}")
            )

        self.nguess = self.start.nguess
        self.nreturned = self.fit.nreturned

    def _load_idx(self):
        """Get list of `idx` from the loaded results.

        Returns
        -------
        idx: list
            List of indices of parameters that were computed.
        """
        idx = []
        for ii in range(self.nparams):
            name = self.param_names[ii]
            if "parameters" in self.results[name]:
                idx.append(ii)
        return idx

    def _load_points(self):
        """Get the points of fixed parameters from the results and set
        `self._points`.

        Returns
        -------
        list
            List of fixed parameter values
        """
        points = []
        dt = []
        for name, idx in zip(self.param_names, self.idx):
            try:
                parameters = self.results[name]["parameters"]
                points.append(list(parameters[:, idx]))
            except KeyError:
                print(f"{name} not found")

        return np.array(points)

    def _load_bounds(self, points):
        """Get the bounds from the points and set it to `self.bounds`.

        Parameters
        ----------
        points: list
            List of fixed parameter values.
        """
        bounds = []
        for pp in points:
            bounds.append([pp[0], pp[-1]])
        return np.asarray(bounds)

    @staticmethod
    def _load_dt(points):
        """Get the spacing dt from the points and set it to `self.dt`. If the
        points are not linearly spaced, dt will be set to None.

        Parameters
        ----------
        points: list
            List of fixed parameter values.
        """
        dt = []
        for pp in points:
            pp = np.asarray(pp)
            # List of unique spacings
            unique_spacings = np.unique(np.diff(pp))
            nunique = len(unique_spacings)
            # Make sure the difference in spacing is not because of numerical
            # precision.
            if nunique == 1:
                max_diff_spacing = 0.0
            else:
                max_diff_spacing = np.max(np.diff(unique_spacings))
            if max_diff_spacing > tol:
                # If difference is not caused by numerical precision, leave it
                spacings = unique_spacings
            else:
                # If difference is caused by numerical precision, filter it
                spacings = [unique_spacings[0]]
            dt.append(spacings if len(spacings) == 1 else None)
        return np.asarray(dt)

    @property
    def fit_info(self):
        """Name and location of the class used to perform the optimization."""
        name = self.fit.__class__.__name__
        path = inspect.getfile(self.fit.__class__)
        return {"name": name, "location": path}

    @property
    def start_info(self):
        """Name and location of the class used to choose starting points to the
        optimization.
        """
        name = self.start.__class__.__name__
        path = inspect.getfile(self.start.__class__)
        return {"name": name, "location": path}
