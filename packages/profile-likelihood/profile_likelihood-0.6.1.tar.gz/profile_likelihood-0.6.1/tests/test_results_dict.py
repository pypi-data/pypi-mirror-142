import numpy as np
import copy
import pytest

try:
    from . import setup_test as st
except ImportError:
    import setup_test as st

param_names = ["parameter0", "parameter1"]
normal_keys = ["error_code", "parameters", "others", "cost"]
error_keys = ["error_code", "parameters", "cost", "traceback"]

PL = copy.deepcopy(st.likelihood)


def test_parameter_names():
    """Test if the result dictionary has the correct parameter names as its
    keys.
    """
    assert all(
        [p1 == p2 for p1, p2 in zip(list(st.results_b), param_names)]
    ), "Problem with parameter names in results dictionary keys"


def test_dictionary_param_not_calculated():
    """Test if the dictionary for the parameters that are not calculated is
    empty.
    """
    assert not bool(
        st.results_b[param_names[1]]
    ), "Problem with dictionary of not-calculated parameter"


def test_results_keys():
    """Test if the dictionary for every parameters in results dictionary has
    the correct keys.
    """
    assert all(
        [
            p1 == p2
            for p1, p2 in zip(list(st.results_b[param_names[0]]), normal_keys)
        ]
    ), "Problem with dictionary keys for calculated parameter"


def test_error_raised():
    """Test if an error is raised when the argument ``ignore_error`` is set to
    False. To check this, we run a serial computation for all index using a fit
    class that doesn't meet the requirements, and setting ``ignore_error`` to
    be ``False``. Then, we use ``pytest`` if a specific exception is raised.
    """
    with pytest.raises(AttributeError):
        _ = PL.compute(st.best_fit, fit_class=st.fit, ignore_error=False)


def test_results_keys_error():
    """Test if the dictionary for the parameters that has an error in the
    computation has the correct keys. This can also be used to make sure an
    error is captured byt the results.
    """
    assert all(
        [
            p1 == p2
            for p1, p2 in zip(list(st.results_e[param_names[0]]), error_keys)
        ]
    ), "Problem with dictionary keys for calculated parameter with error"


if __name__ == "__main__":
    test_parameter_names()
    test_dictionary_param_not_calculated()
    test_results_keys()
    test_error_raised()
    test_results_keys_error()
