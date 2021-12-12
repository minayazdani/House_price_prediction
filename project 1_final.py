
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn import linear_model
from sklearn.preprocessing import scale  
from sklearn.feature_selection import SelectFromModel


df = pd.read_csv('D:/Dr.Farsad/Project/train.csv')
df = df.drop('Unnamed: 0', axis=1)
df['LotArea'] = (df['LotArea']/10.76)
df['LotArea'] = df['LotArea'].agg(int)

x = df.drop('SalePrice', axis=1)
x = pd.get_dummies(x)
y = df['SalePrice']

df = pd.DataFrame(scale(df))
df = pd.get_dummies(df) 
display(df1) 



            #-------------------------------------------------------------#
                       # ...........  Ridge  ...................#
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

param_grid = {'alpha': 10**np.linspace(10,-2,100)*0.5}
rid = GridSearchCV(linear_model.Ridge(), param_grid, scoring='r2')
rid.fit(X_train, np.sqrt(y_train))
print(rid.best_params_)
rid.score(X_test, np.sqrt(y_test))


             #--------------------------------------------------------------#
                        # ...........  Lasso  ...................#

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

param_grid = {'alpha': 10**np.linspace(10,-2,100)*0.5}
las = GridSearchCV(linear_model.Lasso(), param_grid, scoring='r2')
las.fit(X_train, np.sqrt(y_train))
print(las.best_params_)
las.score(X_test, np.sqrt(y_test))


lass = linear_model.Lasso(alpha=0.14240179342179024)
lass.fit(X_train, np.sqrt(y_train))
lass.score(X_test,np.sqrt( y_test))

#Selecting features using Lasso regularisation using SelectFromModel
sel_ = SelectFromModel(linear_model.Lasso(alpha=0.14240179342179024))
sel_.fit(X_train, np.sqrt(y_train))

#Visualising features that were kept by the lasso regularisation
sel_.get_support()

#Make a list of with the selected features
selected_feat = X_train.columns[(sel_.get_support())]
print('total features: {}'.format((X_train.shape[1])))
print('selected features: {}'.format(len(selected_feat)))
print('features with coefficients shrank to zero: {}'.format(np.sum(sel_.estimator_.coef_ == 0)))

#Number of features which coefficient was shrank to zero
np.sum(sel_.estimator_.coef_ == 0)

# Identifying the removed features
removed_feats = X_train.columns[(sel_.estimator_.coef_ == 0).ravel().tolist()]
removed_feats

# Identifying the selected features
selected_feat = X_train.columns[(sel_.estimator_.coef_ != 0).ravel().tolist()]
len(selected_feat)

#Removing the features from training an test set
X_train_selected = sel_.transform(X_train.fillna(0))
X_test_selected = sel_.transform(X_test.fillna(0))
X_train_selected.shape, X_test_selected.shape

X_train_selected = pd.DataFrame(X_train_selected)
X_train_selected.columns = selected_feat
X_test_selected = pd.DataFrame(X_test_selected).columns 
X_test_selected.columns = selected_feat
X_test_selected.columns

dfnew = pd.concat([X_train_selected,X_test_selected], axis=0)

                    #------------------------------------------------------#
                         # ...........  ElasticNet  ...................#
param_grid = {'alpha': 10**np.linspace(10,-2,100)*0.5}
eln = GridSearchCV(linear_model.ElasticNet(), param_grid, scoring='r2')
eln.fit(X_train, np.sqrt(y_train))
print(eln.best_params_)
eln.score(X_test,np.sqrt( y_test))

                     #------------------------------------------------------#
                       # ...........  LinearRegression  ...................#

model = LinearRegression()
model.fit(X_train, y_train)
model.score(X_test, y_test)
pre = model.predict(X_test)

                    #-------------------------------------------------------#

p = pd.read_csv('E:/Dr.Farsad/Project/test.csv')
p = p.drop(['Unnamed: 0'],axis=1)
     
pdummy = pd.get_dummies(p)

len(pdummy.columns)

# Get missing columns in the training test
missing_cols = set(dfdummy.columns) - set(pdummy.columns)
# Add a missing column in test set with default value equal to 0
for c in missing_cols:
    pdummy[c] = 0
# Ensure the order of column in the test set is in the same order than in train set
pdummy = pdummy[dfdummy.columns]

pre = rid.predict(pdummy)


           #-------------------------------- Random Forest Regressor ----------------------------#

#fiting Random Forest Regressor
regr = RandomForestRegressor(max_depth=70, n_estimators=15, max_features=50)
regr.fit(X_train, scale(y_train))
regr.score(X_test,scale(y_test))

# Set the hyperparameters by cross-validation
param_grid = {'n_estimators': [10,15,18,19,20,21,25, 30]}
rfg = GridSearchCV(RandomForestRegressor(), param_grid, scoring='r2')
rfg.fit(X_train, y_train)
print(rfg.best_params_)
rfg.score(X_test, y_test)


x, y = make_regression(n_features=6, n_informative=2, random_state=0, shuffle=False)
print(regr.predict([[5, 3, 785, 3, 5, 2003]]))

            # -------------------------------- Support Vector Regressor ----------------------------#

svr_lin = SVR(kernel='linear', C=10, gamma='auto')
svr_rbf = SVR(kernel='rbf', C=100, gamma=0.01, epsilon=0.1)
svr_poly = SVR(kernel='poly', C=10, gamma='auto', degree=3, epsilon=0.1, coef0=1)

svr_lin.fit(X_train, y_train)
svr_rbf.fit(X_train, y_train)
svr_poly.fit(X_train, y_train)

svr_lin.score(X_test,y_test)
svr_rbf.score(X_test,y_test)
svr_poly.score(X_test,y_test)

svr_lin.predict(X_test)
svr_rbf.predict(X_test)
svr_poly.predict(X_test)


# Set the parameters by cross-validation
param_grid = [
    {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
    {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
    {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['poly']}
   ]

param_grid = {'C': [1, 10, 100, 1000], 'kernel': ['linear']}

clf = GridSearchCV(SVR(), param_grid, scoring='r2')
clf.fit(X_train, y_train)
print("Best parameters set found on development set:")
print(clf.best_params_)
print("Grid scores on development set:")
svr_lin = SVR(kernel='linear', C=10, gamma='auto')
svr_lin.score(X_test,y_test)









