import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tree.base import DecisionTree
from metrics import *
from sklearn.datasets import make_classification

np.random.seed(42)

# Code given in the question
X, y = make_classification(
    n_features=2, n_redundant=0, n_informative=2, random_state=1, n_clusters_per_class=2, class_sep=0.5)

# For plotting
plt.scatter(X[:, 0], X[:, 1], c=y)



# Write the code for Q2 a) and b) below. Show your results.
#Q2(a)

#convert to dataFrame
X=pd.DataFrame(X,columns=["feat1", "feat2"])
y=pd.Series(y)

#train test splits
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#fitting the tree for an exampl
dec_tree=DecisionTree(criterion='entropy',max_depth=3)
dec_tree.fit(X_train,y_train)

#plotting the tree
dec_tree.plot()

#predicting for both info gain methods
for criteria in ["entropy", "gini_index"]:
    tree=DecisionTree(criterion=criteria)  #
    tree.fit(X_train,y_train)
    y_hat=tree.predict(X_test)
    tree.plot()
    print("Criteria :",criteria)
    print("Accuracy:",accuracy(y_hat,y_test))
    for cls in y_test.unique():
        print("Class:",cls)
        print("Precision: ",precision(y_hat, y_test, cls))
        print("Recall: ",recall(y_hat, y_test, cls))   #classifiction task cant use RMSE, or MAE

#results
# Criteria : entropy
# Accuracy: 0.8333333333333334
# Class: 1
# Precision:  0.8571428571428571
# Recall:  0.8
# Class: 0
# Precision:  0.8125
# Recall:  0.8666666666666667

# Criteria : gini_index
# Accuracy: 0.9
# Class: 1
# Precision:  0.875
# Recall:  0.9333333333333333
# Class: 0
# Precision:  0.9285714285714286
# Recall:  0.8666666666666667


#2(b)

#the split function
import numpy as np

#splitting into 'k' folds +> k-1 folds for train and one for test
def kfold_split(X, y, k=5, seed=42):
    np.random.seed(seed)
    indices=np.arange(len(X))
    np.random.shuffle(indices)
    fold_sizes=[len(X) // k] * k
    for i in range(len(X) % k):
        fold_sizes[i]+=1

    folds=[]
    start=0
    for size in fold_sizes:
        end=start+size
        folds.append(indices[start:end])
        start=end
    return folds

# from metrics import accuracy, precision, recall

def cross_val_nested(X, y, max_depth_candidates=range(1, 11), k=5, criterion="information_gain"):
    folds=kfold_split(X, y, k)
    outer_acc,outer_prec,outer_rec,best_depths = [], [], [], []

    for i in range(k):
        #for each fold, setting up test and train => [train,train,train,train,train,test]
        test_indices=folds[i]
        train_indices=np.concatenate([folds[j] for j in range(k) if j != i])

        X_train,y_train=X.iloc[train_indices],y.iloc[train_indices]
        X_test,y_test=X.iloc[test_indices],y.iloc[test_indices]

        #Inner fold creation to not overfit to this sequence of folds in train => [train1,train2,train3,val] => shufffle these folds to get a more general training alg
        inner_folds=kfold_split(X_train, y_train, k)
        depth_scores={}

        for d in max_depth_candidates:
            inner_acc_scores=[]
            for j in range(k):
                val_idx = inner_folds[j]
                inner_train_idx = np.concatenate([inner_folds[m] for m in range(k) if m != j])

                X_inner_train, y_inner_train = X_train.iloc[inner_train_idx], y_train.iloc[inner_train_idx]
                X_val, y_val = X_train.iloc[val_idx], y_train.iloc[val_idx]

                model = DecisionTree(criterion=criterion, max_depth=d)
                model.fit(X_inner_train, y_inner_train)
                y_pred = model.predict(X_val)

                inner_acc_scores.append(accuracy(y_val,y_pred))  #taking the metrucs to find the best one

            depth_scores[d] = np.mean(inner_acc_scores) #mean to find the score for a particular depth

        #take best depth => max accuraacy score
        best_depth=max(depth_scores,key=depth_scores.get)
        best_depths.append(best_depth)

        #train with best depth on outer training data
        model=DecisionTree(criterion=criterion,max_depth=best_depth)
        model.fit(X_train,y_train)
        y_pred=model.predict(X_test)

        #collect metrics
        outer_acc.append(accuracy(y_test, y_pred))
        for i in y_test.unique():
          outer_prec.append(precision(y_test, y_pred,i))
          outer_rec.append(recall(y_test, y_pred,i))

    return {
        "mean_accuracy": np.mean(outer_acc),
        "mean_precision": np.mean(outer_prec, axis=0),
        "mean_recall": np.mean(outer_rec, axis=0),
        "best_depths": best_depths
    }

#testing it out on the dataset generated at the start
cross_val_nested(X,y)

#results
# {'mean_accuracy': np.float64(0.9),
#  'mean_precision': np.float64(0.9016161616161616),
#  'mean_recall': np.float64(0.904318181818182),
#  'best_depths': [1, 2, 1, 1, 1]}

#testing out a depth of 1
et_d_tree=DecisionTree(max_depth=1,criterion="information_gain")
et_d_tree.fit(X_train,y_train)
yh_test=et_d_tree.predict(X_test)
accuracy(y_test,yh_test)

#results
# np.float64(0.9333333333333333)
