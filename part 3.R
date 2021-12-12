
rm(list=ls(all.names=TRUE))

library(faraway)
library(mice)
library(VIM)
library(naniar)

data = read.csv("E:/Dr.farsad/Project/clean_data_train.csv")
data$X = NULL

MSZoning <- readline(prompt="Enter MSZoning {RL RM  C (all) FV  RH}: ")
LotArea <- as.integer(readline(prompt="Enter LotArea: "))
YearBuilt <- as.integer(readline(prompt="Enter YearBuilt: "))

list_Neighborhood = ('CollgCr Veenker Crawfor NoRidge Mitchel Somerst 
  OldTown BrkSide NridgHt Sawyer NAmes   SawyerW IDOTRR MeadowV Gilbert StoneBr
  ClearCr Edwards NWAmes  NPkVill Timber  Blmngtn BrDale  SWISU   Blueste')
Neighborhood <- readline(prompt="Enter Neighborhood from list_Neighborhood: ")

HouseStyle <- readline(prompt="Enter HouseStyle 2Story 1Story 1.5Fin 1.5Unf SFoyer SLvl 2.5Unf 2.5Fin: ")
BedroomAbvGr <- as.integer(readline(prompt="Enter number of Bedroom between 0 and 8: "))
SalePrice <- as.integer(readline(prompt="Enter SalePrice: "))

library(plyr)
new.row <- data.frame('MSZoning'=MSZoning, 'LotArea'= LotArea, 'YearBuilt'= YearBuilt, 
                      'Neighborhood'= Neighborhood, 'HouseStyle'= HouseStyle,
                      'BedroomAbvGr'= BedroomAbvGr, stringsAsFactors=F)

df <- rbind.fill(da, new.row)
i = mice(df, method = 'rf', m=2 , maxit = 0)
c =complete(i,1)
c[nrow(df),62]

newdata = as.data.frame(c[nrow(df),-(SalePrice)])
predict(lm, newdata = newdata)

lm = lm(SalePrice~., data = data)
summary(lm)


        







preference = data.frame('MSSubClass'= NA, 'MSZoning'='FV', 'LotFrontage'= NA, 'LotArea'= 960,
                        'Street'= NA, 'Alley'= NA,'LotShape'= NA, 'LandContour'= NA, 'Utilities'= NA, 
                        'LotConfig'= NA,'LandSlope'= NA, 'Neighborhood'='Veenker', 'Condition1'= NA,
                        'Condition2'= NA, 'BldgType'= NA,'HouseStyle'='2Story', 'OverallQual'= NA,
                        'OverallCond'= NA, 'YearBuilt'= 20, 'YearRemodAdd'= NA, 'RoofStyle'= NA,
                        'RoofMatl'= NA, 'Exterior1st'= NA, 'Exterior2nd'= NA, 'MasVnrType'= NA,
                        'MasVnrArea'= NA,'ExterQual'= NA, 'ExterCond'= NA, 'Foundation'= NA,
                        'BsmtQual'= NA, 'BsmtCond'= NA, 'BsmtExposure'= NA, 'BsmtFinType1'= NA,
                        'BsmtFinType2'= NA, 'TotalBsmtSF'= NA, 'Heating'= NA, 'HeatingQC'= NA, 
                        'CentralAir'= NA, 'Electrical'= NA, 'X1stFlrSF'= NA,'X2ndFlrSF'= NA,
                        'GrLivArea'= NA, 'BedroomAbvGr'= 4, 'KitchenAbvGr'= NA, 'KitchenQual'= NA, 'TotRmsAbvGrd'= NA,
                        'Functional'= NA, 'Fireplaces'= NA, 'FireplaceQu'= NA, 'GarageType'= NA, 'GarageFinish'= NA,
                        'GarageCars'= NA, 'GarageArea'= NA, 'GarageQual'= NA, 'GarageCond'= NA, 'PavedDrive'= NA,
                        'PoolArea'= NA, 'Fence'= NA, 'MiscFeature'= NA, 'SaleType'= NA, 'SaleCondition'= NA,
                        'SalePrice'= 500000,'totalbath'= NA,
                        'totalporch'= NA)
