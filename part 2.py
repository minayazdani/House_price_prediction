
df = pd.read_csv("E:/Dr.Farsad/Project/train.csv")
df = df.drop('Unnamed: 0', axis=1)
df['LotArea'] = (df['LotArea']/10.76)
df['LotArea'] = df['LotArea'].agg(int)
df0=df


lass = linear_model.Lasso(alpha=0.14240179342179024)
lass.fit(X_train, np.sqrt(y_train))
lass.score(X_test,np.sqrt( y_test))


def prefer(preferred_LotArea, number_room, age_house, number_story,
           number_Neighborhood, number_MSZoning, budget):
        
    df1 = df0[df0['LotArea'] >= preferred_LotArea]

    df2 = df1[df1['BedroomAbvGr'] == number_room]

    df3 = df2[df2['YearBuilt'] <= age_house]
    
    df4 = df3[df3['HouseStyle'] == number_story]
    
    df5 = df4[df4['Neighborhood'] == number_Neighborhood]
    
    df6 = df5[df5['MSZoning'] == number_MSZoning]
    
    for i in range(0,len(df6['SalePrice'])):
        if budget-5000 <= df6['SalePrice'][i] <= budget+5000:
            options = df6[df6['SalePrice'] <= budget]
        else:
            df6 = df6.append(pd.Series(), ignore_index=True)
            df6.loc[df6.shape[0]-1,'LotArea'] = preferred_LotArea
            df6.loc[df6.shape[0]-1,'HouseStyle'] = number_story
            df6.loc[df6.shape[0]-1,'Neighborhood'] = number_Neighborhood
            df6.loc[df6.shape[0]-1,'MSZoning'] = number_MSZoning
            df6.loc[df6.shape[0]-1,'BedroomAbvGr'] = number_room
            df6.loc[df6.shape[0]-1,'YearBuilt'] = age_house
      
        
        prediction= las.predict(df6.iloc[-1,:])
        prediction=prediction**2
        if df6["SalePrice"]==prediction:
            options=df6[df6['SalePrice'] == prediction]
        else:
            options=options.sort_values(by='SalePrice')
            options=options.iloc[0]
        
        return(options) 

                                
option = prefer(preferred_LotArea, number_room, age_house, number_story,
                number_Neighborhood, number_MSZoning, budget)

# ask for desirable features
#Ask for area
preferred_LotArea = int(input("type the minimum area (between 120 and 20004): "))

#Ask for the number of room
number_room = int(input("Input the minimum number of room (between 0 and 8): "))

#Ask for the age of house
age_house = int(input("Input the maximum age of house (between 11 and 149): "))

#Ask for budget
budget = int(input("Input your maximum budget: "))

#Ask for neighbourhood 
print("type of the preferred Neighborhood['CollgCr','Veenker','Crawfor','NoRidge','Mitchel','Somerst','OldTown','BrkSide','NridgHt','Sawyer','NAmes','SawyerW','IDOTRR','MeadowV','Gilbert','StoneBr','ClearCr','Edwards','NWAmes','NPkVill','Timber','Blmngtn','BrDale','SWISU','Blueste']")
number_Neighborhood = input('inpute the prefer neighborhood: ')

#Ask for land use: 
print("type of mszoning: 'RL','RM','FV','RH','C','I','RP','A' ")   
number_MSZoning  = input('inpute the prefer mszone: ')

#Ask for the number of story
print(" type of HouseStyle ['2Story', '1Story', '1.5Fin', '1.5Unf','SFoyer', 'SLvl', '2.5Unf','2.5Fin']")           
number_story = input(' inpute the prefer house style: ')

                                
option = prefer(preferred_LotArea, number_room, age_house, number_story,
                number_Neighborhood, number_MSZoning, budget)

suggestion = options[['SalePrice', 'HouseStyle', 'MSZoning', 'LotArea','BedroomAbvGr',"Neighborhood","YearBuilt"]]











              #-----------------------$$$$$$$$$$$------------------------#



import random


def prefer(preferred_LotArea, number_room, age_house, number_story,
           number_Neighborhood, number_MSZoning, budget):
        
    df1 = df[df['LotArea'] <= preferred_LotArea]

    df2 = df1[df1['BedroomAbvGr'] == number_room]

    df3 = df2[df2['YearBuilt'] <= age_house]

    story = []
    for i in number_story:
        story.append(int(i))
        
    HouseStyle = pd.DataFrame()
    for i in range(0,len(story)+1):
        if story[i] == 0:
            HouseStyle=df3
            break
        elif story[i] != 0:
            HouseStyle =pd.concat([HouseStyle, df3[df3['HouseStyle']==list_story.get(story[i])]], axis=0)
        
    Neighbor = []
    for i in number_Neighborhood:
        Neighbor.append(int(i))
        
    Neighborhood = pd.DataFrame()
    for i in range(0,len(Neighbor)+1):
        if Neighbor[i] == 0:
            Neighborhood = HouseStyle
        elif Neighbor[i] != 0:
            Neighborhood =pd.concat([Neighborhood, HouseStyle[HouseStyle['Neighborhood']==list_Neighborhood.get(Neighbor[i])]], axis=0)
            
    MSZoningp = []
    for i in number_MSZoning:
        MSZoningp.append(int(i))
        
    MSZoning = pd.DataFrame()
    for i in range(0,len(MSZoningp)+1):
        if MSZoningp[i] == 0:
            MSZoning = Neighborhood
            break
        elif MSZoningp[i] != 0:
            MSZoning =pd.concat([MSZoning, Neighborhood[Neighborhood['MSZoning']==list_MSZoning.get(MSZoningp[i])]], axis=0)

    options = MSZoning[(MSZoning['SalePrice'] >= budget-5000) &
                       (MSZoning['SalePrice'] <= budget+5000)]
    return(options)   

                                
options = prefer(preferred_LotArea, number_room, age_house, number_story,
                 number_Neighborhood, number_MSZoning, budget)



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
list_Neighborhood = {0: 'all', 1:'CollgCr', 2:'Veenker', 3:'Crawfor', 4:'NoRidge', 5:'Mitchel', 6:'Somerst',
             7:'OldTown', 8:'BrkSide', 9:'NridgHt', 10:'Sawyer', 11:'NAmes', 12:'SawyerW', 13:'IDOTRR',
             14:'MeadowV', 15:'Gilbert', 16:'StoneBr', 17:'ClearCr', 18:'Edwards', 19:'NWAmes', 20:'NPkVill',
             21:'Timber', 22:'Blmngtn', 23:'BrDale', 24:'SWISU', 25:'Blueste'}
print(list_Neighborhood)
number_Neighborhood = input('select from the list_Neighborhood:').split()

   
#Ask for land use: if it is not important for you please type "all". :
#otherwise you can choose. please consider that if you have more than one option you have to type & between the preferred ones with out any space.
print("Input the type of preferred_MSZoning  ['RL', 'RM', 'C (all)', 'FV', 'RH']: ")

list_MSZoning  = {0:'all', 1:'RL', 2:'RM', 3:'FV', 4:'RH'} 
print(list_MSZoning)          
number_MSZoning  = input('select from the list_MSZoning:').split()


#Ask for the number of story: if it is not important for you please type "all". :
#otherwise you can choose. please consider that if you have more than one option you have to type & between the preferred ones with out any space.
print("Input the type of HouseStyle ['2Story', '1Story', '1.5Fin', '1.5Unf','SFoyer', 'SLvl', '2.5Unf','2.5Fin']")
list_story = {0:'all', 1:'2Story', 2:'1Story', 3:'1.5Fin', 4:'1.5Unf', 5:'SFoyer', 6:'SLvl', 7:'2.5Unf', 8:'2.5Fin'}
print(list_story)            
number_story = input('select from the list_story:').split()

                                
options = prefer(preferred_LotArea, number_room, age_house, number_story, number_Neighborhood, number_MSZoning, budget)







preference = {'MSSubClass':np.nan, 'MSZoning':'FV', 'LotFrontage':np.nan, 'LotArea':[960],
              'Street':np.nan, 'Alley':np.nan,'LotShape':np.nan, 'LandContour':np.nan, 'Utilities':np.nan, 
              'LotConfig':np.nan,'LandSlope':np.nan, 'Neighborhood':'Veenker', 'Condition1':np.nan,
              'Condition2':np.nan, 'BldgType':np.nan,'HouseStyle':'2Story', 'OverallQual':np.nan,
              'OverallCond':np.nan, 'YearBuilt':[20], 'YearRemodAdd':np.nan, 'RoofStyle':np.nan,
              'RoofMatl':np.nan, 'Exterior1st':np.nan, 'Exterior2nd':np.nan, 'MasVnrType':np.nan,
              'MasVnrArea':np.nan,'ExterQual':np.nan, 'ExterCond':np.nan, 'Foundation':np.nan,
              'BsmtQual':np.nan, 'BsmtCond':np.nan, 'BsmtExposure':np.nan, 'BsmtFinType1':np.nan,
              'BsmtFinType2':np.nan, 'TotalBsmtSF':np.nan, 'Heating':np.nan, 'HeatingQC':np.nan, 
              'CentralAir':np.nan, 'Electrical':np.nan, 'X1stFlrSF':np.nan,'X2ndFlrSF':np.nan,
              'GrLivArea':np.nan, 'BedroomAbvGr':[4], 'KitchenAbvGr':np.nan, 'KitchenQual':np.nan, 'TotRmsAbvGrd':np.nan,
              'Functional':np.nan, 'Fireplaces':np.nan, 'FireplaceQu':np.nan, 'GarageType':np.nan, 'GarageFinish':np.nan,
              'GarageCars':np.nan, 'GarageArea':np.nan, 'GarageQual':np.nan, 'GarageCond':np.nan, 'PavedDrive':np.nan,
              'PoolArea':np.nan, 'Fence':np.nan, 'MiscFeature':np.nan, 'SaleType':np.nan, 'SaleCondition':np.nan,
              'SalePrice': [500000],'totalbath':np.nan,
              'totalporch':np.nan}
