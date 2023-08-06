import numpy as np

try:
    from . import setup_test as st
except ImportError:
    import setup_test as st

"""What to test here?
* format dumpfile - compare the first line
* load dumpfile - compare it to results_json
"""
dump_compare = ["idx:0", "error:1", "parameters:1.0,2.0", "cost:0.0"]


def test_dumpfile_text():
    """Test if the text information in the dump file what we want: idx, error,
    parameters, and cost.
    """
    for DC, DR in zip(dump_compare, st.dump_raw[0]):
        dc = DC.split(":")
        dr = DR.split(":")

        for ii in range(2):
            assert dc[ii] == dr[ii], f"Dumped info {dr[0]} is not correct."


def test_dumpfile_empty_dict():
    """Test if the dictionary generated from dump file contains empty
    dictionary for parameters that were not calculated.
    """
    dict_dump = st.results_dump["parameter1"]
    assert not dict_dump


def test_dumpfile_dict():
    """Test if information loaded from dump file is the same as the results of
    the computation.
    """
    dict_dump = st.results_dump["parameter0"]
    dict_orig = st.results_p["parameter0"]
    for key in dict_dump:
        data_json = dict_dump[key]
        data_orig = dict_orig[key]
        if not data_json.size:
            assert np.allclose(data_json, data_orig)


if __name__ == "__main__":
    test_dumpfile_text()
    test_dumpfile_empty_dict()
    test_dumpfile_dict()
