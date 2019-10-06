# path of file to dataset
PATH="Desktop/sem_3/dmml/assignment2/connect-4.data"
f=open(PATH,'r')

'''
X : feature, y : target value
we are using feature selection such that our features will be
list of columns in our game that is a, b, c, d, e, f, g
'''
X=[]
y=[]
for i, line in enumerate(f):
    row=line.split(',')
    x=[]
    for j in range(7):
        s = ""
        for k in range(6):
            s = s + row[6*j+k]
        x.append(s)
    X.append(x)
    y.append(row[42])  

f.close()

'''
preprocessing the dataset so that target will be nominal
and labeling the features too.
'''
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

X_ = []
for x_ in range(len(X)):
    for x in range(7):
        X_.append(X[x_][x])

le.fit(X_)

X_=X
X=[]
for x_ in X_:
    X.append(le.transform(x_))

y_=y
y=[]

for out in y_:
    if out=='win\n':
        y.append(1)
    elif out=='loss\n':
        y.append(-1)
    else:
        y.append(0)

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier 
from sklearn.naive_bayes import GaussianNB 

######################## Decision tree ########################
dtree = DecisionTreeClassifier( max_depth = 2)
scores = cross_val_score(dtree, X, y, cv=10)
print('\n\n----------------- Decision tree ----------------\n')
print('crosss validation scores : ')
print(scores )     
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))  

######################## Naive Bayes ##########################
gnb = GaussianNB()
scores = cross_val_score(gnb, X, y, cv=10)
print('\n\n-----------------  Naive Bayes  ----------------\n')
print('crosss validation scores : ')
print(scores )     
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))  

'''
for SVM making one hot encoding of features
NOTE : It is taking quite a while to run because of too many iterations
'''
f=open("Desktop/sem_3/dmml/assignment2/connect-4.data",'r')

X=[]
for i, line in enumerate(f):
    row=line.split(',')
    x=[]
    o_ = [1, 1, 1]
    b_ = [1, 1, 0]
    x_ = [1, 0, 0]
    for feature in row:
        if feature=='o':
            x += o_
        elif feature=='b':
            x += b_
        elif feature=='x':
            x += x_
        else:
            pass
    X.append(x)
f.close()

############################ SVM #############################
from sklearn.svm import LinearSVC
svm = LinearSVC(multi_class='crammer_singer', C=0.5, max_iter=100000)

scores = cross_val_score(svm, X, y, cv=10)
print('\n\n-----------------      SVM      ----------------\n')
print('crosss validation scores : ')
print(scores )     
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)) 