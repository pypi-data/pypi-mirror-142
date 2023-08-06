import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import warnings
import traceback

_dpi = 300


class Plots:
    """Collections of methods to plot the results of profile
    likelihood computation.
    """

    def plot_profiles(
        self,
        idx="all",
        axes=None,
        bounds=None,
        xlabels="default",
        cplabel="cost",
        cplim=None,
        cpscale="linear",
        aspect="auto",
        cpkwargs=None,
    ):
        """Plot cost profiles of the model, i.e. negative loglikelihoods. If
        ``plt.show()`` doesn't show the plot, try to use other backend, like
        TkAgg, Qt5Agg, etc.

        Parameters
        ----------
        idx: {"all", 1d-array}, optional
            Index of the parameters to plot.
            default: "all", which will plot the cost profiles for all
            parameters.

        axes: np.ndarray, optional
            Array of matplotlib Axes. The number of Axes should be at least
            equal to the number of the requested parameter index to plot.
            default: None, which will use an internal function to create the
            Axes.

        bounds: {1d-array, 2d-array}, optional
            Upper and lower bounds of the plot for each parameter, stored in an
            N x 2 array. If a 1D array is given, the array will be copied to
            make a 2D array. If a 2D array is given, each row should correspond
            to different parameter, the first column contains the lower bounds
            and the second column the upper bounds.
            default: None

        xlabels: {"default", list of str}, optional
            List of labels that will be written on the x axis on each plot.
            This list should have the same length as the number parameters in
            the model.
            default: "default", which uses ``self.param_names``

        cplabel: str, optional
            String to write as the label of the vertical axis of the cost
            profile plot.
            default: "cost"

        cplim: {None, 1d-array, 2d-array}, optional
            List of upper bounds and lower bounds for each parameter, stored In
            an N x 2 array. Each row correspond to different parameter, column 1
            contains the lower bounds, and column 2 the upper bounds. For now,
            the array needs to contain the bounds for the complete parameters.
            default: None

        cpscale: {"linear", "log"}, optional
            Scaling to use in the y-axis of cost profile plots. Same yscale
            function in ``matplotlib.pyplot``.
            default: "linear"

        aspect: {"auto", "equal", float}, optional
            An option to set the aspect ratio of the plots. It is the same as
            the aspect argument in ``matplotlib.axes.Axes.set_aspect``.
            default: "auto"

        cpkwargs: dict (optional)
            Optional ``Line2D`` properties to customize the profile likelihood
            plots.
            default: {"c": "tab:blue"}

        Returns
        -------
        axes: list
            Axes object of the plots.
        """
        # Retrieve the profile likelihood results
        best_results = self.best_results

        # Process and set plotting variables
        self._set_plot_vars(idx, bounds, xlabels, aspect)
        self._set_plot_profiles_vars(cplim, cpscale, cplabel)
        _, cpkwargs = self._set_plot_kwargs(cpkwargs=cpkwargs)

        # Create the canvas and axes
        nrows, ncols = self._get_nrows_ncols_cost(len(self._plot_idx))
        axes, nwors, ncols = self._set_axes(axes, nrows, ncols, True)
        print(f"Generating {len(self._plot_idx)} plots of cost profile")

        if ncols == 1:
            if nrows == 1:
                # Case where there is only 1 cost profile to plot
                self._plot_one_profile(
                    best_results, axes, self._plot_idx[0], **cpkwargs
                )
                self._labels_ticks_handler_diag(axes, self._plot_idx[0], 1)
            else:
                # Case where there are 2 cost profiles to plot
                for kk, idxx in enumerate(self._plot_idx):
                    self._plot_one_profile(
                        best_results, axes[kk], idxx, **cpkwargs
                    )
                    self._labels_ticks_handler_diag(axes[kk], idxx, 1)
        else:
            # Case where there are > 2 cost profiles to plot
            for ii in range(nrows):
                for jj in range(ncols):
                    kk = ii * ncols + jj
                    if kk >= len(self._plot_idx):
                        axes[ii, jj].axis("off")
                    else:
                        self._plot_one_profile(
                            best_results,
                            axes[ii, jj],
                            self._plot_idx[kk],
                            **cpkwargs,
                        )
                        self._labels_ticks_handler_diag(
                            axes[ii, jj], self._plot_idx[kk], 1
                        )
        return axes

    def plot_paths(
        self,
        idx="all",
        axes=None,
        bounds=None,
        xlabels="default",
        aspect="auto",
        pkwargs=None,
    ):
        """Plot profile likelihood paths. The paths are projected onto 2D
        planes in parameter space.

        Parameters
        ----------
        idx: {"all", 1d-array}, optional
            Index of the parameters to plot. If "all" is given, then the paths
            for all parameters will be plotted. If an array of length 2 is
            given, the parameter correspond to the first element is plotted on
            the x-axis. It can receive an array with length > 2 as well.
            default: "all"

        axes: np.ndarray, optional
            Array of matplotlib Axes.
            default: None, which will use an internal function to create the
            Axes.

        bounds: {1d-array, 2d-array}, optional
            Upper and lower bounds of the plot for each parameter, stored in an
            N x 2 array. If a 1D array is given, the array will be copied to
            make a 2D array. If a 2D array is given, each row should correspond
            to different parameter, the first column contains the lower bounds
            and the second column the upper bounds.
            default: None

        xlabels: {"default", list of str}, optional
            List of labels that will be written on the x axis on each plot.
            This list should have the same length as the number parameters in
            the model.
            default: "default", which uses ``self.param_names``

        aspect: {"auto", "equal", float}, optional
            An option to set the aspect ratio of the plots. It is the same as
            the aspect argument in ``matplotlib.axes.Axes.set_aspect``.
            default: "auto"

        pkwargs: dict {"x": {}, "y": {}}, optional
            Optional Line2D properties to customize the profile likelihood
            paths. ``pkwargs["x"]`` contains properties to customize the path
            which has fixed parameter plotted on the horizontal axis, and
            similarly ``pkwargs["y"]`` is used for the other path.
            default: {"x": {"ls": "--", "c": "tab:blue"},
                      "y": {"c": "tab:orange"}}

        Returns
        -------
        axes: list
            Axes object of the plots.
        """

        # Retrieve the profile likelihood results
        best_results = self.best_results

        # Process and set the plotting variables
        self._set_plot_vars(idx, bounds, xlabels, aspect)
        pkwargs, _ = self._set_plot_kwargs(pkwargs=pkwargs)

        if len(self._plot_idx) == 1:
            # Plot the paths when only 1 parameter is requested. This will
            # plot all profile likelihood paths corresponding to the requested
            # parameter, i.e., there will be ``self.nparams - 1`` axes.
            idx2 = np.delete(np.arange(self.nparams), self._plot_idx)

            # Create the canvas and axes
            nrows = 1
            ncols = len(idx2)
            axes, _, _ = self._set_axes(axes, nrows, ncols)
            print(f"Generating {ncols} plots of profile likelihood paths.")

            for ii, idxx in enumerate(idx2):
                try:
                    ax = axes[ii]
                except IndexError:
                    ax = axes
                self._plot_paths_one_axis(
                    best_results,
                    ax,
                    idxx,
                    self._plot_idx[0],
                    plotboth=False,
                    **pkwargs,
                )
                self._labels_ticks_handler_lower(
                    ax, idxx, self._plot_idx[0], 1, ii
                )

        else:
            # Plot the paths with multiple parameters requested.
            # Create the canvas and axes
            nrows = ncols = len(self._plot_idx) - 1
            axes, _, _ = self._set_axes(axes, nrows, ncols)
            print(
                f"Generating {sc.special.comb(len(self._plot_idx), 2, True)}"
                " plots of profile likelihood paths."
            )

            if nrows == 1 and ncols == 1:
                # If only 2 indices specify, plot both on 1 axis.
                idxx, idxy = self._plot_idx
                self._plot_paths_one_axis(
                    best_results, axes, idxx, idxy, **pkwargs
                )
                self._labels_ticks_handler_lower(axes, idxx, idxy, 1, 0)
            else:
                # If number of indices > 2, plot in lower triangular matrix.
                for jj, idxy in enumerate(self._plot_idx[1:]):  # rows
                    for ii, idxx in enumerate(self._plot_idx[:-1]):  # columns
                        if ii > jj:  # Turn off upper triangular axis
                            axes[jj, ii].axis("off")
                        else:
                            irow = nrows - jj
                            self._plot_paths_one_axis(
                                best_results,
                                axes[jj, ii],
                                idxx,
                                idxy,
                                **pkwargs,
                            )
                            self._labels_ticks_handler_lower(
                                axes[jj, ii], idxx, idxy, irow, ii
                            )
        return axes

    def plot_paths_and_profiles(
        self,
        idx="all",
        axes=None,
        bounds=None,
        xlabels="default",
        cplabel="cost",
        cplim=None,
        cpscale="linear",
        aspect="auto",
        pkwargs=None,
        cpkwargs=None,
    ):
        """Plot both the paths and the cost profile. The paths will be plotted
        on the lower diagonal while the cost profile on the diagonal. It is
        pretty much combination of
        :meth:`~profile_likelihood.plot_paths` and
        :meth:`~profile_likelihood.plot_profiles`.

        For the parameters and what this returns, see
        :meth:`~profile_likelihood.plot_paths` and
        :meth:`~profile_likelihood.plot_profiles`
        """

        best_results = self.best_results
        self._set_plot_vars(idx, bounds, xlabels, aspect)
        self._set_plot_profiles_vars(cplim, cpscale, cplabel)
        pkwargs, cpkwargs = self._set_plot_kwargs(
            pkwargs=pkwargs, cpkwargs=cpkwargs
        )

        if len(self._plot_idx) == 1:
            # If only 1 index specified, plot projection of the paths and the
            # cost profile at the end, all in 1 row.
            idx2 = np.delete(np.arange(self.nparams), self._plot_idx)

            # Create the canvas and axes
            nrows = 1
            ncols = len(idx2) + 1
            axes, _, _ = self._set_axes(axes, nrows, ncols)
            print(f"Generating {ncols}" " plots of profile likelihood paths.")

            for ii, idxx in enumerate(idx2):
                # Plot paths
                self._plot_paths_one_axis(
                    best_results,
                    axes[ii],
                    idxx,
                    self._plot_idx[0],
                    plotboth=False,
                    **pkwargs,
                )
                self._labels_ticks_handler_lower(
                    axes[ii], idxx, self._plot_idx[0], 1, ii
                )

            # Plot cost profile
            self._plot_one_profile(
                best_results, axes[-1], self._plot_idx[0], **cpkwargs
            )
            self._labels_ticks_handler_diag(axes[-1], self._plot_idx[0], 1)

        else:
            # In any other cases, plot paths on the lower triangular and
            # cost profiles on the diagonal.
            # Create the canvas and axes
            nrows = ncols = len(self._plot_idx)
            axes, _, _ = self._set_axes(axes, nrows, ncols)
            print(
                "Generating "
                f"{sc.special.comb(len(self._plot_idx), 2, True, True)} "
                "plots of profile likelihood and the paths."
            )

            for jj, idxy in enumerate(self._plot_idx):  # rows
                for ii, idxx in enumerate(self._plot_idx):  # columns
                    if ii > jj:  # Turn off upper triangular axes
                        axes[jj, ii].axis("off")
                    else:
                        irow = nrows - jj
                        if ii == jj:  # Plot cost profile
                            self._plot_one_profile(
                                best_results, axes[jj, ii], idxx, **cpkwargs
                            )
                            self._labels_ticks_handler_diag(
                                axes[jj, ii], idxx, irow
                            )
                        else:  # Plot paths
                            self._plot_paths_one_axis(
                                best_results,
                                axes[jj, ii],
                                idxx,
                                idxy,
                                **pkwargs,
                            )
                            self._labels_ticks_handler_lower(
                                axes[jj, ii], idxx, idxy, irow, ii
                            )
        return axes

    ##################################################################
    ##################################################################
    ##################################################################

    def _set_axes(self, axes, nrows: int, ncols: int, cost: bool = False):
        """Prepare the plotting axes, including creating the canvas and setting
        up the grids.

        Parameters
        ----------
        axes: np.ndarray
            Array of Axes.
        nrows: int
            Number of rows on the canvas.
        ncols: int
            Number of columns ont he canvas.
        cost: bool, optional
            A flag to indicate whether the function is used by ``plot_profile``
            function. The assertion of the shape of the axes is different for
            ``plot_profile`` function

        Returns
        -------
        axes: list
            Matplotlib axes.
        """
        if axes is None:
            _, axes = plt.subplots(
                nrows=nrows,
                ncols=ncols,
                dpi=_dpi,
                figsize=(ncols, nrows),
                facecolor="w",
            )
        else:
            shape = np.array(axes).shape
            if cost:
                assert np.prod(shape) >= len(
                    self._plot_idx
                ), f"Need to supply at least {len(self._plot_idx)} axes"
            else:
                assert shape == (
                    nrows,
                    ncols,
                ), f"The axes needs to be {nrows} by {ncols}"
            nrows, ncols = shape
        return axes, nrows, ncols

    def _plot_one_profile(self, best_results, axis, idx_plot, **cpkwargs):
        """Plot cost profile of 1 parameter.

        Parameters
        ----------
        best_results: dict
            A dictionary containing only the best calculation results from
            multiple starting points.
        axis: Matplotlib axis
            Axis of the plot.
        idx_plot: int
            Index of the plot axis, which is also index of parameter to plot.
        **cpkwargs
            Matplotlib ``Line2D`` properties.
        """
        # Get the profile likelihood data of the requested parameter
        pl_data = best_results[self.param_names[idx_plot]]

        # Set the thickness of the frame to 0.1 pt
        for ax in ["top", "bottom", "left", "right"]:
            axis.spines[ax].set_linewidth(0.1)

        # Extract data to plot
        xdata = pl_data["parameters"][:, idx_plot]
        ydata = pl_data["cost"]

        # Plot the cost profile
        axis.plot(xdata, ydata, **cpkwargs)
        axis.set_yscale(self._plot_cpscale)
        # Set the scaling in y axis
        if self._plot_cpscale == "linear":
            axis.ticklabel_format(axis="y", useOffset=True, useMathText=True)
            text = axis.yaxis.get_offset_text()  # Get the text object
            text.set_size(6)  # Set the size.
        elif self._plot_cpscale == "log":
            axis.tick_params(
                axis="y",
                which="minor",
                labelsize=2,
                pad=0.5,
                size=1,
                width=0.5,
                right=False,
            )

        # Set bounds
        self._set_lim(axis, self._plot_bounds, idx_plot, "x")  # set xlim
        self._set_lim(axis, self._plot_cplim, idx_plot, "y")  # set ylim
        self._set_aspect_ratio(axis)

    def _plot_paths_one_axis(
        self,
        best_results,
        axis,
        idxx,
        idxy,
        plotboth=True,
        **pkwargs,
    ):
        """Plot the profile likelihood path(s) on 1 axis.

        Parameters
        ----------
        best_results: dict
            A dictionary containing only the best calculation results.
        axis: Matplotlib axis
            Axis of the plot.
        idxx: int
            Index parameter that is plotted in x direction.
        idxy: int
            Index parameter that is plotted in y direction.
        plotboth: bool
            Flag to plot both paths.
        **pkwargs
            Matplotlib ``Line2D`` properties for the plot of the paths.
        """

        # Set the thickness of the frame to 0.1 pt
        for ax in ["top", "bottom", "left", "right"]:
            axis.spines[ax].set_linewidth(0.1)

        # Plot the paths
        self._plot_one_path(best_results, axis, idxx, idxy, "y", **pkwargs)
        if plotboth:
            self._plot_one_path(best_results, axis, idxx, idxy, "x", **pkwargs)

        # Set bounds
        self._set_lim(axis, self._plot_bounds, idxx, "x")  # set xlim
        self._set_lim(axis, self._plot_bounds, idxy, "y")  # set ylim
        self._set_aspect_ratio(axis)

    def _plot_one_path(
        self, best_results, axis, idxx, idxy, direction, **pkwargs
    ):
        """Plot only one profile likelihood path on each axis.

        Parameters
        ----------
        best_results: dict
            A dictionary containing only the best calculation results.
        axis: Matplotlib axis
            Axis of the plot.
        idxx: int
            Index parameter that is plotted in x direction.
        idxy: int
            Index parameter that is plotted in y direction.
        direction: {"x", "y"}
            Which path to plot, along the x or y direction.
        **pkwargs
            Matplotlib keyword arguments for the paths.
        """
        if direction == "x":
            idx = idxx
        elif direction == "y":
            idx = idxy

        try:
            params = best_results[self.param_names[idx]]["parameters"]
            axis.plot(params[:, idxx], params[:, idxy], **pkwargs[direction])
        except KeyError:
            print(traceback.format_exc())
            warnings.warn(f"Result not found for {self.param_names[idx]}")

    def _labels_ticks_handler_lower(self, axis, idxx, idxy, irow, col):
        """Handle axes labels and ticks of the plots located below the
        diagonal, which typically are the plots of profile likelihood paths.

        Parameters
        ----------
        axis: Matplotlib axis
            Axis of the plot.
        idxx: int
            Index parameter that is plotted in x direction.
        idxy: int
            Index parameter that is plotted in y direction.
        irow: int
            Index of row, inverted, i.e. smaller row number correspond to the
            bottom row. The smallest index is 1.
        col: int
            Index of column.
        """
        # Set the ticks parameters in general
        axis.tick_params(
            axis="both", which="major", labelsize=4, pad=0.5, size=1, width=0.5
        )
        axis.tick_params(
            axis="both", which="minor", labelsize=2, pad=0.5, size=1, width=0.5
        )

        if col == 0:  # The plots on the left edge
            if np.ndim(self._plot_bounds) > 0 and irow > 1:
                axis.set_xticks([])
            axis.set_ylabel(self._plot_xlabels[idxy], fontsize=6, labelpad=0.5)
        if irow == 1:  # The plots on the bottom edge
            if np.ndim(self._plot_bounds) > 0 and col > 0:
                axis.set_yticks([])
            axis.set_xlabel(self._plot_xlabels[idxx], fontsize=6, labelpad=0.5)
        if col > 0 and irow > 1:  # The plot on the bottom left corner
            if np.ndim(self._plot_bounds) > 0:
                axis.set_xticks([])
                axis.set_yticks([])

    def _labels_ticks_handler_diag(self, axis, idx, irow):
        """Handle axes labels and ticks of the plots located on the diagonal,
        which typically are the plots of cost profile.

        Parameters
        ----------
        axis: Matplotlib axis
            Axis of the plot.
        idx: int
            Index parameter.
        irow: int
            Index of row, inverted, i.e. smaller row number correspond to the
            bottom row. The smallest index is 1.
        """
        # Set the ticks parameters in general
        axis.tick_params(
            axis="both", which="major", labelsize=4, pad=0.5, size=1, width=0.5
        )
        axis.tick_params(
            axis="both", which="minor", labelsize=2, pad=0.5, size=1, width=0.5
        )

        # Put the ticks and label on the right
        axis.yaxis.tick_right()
        axis.yaxis.set_label_position("right")
        axis.set_ylabel(
            self._plot_cplabel, fontsize=6, labelpad=5, rotation=-90
        )

        if irow > 1:  # The plots not on the bottom edge
            if np.ndim(self._plot_bounds) > 0:
                axis.set_xticks([])
        elif irow == 1:  # The plot on the bottom right corner
            axis.set_xlabel(self._plot_xlabels[idx], fontsize=6, labelpad=0.5)

    def _set_plot_vars(self, idx, bounds, xlabels, aspect):
        """Set general variables used in the plotting process.

        Parameters
        ----------
        idx: {int, list}
            List of parameter indices requested.
        bounds: list
            Bounds of the plots.
        xlabels: list of str
            Labels of the plots, typically be the name of parameters.
        aspect: float
            Aspect ratio of each plot.
        """
        self._plot_idx = self._get_plot_idx(idx)
        self._plot_bounds = self._get_plot_bounds(bounds)
        self._plot_xlabels = self._get_plot_xlabels(xlabels)
        self._plot_aspect = aspect

    def _set_plot_profiles_vars(self, cplim, cpscale, cplabel):
        """Set variables specifically used to plot the cost profile.

        Parameters
        ----------
        cplim: list
            Vertical bounds of the cost profile plot.
        cpscale: Matplotlib scale
            Scaling on the vertical axis.
        cplabel: str
            Label of the vertical axis.
        """
        self._plot_cplim = self._get_plot_bounds(cplim)
        self._plot_cpscale = cpscale
        self._plot_cplabel = cplabel

    @staticmethod
    def _set_plot_kwargs(**kwargs):
        """Process the keyword arguments.

        Parameters
        ----------
        **kwargs
            Contains ``pkwargs`` and/or ``cpkwargs``.

        Returns
        -------
        pkwargs, cpkwargs: dict
            ``pkwargs`` and ``cpkwargs``
        """
        pkwargs = {}
        cpkwargs = {}

        # Set keyword arguments for the plots of the paths
        if "pkwargs" in kwargs:
            if kwargs["pkwargs"] is None:
                pkwargs = {
                    "x": {"ls": "--", "c": "tab:blue"},
                    "y": {"c": "tab:orange"},
                }
            else:
                pkwargs = kwargs["pkwargs"]
        # Set keyword arguments for the plots of the cost profile
        if "cpkwargs" in kwargs:
            if kwargs["cpkwargs"] is None:
                cpkwargs = {"c": "tab:blue"}
            else:
                cpkwargs = kwargs["cpkwargs"]
        return pkwargs, cpkwargs

    @staticmethod
    def _get_nrows_ncols_cost(total):
        """Get number of rows and columns of the subplots, to make the resulting
        plots as square as possible.

        Parameters
        ----------
        total: int
            Total number of axes.

        Returns
        -------
        [nrows, ncols]: list
            Number of rows and columns
        """
        ncols = int(round(np.sqrt(total)))
        nrows = int(np.ceil(total / ncols))
        return nrows, ncols

    def _set_aspect_ratio(self, axis):
        """Set aspect ratio of the plots.

        Parameters
        ----------
        axis: Matplotlib axis
            Axis of the plot.
        """
        if self._plot_aspect != "auto":
            if self._plot_aspect == "equal":
                self._plot_aspect = 1

            data_ratio = axis.get_data_ratio()
            axis.set_aspect(self._plot_aspect / data_ratio, "box")

    def _get_plot_idx(self, idx):
        """Process the argument idx. This creates 1d-array of indices.

        Parameters
        ----------
        idx: int or list or "all"
            Indices of parameter requested.

        Returns
        -------
        idx: 1d-array
            List of sorted indices.
        """
        if np.ndim(idx) == 0:
            if idx == "all":
                idx = self.idx
            else:
                idx = [idx]
        elif np.ndim(idx) > 1:
            raise TypeError("Only accept idx as int, or 1D array-like")
        return np.sort(idx)

    def _get_plot_bounds(self, bounds):
        """Process the argument bounds. This creates 2D array of bounds.

        Parameters
        ----------
        bouds: list
            Bounds of the parameters.

        Returns
        -------
        bounds: 2d-array
            Bounds of parameters.
        """
        ndim = np.ndim(bounds)
        if ndim == 1:  # Boundaries for all parameters are the same
            check = False
            if len(bounds) == 2:
                check = np.all([np.ndim(bb) == 0 for bb in bounds])
                if check:
                    bounds = np.tile(bounds, (len(self._plot_idx), 1))
            if len(bounds) > 2 or not check:
                ndim = 2
        if ndim == 2:  # Boundaries for each parameter might be different
            assert len(bounds) == len(
                self._plot_idx
            ), f"Size of bounds needs to be {len(self._plot_idx)} by 2"
            for ii, bb in enumerate(bounds):
                if np.ndim(bb) == 0:
                    if bb is None:
                        bounds[ii] = [None, None]
                    else:
                        raise ValueError("Unknowm argument")
        return np.asarray(bounds)

    def _set_lim(self, axis, bounds, idx_plot, direction):
        """Set the limit of horizontal and/or vertical axes.

        Parameters
        ----------
        axis: Matplotlib axis.
            Axis of the plot.
        bounds: list
            Upper and lower bounds of the plot.
        idx_plot: int
            Index of the axis.
        direction: "x" or "y"
            Horizontal or vertical direction.
        """
        if np.ndim(bounds) > 0:
            try:
                ii = np.where(idx_plot == self._plot_idx)[0][0]
                if direction == "x":
                    axis.set_xlim(bounds[ii, 0], bounds[ii, 1])
                elif direction == "y":
                    axis.set_ylim(bounds[ii, 0], bounds[ii, 1])
            except IndexError:
                pass

    def _get_plot_xlabels(self, xlabels):
        """Process the argument xlabels.

        Parameters
        ----------
        xlabels: list of str or "default"
            Labels of the plots, typically be the name of the parameter.

        Returns
        -------
        xlabels: 1d-array
            Labels to write on the plots' axes.
        """
        if np.ndim(xlabels) == 0 and xlabels == "default":
            xlabels = self.param_names
        elif np.ndim(xlabels) == 1:
            assert (
                len(xlabels) == self.nparams
            ), f"Need to provide {self.nparams} labels"
        return xlabels
