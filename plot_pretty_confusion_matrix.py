import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

y_true = y_test
y_pred = model.predict(X_test)

classes_pred = [x+'_pred' for x in list(model.classes_)] # model : the classification model. Eg : RandomForest
classes_true = [x+'_true' for x in list(model.classes_)]    
    
confusion_mat = pd.DataFrame(confusion_matrix(y_true, y_pred), index=classes_true,columns=classes_pred)

plt.figure(figsize = (10,7))
sn.heatmap(confusion_mat, cmap='Blues', annot=True,fmt='g')
