import numpy as np
from profile_likelihood import profile_likelihood

try:
    from . import setup_test as st
except ImportError:
    import setup_test as st

# Define the centers of the computation,  which are the best-fit and the
# reverse of the best-fit
best_fit = st.best_fit
best_fit_2 = st.best_fit[::-1]
center = np.row_stack((best_fit_2, best_fit))

# Define the bounds. The first bound is [2, 2.5], and the second bound is
# [1, 2]. If the computation is done correctly, then the profile likelihood path
# will be continuous.
bounds = [[best_fit[1], 2.5], [best_fit_2[1], best_fit_2[0]]]

# Define the likelihood object
likelihood = profile_likelihood(st.myexp, len(best_fit), len(st.t))

# Run the computation
res = likelihood.compute(center, bounds=bounds, dt=st.dt)


def test_center():
    """Test if the argument ``center`` is stored correctly as an attribute."""
    assert np.allclose(
        likelihood.center, center
    ), "Problem in storing the center points"


def test_continuity_points():
    """Test if the fixed parameter points are created properly by checking if
    the points are continuous at the overlapping bound, which is at 2.
    """
    # Continuity points to check
    p0 = res["parameter0"]["parameters"][0]
    p1 = res["parameter1"]["parameters"][0]

    assert np.allclose(p0, p1, atol=1e-1), "The points are not continuous"


if __name__ == "__main__":
    test_center()
    test_continuity_points()
