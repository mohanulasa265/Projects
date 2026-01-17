Observations:

Dataset 1 (y = 3*x + 4)

Full Batch Gradient Descent converged in 128.00 steps and 128.00 epochs with lr = 0.1

Stochastic Gradient Descent converged in 13344.00 steps and 294.40 epochs with lr = 0.01

FBGD with momentum converged in 75.00 steps and 75.00 epochs with lr = 0.1, beta = 0.8

SGD with momentum converged in 7880.00 steps and 197.00 epochs with lr = 0.01 beta = 0.8


Dataset 2 (y = 100*x + 1)

Full Batch Gradient Descent converged in 3958.00 steps and 3958.00 epochs with lr = 0.001 beta = 0.7

Stochastic Gradient Descent converged in 36324.00 steps and 908.10 epochs with lr = 0.0001 beta = 0.7


FBGD with momentum converged in 3942.00 steps and 3942.00 epochs with lr = 0.001

SGD with momentum converged in 35584.00 steps and 889.60 epochs with lr = 0.0001


1) For both datasets, momentum significantly accelerated convergence compared to the vanilla descent
2) Learning rate is taken small whenever gradients are large and vice versa
3) There is scope of potential reduction of convergence steps further for Dataset 2, but it led to undesired oscillation in the loss vs. epochs plot, indicating instability in training.



