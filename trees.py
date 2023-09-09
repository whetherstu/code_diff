from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
import pandas as pd

subtrainLabel = pd.read_csv('E:\\big\\subtrainLabels.csv')
subtrainfeature = pd.read_csv("E:\\big\\3gramfeature.csv")

subtrain = pd.merge(subtrainLabel,subtrainfeature,on='Id')
labels = subtrain.Class
subtrain.drop(["Class","Id"], axis=1, inplace=True)
subtrain = subtrain.iloc[:,:].values
srf = RF(n_estimators=500, n_jobs=-1)
clf_s = cross_val_score(srf, subtrain, labels, cv=10)
print(clf_s)