from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
import pandas as pd
import openpyxl

#subtrainLabel = pd.read_csv('E:\\big\\subtrainLabels.csv')
subtrainfeature1 = pd.read_csv("E:\\big\\3gramfeature.csv")
subtrainfeature2 = pd.read_csv("E:\\big\\imgfeature.csv")
subtrain = pd.merge(subtrainfeature1,subtrainfeature2,on='Id')

label = pd.read_csv('E:\\big\\subtrainLabels.csv')

subtrain_df = pd.merge(subtrain,label,on='Id')

subtrain_df.to_csv("merge_label", index=True)



labels = subtrain_df.Class
subtrain_df.drop(["Class","Id"], axis=1, inplace=True)
print(subtrain_df)
subtrain_df = subtrain_df.iloc[:,:].values

srf = RF(n_estimators=500, n_jobs=-1)
clf_s = cross_val_score(srf, subtrain_df, labels, cv=9)
print(clf_s)