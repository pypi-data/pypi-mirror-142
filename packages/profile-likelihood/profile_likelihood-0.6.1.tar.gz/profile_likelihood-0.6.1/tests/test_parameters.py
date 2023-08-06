import numpy as np

try:
    from . import setup_test as st
except ImportError:
    import setup_test as st

target_b = st.data_b["parameter0"]["parameters"][:, 1]
target_p = st.data_p["parameter0"]["parameters"][:, 1]

parameters_b = st.results_b["parameter0"]["parameters"][:, 1]
parameters_p = st.results_p["parameter0"]["parameters"][:, 1]


def test_parameters_bounds():
    """Test computation results when using linearly spaced points."""
    assert np.allclose(
        parameters_b, target_b
    ), "Problem in parameter result when specifying bounds"


def test_parameters_points():
    """Test computation results when using custom points."""
    assert np.allclose(
        parameters_p, target_p
    ), "Problem in parameter result when specifying points"


if __name__ == "__main__":
    test_parameters_bounds()
    test_parameters_points()
