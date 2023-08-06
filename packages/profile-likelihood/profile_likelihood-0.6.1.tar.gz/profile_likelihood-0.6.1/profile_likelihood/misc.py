import numpy as np


def insert_parameters(params_to_fit, idx: int, fixed_params: float):
    """Insert the fixed_params into the params_to_fit in the proper
    location.

    Parameters
    ----------
    params_to_fit: list
        Free variable in the function.
    idx: int
        Index of parameter held fixed.
    fixed_params: float
        Value of parameter held fixed.

    Returns
    -------
    parameters: ndarray
        Parameters to input into ``self.model``.
    """
    return np.insert(params_to_fit, idx, fixed_params)


def dict_to_array(result_dict):
    """Convert results from dictionary to matrix/array.

    Parameters
    ----------
    result_dict: dict
        Dictionary to convert.

    Returns
    -------
    save_mat: ndarray
        Array with values obtained from the dictionary.
    """
    nrows = len(result_dict["error_code"])
    save_mat = np.empty((nrows, 0))
    for keys in list(result_dict.keys()):
        to_append = result_dict[keys]
        save_mat = np.column_stack((save_mat, to_append))
    return save_mat


def error_print_style(message):
    """Apply styling to the error message.

    Parameters
    ----------
    message: str
        Error message.

    Returns
    -------
    str
        Error message with styling.
    """
    return f"\033[91m{message}\033[0m"


def check_array_shape(array, shape, array_name):
    """Assert if the array has a correct shape by specifying the shape of the
    intended array.

    Parameters
    ----------
    array: ndarray
        Array to check.
    shape: tuple
        The target shape of the array.
    array_name: str
        Describe the name of the array.
    """
    error_msg = f"The shape of {array_name} needs to be {shape}"
    assert np.shape(array) == shape, error_msg
