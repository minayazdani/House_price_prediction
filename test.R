
p = read.csv('E:/Dr.Farsad/Project/test_data.csv')
p = read.csv('E:/Dr.Farsad/Project/train_data.csv')

p$MoSold = factor(p$MoSold)           
p$YrSold = factor(p$YrSold)
yeartoage = function(x){
  buildingage = 2021 - x
  print(buildingage)
}

yb = yeartoage(p$YearBuilt)
yr = yeartoage(p$YearRemodAdd)
yg = yeartoage(p$GarageYrBlt)  

p$YearBuilt = as.integer(yb)
p$YearRemodAdd = as.integer(yr)
p$GarageYrBlt = as.integer(yg)

p$MSSubClass = ordered(p$MSSubClass)
p$OverallQual = ordered(p$OverallQual)
p$OverallCond = ordered(p$OverallCond)
p$ExterQual =ordered(p$ExterQual)
p$ExterCond=ordered(p$ExterCond)
p$BsmtQual =ordered(p$BsmtQual)
p$BsmtCond=ordered(p$BsmtCond)
p$BsmtExposure= ordered(p$BsmtExposure)
p$BsmtFinType1 =ordered(p$BsmtFinType1)
p$BsmtFinType2=ordered(p$BsmtFinType2)
p$HeatingQC=ordered(p$HeatingQC)
p$KitchenQual=ordered(p$KitchenQual)
p$FireplaceQu=ordered(p$FireplaceQu)
p$GarageQual =ordered(p$GarageQual)
p$GarageCond=ordered(p$GarageCond)


p$Alley = as.character(p$Alley)
p$Alley[is.na(p$Alley) == TRUE]='NOACCESS'
p$Alley[p$Alley==""]='NOACCESS'
p$Alley = factor(p$Alley)

p$Utilities = as.character(p$Utilities)
p$Utilities[is.na(p$Utilities) == TRUE] = 'AllPub'
p$Utilities = factor(p$Utilities)

p$MasVnrType = as.character(p$MasVnrType)
p$MasVnrType[p$MasVnrType==""]='CBlock'
p$MasVnrType = factor(p$MasVnrType)

p$BsmtQual = as.character(p$BsmtQual)
p$BsmtQual[is.na(p$BsmtQual) == TRUE] = 'NoBa'
p$BsmtQual[p$BsmtQual==""]='NoBa'
p$BsmtQual = factor(p$BsmtQual)

p$BsmtCond = as.character(p$BsmtCond)
p$BsmtCond[is.na(p$BsmtCond) == TRUE] = 'NoBa'
p$BsmtCond[p$BsmtCond==""]='NoBa' 
p$BsmtCond = factor(p$BsmtCond)

p$BsmtExposure = as.character(p$BsmtExposure)
p$BsmtExposure[is.na(p$BsmtExposure) == TRUE] = 'NoBa'
p$BsmtExposure[p$BsmtExposure==""]='NoBa'
p$BsmtExposure = factor(p$BsmtExposure)

p$BsmtFinType1 = as.character(p$BsmtFinType1)
p$BsmtFinType1[is.na(p$BsmtFinType1) == TRUE] = 'NoBa'
p$BsmtFinType1[p$BsmtFinType1==""]='NoBa'
p$BsmtFinType1 = factor(p$BsmtFinType1)

p$BsmtFinType2 = as.character(p$BsmtFinType2)
p$BsmtFinType2[is.na(p$BsmtFinType2) == TRUE] = 'NoBa'
p$BsmtFinType2[p$BsmtFinType2==""]='NoBa'
p$BsmtFinType2 = factor(p$BsmtFinType2)

p$Electrical = as.character(p$Electrical)
p$Electrical[p$Electrical==""]='SBrkr'
p$Electrical = factor(p$Electrical)

p$FireplaceQu = as.character(p$FireplaceQu)
p$FireplaceQu[is.na(p$FireplaceQu)==TRUE]='NOF'
p$FireplaceQu[p$FireplaceQu==""]='NOF'
p$FireplaceQu = factor(p$FireplaceQu)

p$GarageType = as.character(p$GarageType)
p$GarageType[is.na(p$GarageType)==TRUE]='NOG'
p$GarageType[p$GarageType==""]='NOG'
p$GarageType = factor(p$GarageType)

p$GarageFinish = as.character(p$GarageFinish)
p$GarageFinish[is.na(p$GarageFinish)==TRUE]='NOG'
p$GarageFinish[p$GarageFinish==""]='NOG' 
p$GarageFinish = factor(p$GarageFinish)

p$GarageQual = as.character(p$GarageQual)
p$GarageQual[is.na(p$GarageQual)==TRUE]='NOG'
p$GarageQual[p$GarageQual==""]='NOG'
p$GarageQual = factor(p$GarageQual)

p$GarageCond = as.character(p$GarageCond)
p$GarageCond[is.na(p$GarageCond)==TRUE]='NOG'
p$GarageCond[p$GarageCond==""]='NOG'
p$GarageCond = factor(p$GarageCond)

p$PoolQC = as.character(p$PoolQC)
p$PoolQC[is.na(p$PoolQC)==TRUE]='NOP'
p$PoolQC[p$PoolQC==""]='NOP'
p$PoolQC = factor(p$PoolQC)

p$Fence = as.character(p$Fence)
p$Fence[is.na(p$Fence)==TRUE]='NOF'
p$Fence[p$Fence==""]='NOF'
p$Fence = factor(p$Fence)

p$MiscFeature = as.character(p$MiscFeature)
p$MiscFeature[is.na(p$MiscFeature)==TRUE]='NONE'
p$MiscFeature[p$MiscFeature==""]='NONE'
p$MiscFeature = factor(p$MiscFeature)

#new ariable 
p$totalbath=(0.5*p$HalfBath)+p$FullBath+(0.5*p$BsmtHalfBath)+p$BsmtFullBath
#columns:47,48,49,50
p$totalporch=p$OpenPorchSF+p$X3SsnPorch+p$EnclosedPorch+p$ScreenPorch+p$WoodDeckSF
#columns:67,68,69,70,72
#this is proven


library(mice)
library(VIM)

impu= mice(p, m=1,  method = 'rf', maxit = 0)
densityplot(impu)
comp=complete(impu,1)

#delete
comp$MiscVal = NULL 
comp$GarageYrBlt = NULL 
comp$LowQualFinSF = NULL
comp$YrSold = NULL 
comp$MoSold = NULL 

#save
write.csv(comp,"E:/Dr.Farsad/Project/train.csv")

v = read.csv("E:/Dr.Farsad/Project/train.csv")
v = v[,-1]
dim(v)
sapply(v, function(x) sum(is.na(x)))

p = read.csv('E:/Dr.Farsad/Project/test.csv')
df = read.csv('E:/Dr.Farsad/Project/train.csv')

df$X = NULL
p$X = NULL

lm = lm(SalePrice~. , df)




