.. _howto:

========
Examples
========

List of (incomplete) examples about using ``profile_likelihood``:

1. `Basic
   computation <https://git.physics.byu.edu/yonatank/profile_likelihood/blob/add-doc/examples/basic_computation.ipynb>`__
   We show a minimum implementation on how to compute the profile likelihood of the model.

2. `Geometric
   representation <https://git.physics.byu.edu/yonatank/profile_likelihood/blob/add-doc/examples/geometric_representation.ipynb>`__
   In this example, we compare the profile likelihood paths to the cost contour of the model and show that the paths follows the direction of the canyon.
   We will also give some interpretation of the results.

3. `Parallel
   computing <https://git.physics.byu.edu/yonatank/profile_likelihood/blob/add-doc/examples/parallel_computing.ipynb>`__
   We show how to use multiprocessing to compute profile likelihood.
   The process will be divided per parameter.

4. `Custom fixed
   points <https://git.physics.byu.edu/yonatank/profile_likelihood/blob/add-doc/examples/custom_fixed_points.ipynb>`__
   Sometimes, cleverly choosing the points to do the computation can result in more efficient process.
   For example, around the region where the canyon curves, we would want to have more points to capture the shape of the canyon.
   On the other hand, in some region the canyon might look like a line (the canyon doesn't curve significantly).
   In this case, we don't need as much point to capture the shape of the canyon.
   This can possibly speed up the computation, because we can require fewer number of points in our computation.

   To show this, we will compare the results of profile likelihood computation using the sum of exponentials model.
   We will run the computation using linearly spaced points (using the internal algorithm to generate the points) and some custom points.
   We will compare the time to run for each computation.
   Additionally, we will also compare the results qualitatively by plotting the profile likelihood paths on the cost contour and comparing the profile likelihood.

5. `Multiple starting
   points <https://git.physics.byu.edu/yonatank/profile_likelihood/blob/add-doc/examples/multiple_starting_points.ipynb>`__
   We note that usually the results from the optimization algorithm depends on the initial guess, especiallly when the function to optimize has multiple local minima.
   In the case where there are multiple local minima on cost contour, we might want to use several trial starting points to find those minima.
   In this example, we want to show how user can define custom class to choose starting points and to use multiple initial guess' in the optimization algorithm.
   The comparison to the results will be done internally.

6. `Custom fitting
   routine <https://git.physics.byu.edu/yonatank/profile_likelihood/blob/add-doc/examples/custom_fitting.ipynb>`__
   We show how to use custom fitting routine, besides the default one provided.
   Additionally, we compare the results of profile likelihood computations using the default fitting class and the custom fitting class.

7. `Save and load
   results <https://git.physics.byu.edu/yonatank/profile_likelihood/blob/add-doc/examples/save_and_load.ipynb>`__
   It will be useful to save the results of profile likelihood computation for future use and to load the results again later.
   This is especially convenient when the computation is slow.

8. `Plotting
   routines <https://git.physics.byu.edu/yonatank/profile_likelihood/blob/add-doc/examples/plotting_routines.ipynb>`__
   Here, we show how to use internal function to plot the results of profile likelihood calculation.
   There are 3 plotting routines available: :meth:`profile_likelihood.profile_likelihood.plot_profiles`, :meth:`profile_likelihood.profile_likelihood.plot_paths`, and :meth:`profile_likelihood.profile_likelihood.plot_paths_and_profiles`.
