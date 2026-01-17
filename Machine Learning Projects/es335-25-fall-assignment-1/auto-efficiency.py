import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tree.base import DecisionTree
from metrics import *
#imports for the comparison
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.tree import plot_tree



np.random.seed(42)

# Reading the data
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
data = pd.read_csv(url, delim_whitespace=True, header=None,
                 names=["mpg", "cylinders", "displacement", "horsepower", "weight",
                        "acceleration", "model year", "origin", "car name"])

# Clean the above data by removing redundant columns and rows with junk values
# yes, a few columns that we will see onwards create a problem with improper values in the dataset

#viewing the dataframe
#data
print(data.shape)
print(data.isnull().sum()) # to see if any columns are not filled
print(data.dtypes) # to see if any of the data types are not supported => float64s and int64s => handled well 

#a point of suspicion was Horsepower, whose dtype was given as object, instead of a float like usual.
#used :
# data['horsepower'].unique()
# isnt showing when printing
#cleaning the horsepower column
data=data[data['horsepower']!='?'].reset_index(drop=True)
data['horsepower']=data['horsepower'].astype(float)


print(data.duplicated().sum()) #basic data pre-processing, check if any data is duplicated, if yes just remove it in the future. We didnt get any


#So, while we were doing this we tried fitting and predicting the resulting tree
#Importance of which metric to be used for what task is very important. For ex: dont use accuracy for a regression task

#data splitting => used scikit learn library
X_data=data.iloc[:,1:8].reset_index(drop=True)
y_data=data["mpg"]

#fitting the tree to the data
for criteria in ["mse"]:
    tree = DecisionTree(criterion=criteria, max_depth=5)  #only msw
    tree.fit(X_data, y_data)
    y_hat = tree.predict(X_data)
    tree.plot()
    print("Criteria :", criteria)
    print("RMSE: ", rmse(y_hat, y_data))
    print("MAE: ", mae(y_hat, y_data))
    # print("Accuracy", accuracy(y_hat,y_data))

#Results from our decision tree:
# Criteria : mse
# RMSE:  4.668742866549878
# MAE:  3.4943649335606763


#Now, fitting with the decision tree from scikit


tree=DecisionTreeRegressor(max_depth=5,random_state=42)

#fitting
tree.fit(X_data, y_data)

#preds
y_hat = tree.predict(X_data)

#metrics
rmse_val = np.sqrt(mean_squared_error(y_data, y_hat))
mae_val = mean_absolute_error(y_data, y_hat)

print("RMSE:", rmse_val)
print("MAE:", mae_val)

#visualize just to get an idea of the tree
plt.figure(figsize=(20,10))
plot_tree(tree, feature_names=X_data.columns, filled=True, rounded=True)
plt.show()

#Results of scikit's decision treee
# RMSE: 2.178138849149237
# MAE: 1.5952216438662674






# Compare the performance of your model with the decision tree module from scikit learn

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

tree=DecisionTreeRegressor(max_depth=5,random_state=42)

#fitting
tree.fit(X_data, y_data)

#preds
y_hat = tree.predict(X_data)

#metrics
rmse_val = np.sqrt(mean_squared_error(y_data, y_hat))
mae_val = mean_absolute_error(y_data, y_hat)

print("RMSE:", rmse_val)
print("MAE:", mae_val)

#visualize just to get an idea of the tree
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))
plot_tree(tree, feature_names=X_data.columns, filled=True, rounded=True)
plt.show()


#results
# RMSE: 2.178138849149237
# MAE: 1.5952216438662674
