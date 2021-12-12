

import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.impute import SimpleImputer
from sklearn_pandas import CategoricalImputer
import miceforest as mf

147500
NaN = np.nan

df1 = pd.read_csv('E:/Dr.Farsad/Project/train.csv')


imp = mf.ampute_data(pd.get_dummies(df1),perc=0.25,random_state=1991)
kernel = mf.MultipleImputedKernel(
  data=imp,
  save_all_iterations=True,
  random_state=1991
)

# Our new dataset
df = df.append(pd.Series(), ignore_index=True)

df.loc[df.shape[0]-1,'LotArea'] = 9937
df.loc[df.shape[0]-1,'MSZoning'] = 'RL'
df.loc[df.shape[0]-1,'Neighborhood'] = 'Edwards'
df.loc[df.shape[0]-1,'HouseStyle'] = '1Story'
df.loc[df.shape[0]-1,'BedroomAbvGr'] = 3
df.loc[df.shape[0]-1,'YearBuilt'] = 56
df.loc[df.shape[0]-1,'SalePrice'] >= .....
impsale = []
for i in range(0,100):
    new_data = pd.get_dummies(df)# Make a multiple imputed dataset with our new data
    new_data_imputed = kernel.impute_new_data(new_data)# Return a completed dataset
    new_completed_data = new_data_imputed.complete_data(0)

    imp = pd.DataFrame(new_completed_data)
    imp.columns = pd.get_dummies(df).columns
    impsale.append(imp.SalePrice[1314])

np.mean(impsale)

imputer = KNNImputer(n_neighbors=10, weights="uniform")
imp = imputer.fit_transform(pd.get_dummies(df))

imp = pd.DataFrame(imp)
imp.columns = pd.get_dummies(df).columns
imp.SalePrice[1314]


imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
# transform the dataset
imp = imputer.fit_transform(pd.get_dummies(df))

imp = pd.DataFrame(imp)
imp.columns = pd.get_dummies(df).columns
imp.SalePrice[1314]




imputer = CategoricalImputer()
imp = imputer.fit_transform(pd.get_dummies(df))



#Ask for area
preferred_LotArea = int(input("type the minimum area (between 120 and 20004): "))

#Ask for the number of room
number_room = int(input("Input the minimum number of room (between 0 and 8): "))

#Ask for the age of house
age_house = int(input("Input the maximum age of house (between 11 and 149): "))

#Ask for budget
budget = int(input("Input your maximum budget: "))
    
#Ask for neighbourhood 
print("Input the preferred Neighborhood: please select from the list")
list_Neighborhood = {1:'CollgCr', 2:'Veenker', 3:'Crawfor', 4:'NoRidge', 5:'Mitchel', 6:'Somerst',
             7:'OldTown', 8:'BrkSide', 9:'NridgHt', 10:'Sawyer', 11:'NAmes', 12:'SawyerW', 13:'IDOTRR',
             14:'MeadowV', 15:'Gilbert', 16:'StoneBr', 17:'ClearCr', 18:'Edwards', 19:'NWAmes', 20:'NPkVill',
             21:'Timber', 22:'Blmngtn', 23:'BrDale', 24:'SWISU', 25:'Blueste'}
print(list_Neighborhood)
Neighborhood = input('select from the list_Neighborhood:')

   
#Ask for land use: if it is not important for you please type "all". :
#otherwise you can choose. please consider that if you have more than one option you have to type & between the preferred ones with out any space.
print("Input the type of preferred_MSZoning")
list_MSZoning  = {1:'RL', 2:'RM', 3:'FV', 4:'RH'} 
print(list_MSZoning)          
MSZoning  = input('select from the list_MSZoning:')


#Ask for the number of story: if it is not important for you please type "all". :
#otherwise you can choose. please consider that if you have more than one option you have to type & between the preferred ones with out any space.
print("Input the type of HouseStyle ['2Story', '1Story', '1.5Fin', '1.5Unf','SFoyer', 'SLvl', '2.5Unf','2.5Fin']")
list_story = {1:'2Story', 2:'1Story', 3:'1.5Fin', 4:'1.5Unf', 5:'SFoyer', 6:'SLvl', 7:'2.5Unf', 8:'2.5Fin'}         
story = input('select from the list_story:')





            #----------------------------------------------------------------#


l = []
ndf = []  
npp = []  
for i in range(0,76):
    if df[df.columns[i]].dtypes == 'O' and len(df[df.columns[i]].unique())!=len(p[p.columns[i]].unique()):
        l.append(df.columns[i])
        ndf.append(len(df[df.columns[i]].unique()))
        npp.append(len(p[p.columns[i]].unique()))

print(l)
print(ndf)
print(npp)
   
len(p['Utilities'].unique())
len(p['Condition2'].unique())
len(p['RoofMatl'].unique())
len(p['Exterior1st'].unique())
len(p['Exterior2nd'].unique())
len(p['Heating'].unique())
len(p['Electrical'].unique())
len(p['PoolQC'].unique())
len(p['MiscFeature'].unique())
