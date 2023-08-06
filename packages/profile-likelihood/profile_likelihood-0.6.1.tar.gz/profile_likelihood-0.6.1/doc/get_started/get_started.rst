.. _get_started:

===========
Get started
===========

Installation
============

From source

.. code:: bash

   $ git clone https://git.physics.byu.edu/yonatank/profile_likelihood.git
   $ cd profile_likelihood
   $ pip install -e .  # Install the package
   $ python -m pytest .  # Run test


Basic usage
===========

As an example, we want to run profile likelihood calculation to sum of
exponential model

.. math::
   f\left(\vec{\theta}; t\right) = \exp(-\theta_1 t) + \exp(-\theta_2 t),

with ``t = [1.0, 1.2, 2.0]`` and data ``y = [0.50, 0.40, 0.15]``.

.. code:: python

   import numpy as np
   from profile_likelihood import profile_likelihood

   tdata = np.array([1.0, 1.2, 2.0]).reshape((-1, 1))  # Sampling time
   ydata = np.array([0.50, 0.40, 0.15])  # Mock data

   def residuals(theta):
	   """The function, representing the model, that will be used in the
	   optimization process. This function takes an array of parameter and return
	   an array of the residuals.
	   """
	   pred = np.sum(np.exp(-theta * tdata), axis=1)  # Model that gives predictions
	   return ydata - pred  # Return the residual vector.

   best_fit = np.array([1.0, 2.0])  # Best-fit parameter
   nparams = len(best_fit)  # Number of parameters
   npred = 3  # Number of predictions

   # Create likelihood object
   likelihood = profile_likelihood(residuals, nparams, npred)

   # Run computation
   likelihood.compute(best_fit)

   # Access results
   likelihood.results

For more examples, see
`here <https://git.physics.byu.edu/yonatank/profile_likelihood/tree/v1.0.1/examples>`__.
