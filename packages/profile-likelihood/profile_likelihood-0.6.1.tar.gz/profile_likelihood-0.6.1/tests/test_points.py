import numpy as np

try:
    from . import setup_test as st
except ImportError:
    import setup_test as st

target_b = st.data_b["parameter0"]["parameters"][:, 0]
target_p = st.data_p["parameter0"]["parameters"][:, 0]

points_b = st.results_b["parameter0"]["parameters"][:, 0]
points_p = st.results_p["parameter0"]["parameters"][:, 0]


def test_length():
    """Test the length of the generated linearly spaced points."""
    assert (
        len(points_b) == st.npoints
    ), "Doesn't create linearly spaced points properly"


def test_bounds():
    """Test if linearly spaced points are withing bounds."""
    to_check = np.all([st.bounds[0] <= ii <= st.bounds[1] for ii in points_b])
    assert to_check, "Doesn't create linearly spaced points properly"


def test_dt():
    """Test if points spacing is dt. ``np.isclose`` is used to prevent error
    due to numerical precission.
    """
    dt = points_b[1:] - points_b[:-1]
    assert [
        np.isclose(ii, st.dt) for ii in dt
    ], "Doesn't create linearly spaced points properly"


def test_points_bounds():
    """Test if linearly spaced points are generated properly."""
    assert np.array_equal(
        points_b, target_b
    ), "Problem in defining fixed points when specifying bounds"


def test_points_points():
    """Test if custom points are splitted properly."""
    assert np.array_equal(
        points_p, target_p
    ), "Problem in defining fixed points when specifying points"


if __name__ == "__main__":
    test_length()
    test_bounds()
    test_dt()
    test_points_bounds()
    test_points_points()
