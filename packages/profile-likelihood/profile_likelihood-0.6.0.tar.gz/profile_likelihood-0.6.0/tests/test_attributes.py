import numpy as np
import os
import pytest

try:
    from . import setup_test as st
except ImportError:
    import setup_test as st

this_path = os.path.dirname(os.path.abspath(__file__))
def_path = f"{this_path}/../profile_likelihood/default"
names_orig = ["parameter0", "parameter1"]
names_new = [r"$\theta_0$", r"$\theta_1$"]


def test_model():
    """Test getting information about the model used."""
    model_info = {
        "name": "residuals",
        "location": f"{this_path}/model_exp.py",
    }
    assert (
        st.likelihood.model_info == model_info
    ), "Doesn't show model information properly"


def test_nparams():
    """Test retrieving number of parameters."""
    assert np.equal(
        st.likelihood.nparams, len(st.best_fit)
    ).all(), "Doesn't store number of parameter properly"


def test_npred():
    """Test retrieving number of predictions."""
    assert np.equal(
        st.likelihood.npred, len(st.t)
    ).all(), "Doesn't store number of parameter properly"


def test_param_names_get():
    """Test retrieving parameters' names."""
    assert (
        st.likelihood.param_names == names_orig
    ), "Doesn't store parameter names properly"


def test_param_names_set():
    """Test setting parameters' names."""
    st.likelihood.param_names = names_new
    assert (
        st.likelihood.param_names == names_new
    ), "Doesn't update parameter names properly"
    # Revert param_names back
    st.likelihood.param_names = names_orig


def test_param_names_exception():
    """Test exception in setting parameters' names."""
    with pytest.raises(AssertionError):
        st.likelihood.param_names = "theta0"


def test_start_class():
    """Test getting information of the starting point class."""
    loc = f"{def_path}/single_starting_point.py"
    to_check = []

    # Check the class names
    to_check.append(st.likelihood.start_info["name"] == "single_starting_point")

    # Check the path
    to_check.append(os.path.samefile(st.likelihood.start_info["location"], loc))

    assert np.all(to_check), "Doesn't show start class information properly"


def test_fit_class():
    """Test getting information of the fitting class."""
    loc = f"{def_path}/fit_leastsq.py"
    to_check = []

    # Check the class names
    to_check.append(st.likelihood.fit_info["name"] == "fit_leastsq")

    # Check the path
    to_check.append(os.path.samefile(st.likelihood.fit_info["location"], loc))

    assert np.all(to_check), "Doesn't show fit class information properly"


if __name__ == "__main__":
    test_model()
    test_nparams()
    test_npred()
    test_param_names_get()
    test_param_names_set()
    test_param_names_exception()
    test_start_class()
    test_fit_class()
