# multiple linear Regression

# imported libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importind the data set
df=pd.read_csv("50_startups.csv")
df.head()
x=df.iloc[:,:-1]
y=df.iloc[:,-1]

# convert the column into categarical coluns
states=pd.get_dummies(x["State"],drop_first=True)
#Drop the state coulmn
x=x.drop("State",axis=1)

#concat the dummies
x=pd.concat([x,states],axis=1)


#splittind the dataset into training set and test data set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)


#fitting multiple linear Regression to training set
from sklearn.linear_model import LinearRegression

res=LinearRegression()
res.fit(x_train,y_train)


#prediciting the test set resultes
y_pred=res.predict(x_test)
print(y_pred)
scor=res.score(x,y)
print(scor)

from sklearn.metrics import r2_score
r2_scr=r2_score(y_test, y_pred)