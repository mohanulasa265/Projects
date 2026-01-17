import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from tree.base import DecisionTree
from metrics import *

np.random.seed(42)
num_average_time = 100  # Number of times to run each experiment to calculate the average values


# Function to create fake data (take inspiration from usage.py)
#need to add for the four cases, take those as ip
def make_fake_data(N,M,input_type="discrete",output_type="discrete"):
    if input_type=="discrete":
        X=pd.DataFrame(np.random.randint(0,3,size=(N,M)),columns=[f"X{i}" for i in range(M)])
    else:  #real ip
        X=pd.DataFrame(np.random.randn(N,M),columns=[f"X{i}" for i in range(M)])
    if output_type=="discrete":
        y=pd.Series(np.random.randint(0,2,size=N))
    else:  #real op
        y=pd.Series(np.random.randn(N))
  
    return X,y


  
# Function to calculate average time (and std) taken by fit() and predict() for different N and P for 4 different cases of DTs
def measure_time(tree_clss,X,y):
  ##fit
  start=time.time()
  tree= tree_clss
  tree.fit(X,y)
  end=time.time()
  fit_time=(end-start)

  ## pred time
  start=time.time()
  tree.predict(X)
  end=time.time()
  pred_time=(end-start)

  return fit_time,pred_time


# Function to plot the results
def measure_and_plot(Ms,Ns, max_depth):
#give a list of Ms, Ns and Max_depth as its inputs
    
tree_cases=[("Discrete In,Discrete Out","discrete","discrete"),("Real In,Discrete Out","real","discrete"),("Discrete In,Real Out","discrete", "real"),("Real In,Real Out", "real", "real")]

results_all={}

#all cases at once
for case_name,in_type,out_type in tree_cases:
    print(f"Running: {case_name}") #need to see what is running without just waitiming aimlessly
    results_all[case_name]={"Nchange":[],"Mchange":[]} #a list of lists-> containing varying Ms and Ns for a particular tree

    fixed_m=5
    for N in Ns: #foreach n
        X,y=make_fake_data(N,fixed_m,in_type,out_type)
        tree=DecisionTree(criterion="information_gain", max_depth=max_depth)
        fit_time,predict_time=measure_fitting_time(tree, X, y)
        results_all[case_name]["Nchange"].append((N,fixed_m,fit_time,predict_time))

    fixed_n=500
    for M in Ms: #foreach m
        X,y=make_fake_data(fixed_n,M,in_type, out_type)
        tree=DecisionTree(criterion="information_gain", max_depth=max_depth)
        fit_time,predict_time=measure_fitting_time(tree,X,y)
        results_all[case_name]["Mchange"].append((fixed_n,M,fit_time,predict_time))


#plotting all the 8 plots=> (4 cases * 2 varies)
for case_name in results_all.keys():
    print(f"Plotting:{case_name}") #to check

    Ns=[r[0] for r in results_all[case_name]["Nchange"]]
    fit_times_N=[r[2] for r in results_all[case_name]["Nchange"]]
    predict_times_N=[r[3] for r in results_all[case_name]["Nchange"]]

    plt.figure(figsize=(8,5))
    plt.plot(Ns,fit_times_N,marker="o",label="Fit time")
    plt.plot(Ns,predict_times_N,marker="o",label="Predict time")
    plt.xlabel("Number of samples (N)")
    plt.ylabel("Time (s)")
    plt.title(f"{case_name} - Scaling with N (M fixed)")
    plt.legend()
    plt.grid(True)
    plt.show()

    Ms=[r[1] for r in results_all[case_name]["Mchange"]]
    fit_times_M=[r[2] for r in results_all[case_name]["Mchange"]]
    predict_times_M=[r[3] for r in results_all[case_name]["Mchange"]]

    plt.figure(figsize=(8,5))
    plt.plot(Ms,fit_times_M, marker="o",label="Fit time")
    plt.plot(Ms,predict_times_M,marker="o",label="Predict time")
    plt.xlabel("Number of features (M)")
    plt.ylabel("Time (s)")
    plt.title(f"{case_name} - Scaling with M (N fixed)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Other functions
# ...


# Run the functions, Learn the DTs and Show the results/plots
