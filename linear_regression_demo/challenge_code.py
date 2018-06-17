import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_csv('challenge_dataset.txt', sep=",", header=None,names=['Brain','Body'],index_col=False)
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

#train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

#visualize results
plt.scatter(x_values, y_values)
pred = body_reg.predict(x_values)
plt.plot(x_values, pred)
plt.show()

#calculate the error
from sklearn.metrics import accuracy_score
print(accuracy_score(pred,y_values))
