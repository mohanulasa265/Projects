"""
The current code given is for the Assignment 1.
You will be expected to use this to make trees for:
> discrete input, discrete output
> real input, real output
> real input, discrete output
> discrete input, real output
"""
from dataclasses import dataclass
from typing import Literal

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import *

np.random.seed(42)


@dataclass

class Node:
    def __init__(self):
        self.attr = None
        self.pred = None
        self.children = {}
        self.rootnode = None
        self.leftnode = None
        self.rightnode = None
        self.split = None

class DecisionTree:
    criterion: Literal["information_gain", "gini_index"]  # criterion won't be used for regression
    max_depth: int  # The maximum depth the tree can grow to

    def __init__(self, criterion, max_depth=5):
        self.criterion = criterion
        self.max_depth = max_depth
        self.input = None # for knowing the nature of input(real or discrete)
        self.output = None # for knowing the nature of input(real or discrete)

    def grow_tree(self, X: pd.DataFrame, y: pd.Series, depth: int):
        node = Node()
        if len(y.unique()) == 1 or depth>= self.max_depth: # condition where max depth reached or else all values of y are same
            if self.output == False:
                node.pred = y.mode()[0]  # when output is discrete
            else:
                node.pred = y.mean()  # when output is real
            return node

        res = opt_split_attribute(X, y, self.criterion, X.columns)

        if isinstance(res, tuple):   # real feature
              best_feat, best_thresh = res
        else:                        # discrete feature
             best_feat, best_thresh = res, None

        node.attr = best_feat
        node.split = best_thresh


        if self.input[best_feat] == False: # discrete input
            for i in X[best_feat].unique():
                X_subset, y_subset = split_data(X,y,best_feat,i) # Taking the subset of the dataframe where attribute = That particular feature

                if len(X_subset)  == 0:
                    child = Node()
                    if self.output == False:
                        child.pred = y.mode()[0] # if values of attributes are empty then return the most common value of target attribute(in case of discrete output)
                    else:
                        child.pred = y.mean() # if values of attributes are empty then return the mean value of target attribute(in case of real output)
                    node.children[i] = child

                else:
                    node.children[i] = self.grow_tree(X_subset,y_subset,depth+1) # new children becomes the sub root node. so called the funtion recursively
            return node

        else:  # real input
            avg_split = 0
            gain = 9999999999999
            final_split = 0
            X_sort = X.sort_values(by=best_feat)
            y_sort = y.loc[X_sort.index]
            x_vals = X_sort[best_feat].values
            y_vals = y_sort.values
            for i in range(len(X_sort)-1):
                avg_split = (x_vals[i] + x_vals[i+1])/2  # splits should be done between every consecutive values
                y_left = y_vals[x_vals<=avg_split]
                y_right = y_vals[x_vals>avg_split]


                if self.output:  # real output
                    weighted_loss = (len(y_left)/len(y_vals))*mse_feat(pd.Series(y_left)) + (len(y_right)/len(y_vals))*mse_feat(pd.Series(y_right))
                else: # discrete output
                    if self.criterion == 'gini_index':
                        weighted_loss = (len(y_left)/len(y_vals))*gini_index(pd.Series(y_left)) + (len(y_right)/len(y_vals))*gini_index(pd.Series(y_right))

                    else:
                        weighted_loss = (len(y_left)/len(y_vals))*entropy(pd.Series(y_left)) + (len(y_right)/len(y_vals))*entropy(pd.Series(y_right))

                if weighted_loss < gain:
                    gain = weighted_loss
                    final_split = avg_split

            node.split = final_split

            node.leftnode = self.grow_tree(X[X[best_feat] <= final_split],y[X[best_feat] <= final_split], depth+1)
            node.rightnode = self.grow_tree(X[X[best_feat] > final_split],y[X[best_feat] > final_split], depth+1)

            return node

    def fit(self, X: pd.DataFrame, y: pd.Series) -> None:
        """
        Function to train and construct the decision tree
        """

        # If you wish your code can have cases for different types of input and output data (discrete, real)
        # Use the functions from utils.py to find the optimal attribute to split upon and then construct the tree accordingly.
        # You may(according to your implemetation) need to call functions recursively to construct the tree.

        self.input = {}
        for i in X.columns:
            self.input[i] = check_ifreal(X[i])
        self.output = check_ifreal(y.squeeze()) #safety for y  passed as a dataframe

        self.rootnode = self.grow_tree(X,y,depth = 0)

    def predict(self, X: pd.DataFrame) -> pd.Series:
        """
        Funtion to run the decision tree on test inputs
        """
        y_hat = [] # hat represents prediction
        for _,row in X.iterrows():
            node = self.rootnode

            while node.pred is None: # traversing through the entire nodes until we hit the leaf
                if node.split is not None:  # regression
                    if row[node.attr] <= node.split:
                        node = node.leftnode
                    else:
                        node = node.rightnode
                else:   # classification
                    val = row[node.attr]
                    node = node.children.get(val,None)
                    if node is None:
                        break

            if node is None:
                y_hat.append(None)
            else:
                y_hat.append(node.pred)
        return pd.Series(y_hat,index=X.index)


    def plot(self) -> None:
        """
        Function to plot the tree

        Output Example:
        ?(X1 > 4)
            Y: ?(X2 > 7)
                Y: Class A
                N: Class B
            N: Class C
        Where Y => Yes and N => No
        """
        def print_tree(node,x= ""):
            if node.split is not None:
                print(x + f"?({node.attr} <= {node.split})")
                print(x + "  Y: ", end="")
                print_tree(node.leftnode, x + "     ")
                print(x + "  N: ", end="")
                print_tree(node.rightnode, x + "     ")

            elif node.pred is not None:
                print(str(node.pred))
                return

            else:
                print(x + f"?({node.attr})")
                for val, item in node.children.items():
                    print(x + f"  {val}: ",end="")
                    print_tree(item, x + "     ")


        print_tree(self.rootnode)
