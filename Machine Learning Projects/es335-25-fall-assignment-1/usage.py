"""
The current code given is for the Assignment 1.
You will be expected to use this to make trees for:
> discrete input, discrete output
> real input, real output
> real input, discrete output
> discrete input, real output
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tree.base import DecisionTree
from metrics import *

np.random.seed(42)
# Test case 1
# Real Input and Real Output

N = 30
P = 5
X = pd.DataFrame(np.random.randn(N, P))
y = pd.Series(np.random.randn(N))


for criteria in ["information_gain", "gini_index"]:
    tree = DecisionTree(criterion=criteria)  # Split based on Inf. Gain
    tree.fit(X, y)
    y_hat = tree.predict(X)
    tree.plot()
    print("Criteria :", criteria)
    print("RMSE: ", rmse(y_hat, y))
    print("MAE: ", mae(y_hat, y))

# Test case 2
# Real Input and Discrete Output

N = 30
P = 5
X = pd.DataFrame(np.random.randn(N, P))
y = pd.Series(np.random.randint(P, size=N), dtype="category")

for criteria in ["information_gain", "gini_index"]:
    tree = DecisionTree(criterion=criteria)  # Split based on Inf. Gain
    tree.fit(X, y)
    y_hat = tree.predict(X)
    tree.plot()
    print("Criteria :", criteria)
    print("Accuracy: ", accuracy(y_hat, y))
    for cls in y.unique():
        print("Precision: ", precision(y_hat, y, cls))
        print("Recall: ", recall(y_hat, y, cls))


# Test case 3
# Discrete Input and Discrete Output

N = 30
P = 5
X = pd.DataFrame({i: pd.Series(np.random.randint(P, size=N), dtype="category") for i in range(5)})
y = pd.Series(np.random.randint(P, size=N), dtype="category")

for criteria in ["information_gain", "gini_index"]:
    tree = DecisionTree(criterion=criteria)  # Split based on Inf. Gain
    tree.fit(X, y)
    y_hat = tree.predict(X)
    tree.plot()
    print("Criteria :", criteria)
    print("Accuracy: ", accuracy(y_hat, y))
    for cls in y.unique():
        print("Precision: ", precision(y_hat, y, cls))
        print("Recall: ", recall(y_hat, y, cls))

# Test case 4
# Discrete Input and Real Output

N = 30
P = 5
X = pd.DataFrame({i: pd.Series(np.random.randint(P, size=N), dtype="category") for i in range(5)})
y = pd.Series(np.random.randn(N))

for criteria in ["information_gain", "gini_index"]:
    tree = DecisionTree(criterion=criteria)  # Split based on Inf. Gain
    tree.fit(X, y)
    y_hat = tree.predict(X)
    tree.plot()
    print("Criteria :", criteria)
    print("RMSE: ", rmse(y_hat, y))
    print("MAE: ", mae(y_hat, y))



#RESULTS

# ?(0 <= 0.7601447258863604)
#   Y:      ?(0 <= -0.06129716924473577)
#        Y:           ?(0 <= -1.3181071960107182)
#             Y:                ?(0 <= -1.5070891895991256)
#                  Y:                     ?(0 <= -1.7347173231825872)
#                       Y: -0.0771017094141042
#                       N: 0.01300189187790702
#                  N:                     ?(0 <= -1.4394428450912664)
#                       Y: -0.7537361643574896
#                       N: -0.8895144296255233
#             N:                ?(0 <= -0.4712959653288761)
#                  Y:                     ?(0 <= -0.6607754103120528)
#                       Y: 0.5651932647728086
#                       N: 1.2883541924917778
#                  N:                     ?(0 <= -0.3487773248808214)
#                       Y: -0.6800247215784908
#                       N: 0.5842541847457329
#        N:           ?(0 <= 0.6175903665033216)
#             Y:                ?(0 <= 0.3427397874516045)
#                  Y:                     ?(0 <= 0.31281565586420373)
#                       Y: -0.22081109811263763
#                       N: -0.9746816702273214
#                  N:                     ?(0 <= 0.38272323116147616)
#                       Y: 0.9633761292443218
#                       N: -0.28265871730978087
#             N: -1.1913034972026486
#   N:      ?(0 <= 0.7864274094101786)
#        Y: 2.720169166589619
#        N:           ?(0 <= 1.5077915869695468)
#             Y:                ?(0 <= 1.1437600738435107)
#                  Y:                     ?(0 <= 0.8765913117457111)
#                       Y: 0.34473586313325866
#                       N: 0.787084603742452
#                  N:                     ?(0 <= 1.4109443987461885)
#                       Y: -0.8206823183517105
#                       N: 0.29307247329868125
#             N:                ?(0 <= 1.870195015413759)
#                  Y: 1.4535340771573169
#                  N: 0.8271832490360238
# Criteria : information_gain
# RMSE:  0.32172798028689326
# MAE:  0.1785456754875403


# ?(0 <= 0.7601447258863604)
#   Y:      ?(0 <= -0.06129716924473577)
#        Y:           ?(0 <= -1.3181071960107182)
#             Y:                ?(0 <= -1.5070891895991256)
#                  Y:                     ?(0 <= -1.7347173231825872)
#                       Y: -0.0771017094141042
#                       N: 0.01300189187790702
#                  N:                     ?(0 <= -1.4394428450912664)
#                       Y: -0.7537361643574896
#                       N: -0.8895144296255233
#             N:                ?(0 <= -0.4712959653288761)
#                  Y:                     ?(0 <= -0.6607754103120528)
#                       Y: 0.5651932647728086
#                       N: 1.2883541924917778
#                  N:                     ?(0 <= -0.3487773248808214)
#                       Y: -0.6800247215784908
#                       N: 0.5842541847457329
#        N:           ?(0 <= 0.6175903665033216)
#             Y:                ?(0 <= 0.3427397874516045)
#                  Y:                     ?(0 <= 0.31281565586420373)
#                       Y: -0.22081109811263763
#                       N: -0.9746816702273214
#                  N:                     ?(0 <= 0.38272323116147616)
#                       Y: 0.9633761292443218
#                       N: -0.28265871730978087
#             N: -1.1913034972026486
#   N:      ?(0 <= 0.7864274094101786)
#        Y: 2.720169166589619
#        N:           ?(0 <= 1.5077915869695468)
#             Y:                ?(0 <= 1.1437600738435107)
#                  Y:                     ?(0 <= 0.8765913117457111)
#                       Y: 0.34473586313325866
#                       N: 0.787084603742452
#                  N:                     ?(0 <= 1.4109443987461885)
#                       Y: -0.8206823183517105
#                       N: 0.29307247329868125
#             N:                ?(0 <= 1.870195015413759)
#                  Y: 1.4535340771573169
#                  N: 0.8271832490360238
# Criteria : gini_index
# RMSE:  0.32172798028689326
# MAE:  0.1785456754875403



# ?(0 <= 0.5164969924782189)
#   Y:      ?(0 <= -0.27609121953408433)
#        Y:           ?(0 <= -0.9323777557466029)
#             Y:                ?(0 <= -1.2543335681499475)
#                  Y: 1
#                  N: 4
#             N:                ?(0 <= -0.7614436850749187)
#                  Y:                     ?(0 <= -0.8779627412500777)
#                       Y: 0
#                       N: 0
#                  N:                     ?(0 <= -0.5885718340634528)
#                       Y: 1
#                       N: 1
#        N:           ?(0 <= 0.23755737182853265)
#             Y:                ?(0 <= 0.10525665512198312)
#                  Y:                     ?(0 <= -0.21290172679224775)
#                       Y: 4
#                       N: 2
#                  N:                     ?(0 <= 0.11542236428001501)
#                       Y: 0
#                       N: 4
#             N: 1
#   N:      ?(0 <= 0.6739597582050516)
#        Y:           ?(0 <= 0.5982789292290867)
#             Y: 2
#             N:                ?(0 <= 0.6297931850415087)
#                  Y: 4
#                  N: 3
#        N:           ?(0 <= 0.9239599087303167)
#             Y: 4
#             N:                ?(0 <= 1.2651119430167408)
#                  Y: 2
#                  N:                     ?(0 <= 1.8779659278698122)
#                       Y: 4
#                       N: 2
# Criteria : information_gain
# Accuracy:  0.9
# Precision:  1.0
# Recall:  0.9
# Precision:  0.9
# Recall:  0.9
# Precision:  0.8333333333333334
# Recall:  1.0
# Precision:  1.0
# Recall:  0.5
# Precision:  0.75
# Recall:  1.0


# ?(0 <= 0.5164969924782189)
#   Y:      ?(0 <= 0.23755737182853265)
#        Y:           ?(0 <= -0.27609121953408433)
#             Y:                ?(0 <= -0.9323777557466029)
#                  Y:                     ?(0 <= -1.2543335681499475)
#                       Y: 1
#                       N: 4
#                  N:                     ?(0 <= -0.7614436850749187)
#                       Y: 0
#                       N: 1
#             N:                ?(0 <= 0.10525665512198312)
#                  Y:                     ?(0 <= -0.21290172679224775)
#                       Y: 4
#                       N: 2
#                  N:                     ?(0 <= 0.11542236428001501)
#                       Y: 0
#                       N: 4
#        N: 1
#   N:      ?(0 <= 0.5982789292290867)
#        Y: 2
#        N:           ?(0 <= 0.9239599087303167)
#             Y:                ?(0 <= 0.6739597582050516)
#                  Y:                     ?(0 <= 0.6297931850415087)
#                       Y: 4
#                       N: 3
#                  N: 4
#             N:                ?(0 <= 1.2651119430167408)
#                  Y: 2
#                  N:                     ?(0 <= 1.8779659278698122)
#                       Y: 4
#                       N: 2
# Criteria : gini_index
# Accuracy:  0.9
# Precision:  1.0
# Recall:  0.9
# Precision:  0.9
# Recall:  0.9
# Precision:  0.8333333333333334
# Recall:  1.0
# Precision:  1.0
# Recall:  0.5
# Precision:  0.75
# Recall:  1.0



# ?(0)
#   0:      ?(0)
#        0:           ?(0)
#             0:                ?(0)
#                  0:                     ?(0)
#                       0: 3
#   3:      ?(0)
#        3:           ?(0)
#             3:                ?(0)
#                  3:                     ?(0)
#                       3: 0
#   4:      ?(0)
#        4:           ?(0)
#             4:                ?(0)
#                  4:                     ?(0)
#                       4: 1
#   2:      ?(0)
#        2:           ?(0)
#             2:                ?(0)
#                  2:                     ?(0)
#                       2: 1
#   1:      ?(0)
#        1:           ?(0)
#             1:                ?(0)
#                  1:                     ?(0)
#                       1: 2
# Criteria : information_gain
# Accuracy:  0.4666666666666667
# Precision:  0.3333333333333333
# Recall:  0.42857142857142855
# Precision:  0.0
# Recall:  0.0
# Precision:  0.5454545454545454
# Recall:  0.6666666666666666
# Precision:  0.75
# Recall:  0.6
# Precision:  0.3333333333333333
# Recall:  0.4




# ?(0)
#   0:      ?(0)
#        0:           ?(0)
#             0:                ?(0)
#                  0:                     ?(0)
#                       0: 3
#   3:      ?(0)
#        3:           ?(0)
#             3:                ?(0)
#                  3:                     ?(0)
#                       3: 0
#   4:      ?(0)
#        4:           ?(0)
#             4:                ?(0)
#                  4:                     ?(0)
#                       4: 1
#   2:      ?(0)
#        2:           ?(0)
#             2:                ?(0)
#                  2:                     ?(0)
#                       2: 1
#   1:      ?(0)
#        1:           ?(0)
#             1:                ?(0)
#                  1:                     ?(0)
#                       1: 2
# Criteria : gini_index
# Accuracy:  0.4666666666666667
# Precision:  0.3333333333333333
# Recall:  0.42857142857142855
# Precision:  0.0
# Recall:  0.0
# Precision:  0.5454545454545454
# Recall:  0.6666666666666666
# Precision:  0.75
# Recall:  0.6
# Precision:  0.3333333333333333
# Recall:  0.4





# ?(0)
#   3:      ?(0)
#        3:           ?(0)
#             3:                ?(0)
#                  3:                     ?(0)
#                       3: 0.13228249706842737
#   4:      ?(0)
#        4:           ?(0)
#             4:                ?(0)
#                  4:                     ?(0)
#                       4: -0.10264616560882701
#   1:      ?(0)
#        1:           ?(0)
#             1:                ?(0)
#                  1:                     ?(0)
#                       1: -0.05415949861222805
#   2:      ?(0)
#        2:           ?(0)
#             2:                ?(0)
#                  2:                     ?(0)
#                       2: -0.09531760063802394
#   0:      ?(0)
#        0:           ?(0)
#             0:                ?(0)
#                  0:                     ?(0)
#                       0: 0.7694639675155581
# Criteria : information_gain
# RMSE:  0.9379116719412398
# MAE:  0.7351640245903074




# ?(0)
#   3:      ?(0)
#        3:           ?(0)
#             3:                ?(0)
#                  3:                     ?(0)
#                       3: 0.13228249706842737
#   4:      ?(0)
#        4:           ?(0)
#             4:                ?(0)
#                  4:                     ?(0)
#                       4: -0.10264616560882701
#   1:      ?(0)
#        1:           ?(0)
#             1:                ?(0)
#                  1:                     ?(0)
#                       1: -0.05415949861222805
#   2:      ?(0)
#        2:           ?(0)
#             2:                ?(0)
#                  2:                     ?(0)
#                       2: -0.09531760063802394
#   0:      ?(0)
#        0:           ?(0)
#             0:                ?(0)
#                  0:                     ?(0)
#                       0: 0.7694639675155581
# Criteria : gini_index
# RMSE:  0.9379116719412398
# MAE:  0.7351640245903074
