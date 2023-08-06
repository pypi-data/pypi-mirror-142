import numpy as np
import pickle
import os
from profile_likelihood.profile_likelihood import profile_likelihood

try:
    import model_exp
    import fit_class_test
except ModuleNotFoundError:
    from . import model_exp
    from . import fit_class_test


path = os.path.dirname(os.path.abspath(__file__))

# Load target results
# Target data for calculation specifying bounds and dt
data_b = pickle.load(open(path + "/data_b.pkl", "rb"))

# Target data for calculation specifying points
data_p = pickle.load(open(path + "/data_p.pkl", "rb"))

# Setup profile likelihood object
t = np.array([1.0, 1.2, 2.0])
best_fit = np.array([1, 2])
mydata = np.exp(-1 * t) + np.exp(-2 * t)
myexp = model_exp.residuals
bounds = [0.6, 2.5]
dt = 0.01
npoints = 190
fit = fit_class_test.fit(5)
likelihood = profile_likelihood(myexp, len(best_fit), len(t))
filename = path + "/exp_model_test"

# Compute profile likelihood
# Get results that contains error
results_e = likelihood.compute(
    best_fit, idx=0, bounds=bounds, dt=dt, fit_class=fit, ignore_error=True
)
# Get results with specified bounds
results_b = likelihood.compute(best_fit, idx=0, bounds=bounds, dt=dt)
# Get results with specified fixed points
results_p = likelihood.compute(
    best_fit,
    idx=0,
    points=np.linspace(*bounds, npoints + 1)[1:],
    dumpfile=filename + ".dump",
)

# Save the results with fixed points specified
likelihood.save_results(filename + ".json")

# Load the saved results
results_dump = likelihood.load_results(filename + ".dump", best_fit)
results_json = likelihood.load_results(filename + ".json", best_fit)
results_pkl = likelihood.load_results(filename + ".pkl", best_fit)

# Raw data from dump file
dump_raw = np.genfromtxt(filename + ".dump", delimiter="; ", dtype=str)

# Remove dump file
os.remove(filename + ".dump")

if __name__ == "__main__":
    # Export results_p as a pickle file
    pickle.dump(results_p, open(filename + ".pkl", "wb"))

    # Save results_b and results_p as the correct data to compare
    pickle.dump(results_b, open("data_b.pkl", "wb"))
    pickle.dump(results_p, open("data_p.pkl", "wb"))
