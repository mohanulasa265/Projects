Observations:

1) The scaled version converged fast because when we scale the data (make x values smaller and similar in range),the gradients become smaller and more balanced,
2) So the learning rate we chose works well — the updates move smoothly toward the minimum.
3) In the unscaled version, the x values are very large (up to 1000),this makes the gradients extremely large,
4) So with the same learning rate, each step becomes too big.
5) The algorithm keeps jumping past the minimum instead of moving gradually,which causes oscillations and no convergence even after many iterations.