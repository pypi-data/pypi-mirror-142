from profile_likelihood.save_load import _split_extension
import numpy as np
import copy

try:
    from . import setup_test as st
except ImportError:
    import setup_test as st

points = np.linspace(*st.bounds, st.npoints + 1)[1:]
bounds = copy.copy(st.bounds)
bounds[0] += st.dt


def test_get_extension():
    """Test if the function to get file extension works properly."""
    fname_pkl = st.filename + ".pkl"
    fname_json = st.filename + ".json"

    _, ext_pkl = _split_extension(fname_pkl)
    _, ext_json = _split_extension(fname_json)
    assert ext_pkl == "pkl"
    assert ext_json == "json"


def test_load_pickle():
    """Test if information loaded from pickle file is the same as the results
    saved.
    """
    dict_pkl = st.results_pkl["parameter0"]
    dict_orig = st.results_p["parameter0"]
    for key in dict_pkl:
        data_pkl = dict_pkl[key]
        data_orig = dict_orig[key]
        if not data_pkl.size:
            assert np.allclose(data_pkl, data_orig)


def test_load_json():
    """Test if information loaded from json file is the same as the results
    saved.
    """
    dict_json = st.results_json["parameter0"]
    dict_orig = st.results_p["parameter0"]
    for key in dict_json:
        data_json = dict_json[key]
        data_orig = dict_orig[key]
        if not data_json.size:
            assert np.allclose(data_json, data_orig)


def test_load_points():
    """Test if the loaded result has the same fixed parameter points as the
    original computation.
    """
    print(st.likelihood.param_names)
    assert np.allclose(
        st.likelihood.fixed_params[0], points
    ), "Problem with loading parameter points"


def test_load_bounds():
    """Test if the loaded result has the same parameter bounds as the original
    computation.
    """
    assert np.allclose(
        st.likelihood.bounds, bounds
    ), "Problem with loading parameter bounds"


def test_load_dt():
    """Test if the loaded result has the same parameter spacing as the original
    computation.
    """
    assert np.allclose(
        st.likelihood.dt, st.dt
    ), "Problem with loading parameter spacing"


if __name__ == "__main__":
    test_get_extension()
    test_load_pickle()
    test_load_json()
    test_load_points()
    test_load_points()
    test_load_dt()
