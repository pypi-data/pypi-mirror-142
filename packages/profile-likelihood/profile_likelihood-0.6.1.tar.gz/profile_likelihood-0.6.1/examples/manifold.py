import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

__all__ = ["cost_contour_data", "plot_cost_contour"]


def cost_contour_data(
    cost_func,
    xlist=np.linspace(-5, 5),
    ylist=np.linspace(-5, 5),
):
    # Convert the arrays to numpy arrays
    (
        xlist,
        ylist,
    ) = convert_array_args(xlist, ylist)

    # Get list of parameters
    ThetaX, ThetaY = get_theta(xlist, ylist)

    # Calculate costs
    Cost = get_cost(cost_func, ThetaX, ThetaY)

    return ThetaX, ThetaY, Cost


def plot_cost_contour(
    thetaX_mat, thetaY_mat, Cost_mat, dpi=150, levels="default", scale="lin"
):
    levels = get_levels(levels, Cost_mat, scale)

    # Plot cost contour
    fig = plt.figure(dpi=150, facecolor="w")
    ax = fig.add_subplot(111)
    if scale == "lin":
        im = ax.contourf(thetaX_mat, thetaY_mat, Cost_mat, levels=levels)
    elif scale == "log":
        ub = np.ceil(np.log10(np.max(Cost_mat)))
        lb = np.floor(np.log10(np.min(Cost_mat)))
        im = ax.contourf(
            thetaX_mat,
            thetaY_mat,
            Cost_mat,
            locator=ticker.LogLocator(),
            levels=np.logspace(lb, ub, levels),
        )
    clb = plt.colorbar(im)
    return ax, clb


def convert_array_args(xlist, ylist):
    xlist = np.array(xlist)
    ylist = np.array(ylist)
    return xlist, ylist


def get_theta(xlist, ylist):
    XX, YY = np.meshgrid(xlist, ylist)
    return XX, YY


def get_cost(cost_func, ThetaX, ThetaY):
    Cost = np.empty(ThetaX.shape)
    for ii, (rx, ry) in enumerate(zip(ThetaX, ThetaY)):
        for jj, (cx, cy) in enumerate(zip(rx, ry)):
            params = np.array([cx, cy])
            Cost[ii, jj] = cost_func(params)
    return Cost


def get_levels(levels, Cost, scale):
    if levels == "default":
        if scale == "lin":
            levels = np.linspace(np.min(Cost), np.max(Cost), 50)
        elif scale == "log":
            levels = np.logspace(np.log(np.min(Cost)), np.log(np.max(Cost)), 50)
    return levels
