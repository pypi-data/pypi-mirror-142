.. _theory:

======
Theory
======

In the problem of fitting a theoretical model :math:`f\left(t_m, \vec{\theta}\right)`
to the :math:`M` experimentally determined data points :math:`y_m` at times
:math:`t_m`, by assuming that the experimental errors for the data points are
independent and Gaussian distributed with standard deviation of :math:`\sigma`,
the probability that a given model produced the observed data points is

.. math::
   P\left(\vec{y}\middle|\vec{\theta}\right) =
   \prod_{m=1}^N \frac{1}{\sqrt{2\pi}\sigma}
   e^{-\left(f(t_m,\vec{\theta}) - y_m\right)^2/2\sigma^2}.

The likelihood function of this model, :math:`L\left(\vec{\theta}\middle|\vec{y}\right)`,
is the probability of the occurrence of the outcomes :math:`\vec{y}` given a set
of parameters :math:`\vec{\theta}` of the model, :math:`P\left(\vec{y}\middle|\vec{\theta}\right)`.
Using the equation above, we can write

.. math::
   L\left(\vec{\theta}\middle|\vec{y}\right) \propto
   \exp\left[ -C\left(\vec{\theta}\right) \right],

where :math:`C\left(\vec{\theta}\right)` is the cost function, given by

.. math::
   C\left(\vec{\theta}\right) = \frac{1}{2} \sum_m
   \left(\frac{y_m - f\left(t_m, \vec{\theta}\right)}
   {\sigma_m} \right)^2.

Suppose the model :math:`f\left(t_m, \vec{\theta}\right)` has :math:`N`
parameters, written as :math:`\{ \theta_1, \cdots, \theta_N \}`. The profile
likelihood of the model for parameter :math:`\theta_j` is the possible maximum
likelihood given the parameter :math:`\theta_j`. The profile likelihood for
parameter :math:`\theta_j` is calculated by setting :math:`\theta_j` to a fixed
value, then maximizing the likelihood function (by minimizing the cost function)
over the other parameters of the model. We repeat this computation across a
range of :math:`\theta_j`, :math:`\left(\theta_j^{\min}, \theta_j^{\max}\right)`.

Computation process
===================

Assuming that the best-fit parameter is the maximum of the likelihood function,
the computation starts at the best-fit parameter.
Then the profile likelihood computation will continue for the parameters to the
left of the best-fit.
After this is done, the computation returns to the best-fit and continue for
the parameters to the right. This process is done for each parameter.
