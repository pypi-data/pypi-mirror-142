import numpy as np

try:
    from . import setup_test as st
except ImportError:
    import setup_test as st

target_b = st.data_b["parameter0"]["cost"]
target_p = st.data_p["parameter0"]["cost"]

cost_b = st.results_b["parameter0"]["cost"]
cost_p = st.results_p["parameter0"]["cost"]


def test_cost_bounds():
    """Test the cost value when running computation by specifying bounds."""
    assert np.allclose(
        cost_b, target_b, atol=1e-5
    ), "Problem in parameter result when specifying bounds"


def test_cost_points():
    """Test the cost value when running computation by specifying points."""
    assert np.allclose(
        cost_p, target_p, atol=1e-5
    ), "Problem in parameter result when specifying points"


if __name__ == "__main__":
    test_cost_bounds()
    test_cost_points()
