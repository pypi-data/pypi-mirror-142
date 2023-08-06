import numpy as np
import pickle
import json
import warnings


avail_ext = ["pkl", "json", "dump"]


def save_results(filename, data):
    """Save data dictionary as JSON file.

    Parameters
    ----------
    filename: str
        Path and filename of the output file
    """
    fname = _check_filename(filename)
    print(f"Save results to {fname} ....")
    with open(fname, "w") as f:
        json.dump(data, f, cls=NumpyArrayEncoder, indent=4)


def load_results(filename, param_names):
    """Load results from the previously saved calculation.

    Parameters
    ----------
    filename: str
        Path to the result file.
    param_names: list
        List of names of the parameters.

    Returns
    -------
    results: dict
        See :meth:`profile_likelihood.compute`.
    """
    _, ext = _split_extension(filename)
    print(f"Load data from {filename} ....")
    if ext == avail_ext[0]:  # pkl
        results = _load_pickle(filename)
    elif ext == avail_ext[1]:  # json
        results = _load_json(filename)
    elif ext == avail_ext[2]:  # dump
        results = _load_dump(filename, param_names)
    param_names = _check_param_names(results, param_names)
    return results, param_names


def _load_pickle(filename):
    """Load results that was saved as a pickle file.

    Parameters
    ----------
    filename: str
        Path to the result file.

    Returns
    -------
    results: dict
        See :meth:`profile_likelihood.compute`.
    """
    with open(filename, "rb") as f:
        results = pickle.load(f)
    return results


def _load_json(filename):
    """Load results that was saved as a json file.

    Parameters
    ----------
    filename: str
        Path to the result file.

    Returns
    -------
    results: dict
        See :meth:`profile_likelihood.compute`.
    """
    with open(filename, "r") as f:
        results = json.load(f)

    # Decoding to ndarray
    for param in results:
        for key in results[param]:
            if isinstance(results[param][key], list):
                results[param][key] = np.array(results[param][key])
    return results


def _load_dump(filename, param_names):
    """Load result dictionary from the dump file.

    Parameters
    ----------
    filename: str
        Path to the result file.
    param_names: list of str
        List of names of parameters of the model.

    Returns
    -------
    results: dict
        See :meth:`profile_likelihood.compute`.
    """
    dump_mat = _dumpdata_to_matrix(filename)
    results = _dumpmat_to_dict(dump_mat, param_names)
    return results


def _dumpdata_to_matrix(dumpfile):
    """Load the results in the dump file and put it into a matrix.

    Parameters
    ----------
    dumpfile: str
        Path and name of the dump file.

    Returns
    -------
    dump_mat: 2d ndarray
        Matrix containing information loaded from dump file, sorted by the index
        of fixed parameter.
    """
    dfile = np.genfromtxt(dumpfile, delimiter="; ", dtype=str)
    dump_mat = np.empty(0)
    for ii, data in enumerate(dfile):
        idx = int(data[0].split(":")[1])
        error = int(data[1].split(":")[1])
        parameters = np.asarray((data[2].split(":")[1]).split(","), dtype=float)
        cost = float(data[3].split(":")[1])
        toappend = np.concatenate(([idx], [error], parameters, [cost]))

        # Put these information into a matrix
        if ii:
            dump_mat = np.row_stack((dump_mat, toappend))
        else:
            dump_mat = np.append(dump_mat, toappend)

    # Sort by fixed parameter index
    idx_sorted = np.argsort(dump_mat[:, 0])
    dump_mat = dump_mat[idx_sorted]

    return dump_mat


def _dumpmat_to_dict(dump_mat, param_names):
    """Convert matrix from the dump file to a dictionary, in the same format as
    ```profile_likelihood.results``.

    Parameters
    ----------
    dump_mat: 2d ndarray
        Matrix containing information loaded from dump file, sorted by the index
        of fixed parameter.
    param_names: list of str
        List of names of parameters of the model.

    Returns
    -------
    dump_dict: dict
        Dictionary containing information from dump file.
    """
    avail_idx = np.unique(dump_mat[:, 0])  # List of available index

    dump_dict = {}
    for ii, name in enumerate(param_names):
        if ii in avail_idx:
            # If computation results for index ii is found, process the matrix
            # and create a dictionary

            # Get part of matrix containing information for parameter index idx
            name_idx = np.where(dump_mat[:, 0] == ii)[0]
            name_mat = dump_mat[name_idx]

            # Sort name_mat by the fixed parameter value
            idx_sort = np.argsort(name_mat[:, ii + 2])
            name_mat = name_mat[idx_sort]

            # Extract the data, similar format to data in profile_likelihood
            # Column 0 contains idx
            error_code = name_mat[:, 1]
            parameters = name_mat[:, 2:-1]
            cost = name_mat[:, -1]
            others = np.empty((len(cost), 0))

            # Dictionary to append into dump_dict
            toappend_dict = {
                name: {
                    "error_code": error_code,
                    "parameters": parameters,
                    "others": others,
                    "cost": cost,
                }
            }
        else:
            # If result for index ii is not found, then return an empty
            # dictionary, just like the convention for parameters that are not
            # calculated.
            toappend_dict = {name: {}}

        # Append the dictionary to dump_dict
        dump_dict.update(toappend_dict)
    return dump_dict


def _check_filename(filename):
    """Check if filename argument has JSON extension.

    Parameters
    ----------
    filename: str
        Path and filename of the output file

    Returns
    -------
    filename: str
        Filename with the `.json` extension.
    """
    fname, ext = _split_extension(filename)
    if not ext or ext not in avail_ext:
        warnings.warn("Working with a pickle file")
        ext = "json"
    filename = ".".join([fname, ext])
    return filename


def _split_extension(filename):
    """Get the extension of filename, if it is available.

    Parameters
    ----------
    filename: str
        Path and filename of the output file

    Returns
    -------
    fname: str
        File name without extension.
    extension: str
        File extension founr in filename. This can be None if no extension
        found.
    """
    fname = filename.split(".")
    if len(fname) > 1:
        extension = fname.pop()
    else:
        extension = None
    fname = ".".join(fname)
    return fname, extension


def _check_param_names(results, param_names):
    """Check if parameters names given is the same as those stored from the
    previous calculation, then change it to match the previous calculation if
    they are different.

    Parameters
    ----------
    results : dict
        Results dictionary from previous calculation.
    param_names : list
        Names of the parameters

    Returns
    -------
    param_names: list
        Updated parameters names
    """
    keys = list(results)
    if np.any(param_names != keys):
        print("Change param_names to result dictionary keys.")
        param_names = keys
    return param_names


class NumpyArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
