This is the second DMML assignment submission by Rohit Singh(MCS201812) & Shrisha Rao(MCS201916)
OUTPUT is given below

Documentation:
We are using sicketLearn library in our code

Our code runs as follows:

In lines 10-23, we create lists X and y where X contains lists of 7 strings of length 6 each and y is the list containing the output corresponding to each play.
	For example, the first line of the given dataset is:
	b,b,b,b,b,b,b,b,b,b,b,b,x,o,b,b,b,b,x,o,x,o,x,o,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,win
	So, the first list in X will be [bbbbbb, bbbbbb, xobbbb, xoxoxo, bbbbbb, bbbbbb, bbbbbb] and the first element of y will be 'win'.

In lines 32-35, we create a list X_ consisting of each string occuring in each list in X.

In lines 39-53, we create new lists X and y where X now contains lists of the encoding of the strings and y now replaces each 'win', 'loss' and 'draw' in the 
	previous y by 1, -1 and 0 respectively.

In lines 59-73, we feed the lists X and y to create a decision tree of depth 2 (because this gave the best results for our case) and a naive bayes classifier and
	output the cross validation scores and the accuracy.

In lines 81-98, we create a different list X for SVM. X is a list of lists containing 0's and 1's such that the i'th list of X corresponds to the i'th line of the
	given dataset with each o by 1, 1, 1, each b by 1, 1, 0, and each x by 1, 0, 0.

In the remaining lines, we input this list X and the list y we defined before to create an SVM and output the cross validation scores and accuracy.


