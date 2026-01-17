Observations in this Task:
1) Higher-ranked matrix refactorization leads to much better reproduction of images, which can be seen in the Jupyter notebook "task_4_new.ipynb". It also increases the size of the data (matrix elements) required, and it scales linearly with r (r*(nRows + nColumns)).
2) While making the stock factorization, ALS was much slower than Gradient Descent. A reason that can explain this is due to solving the least squares problem for each of the r rows and r columns in W and H, for every iteration. The time complexity of ALS is much greater than finding gradients in Gradient descent, again can be seen in the jupyter notebook with the runtimes.
3) Using too many iterations >3000) for matrix refactorization gave very noisy images as results.
4) In the data compression task, we see that as we increase the rank for the factorization, we can see a decrease in RMSE and an increase in PSNR.
5) For all three subproblems, we could see lower RMSEs with an increase in rank.
6) In the end, we can safely say that, compressing pictures in the form of smaller matrices W and H, can keep the same image quality as the full-length matrix, meanwhile taking up much lesser space. (As low as ~80% decrease for a rank 10 factorization shown in the notebook)

