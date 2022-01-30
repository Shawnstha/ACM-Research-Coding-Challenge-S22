import numpy as np
import pandas as pd
#Creates a Dataframe file from the csv file 
data = pd.read_csv("mushrooms.csv") 

#Tuple with the values of 'e' and 'p' and their respective counts
(unique, counts) = np.unique(data['class'], return_counts=True)

#Print out values of the tuple 
print("Target variables", unique)
print("Counts of the target variable :", counts)

#Dataset of the independent "x" variables for linear regression, in this case being mushroom characteristicss
x = data[['cap-shape',	'cap-surface',	'cap-color',	'bruises',	'odor',	'gill-attachment',	'gill-spacing',	'gill-size',	'gill-color',	'stalk-shape',	'stalk-root',	'stalk-surface-above-ring',	'stalk-surface-below-ring',	'stalk-color-above-ring']]

#Dataset of the independent "y" variable for linear regression, in this case being the poisonous and edible attributes of the mushrooms
y = data['class']

#Conversion of the char values into dummy int values for linear regression
x = pd.get_dummies(data=x, drop_first=True)

from sklearn.model_selection import train_test_split

#Division of the mushrooms dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y , test_size=0.25, random_state=0)

from sklearn.linear_model import LogisticRegression
#Creation of logistic regression model based on the training set data
model = LogisticRegression()
model.fit(X_train, y_train)

#Predictions made on the testing data
predictions = model.predict(X_test)
from sklearn.metrics import confusion_matrix

#Accuracy determined by using the formula: (TP+TN)/(TP+FP+TN+FN)
cm = confusion_matrix(y_test, predictions)

TN, FP, FN, TP = confusion_matrix(y_test, predictions).ravel()

print('True Positive(TP)  = ', TP)
print('False Positive(FP) = ', FP)
print('True Negative(TN)  = ', TN)
print('False Negative(FN) = ', FN)
accuracy = (TP+TN) /(TP+FP+TN+FN)

print('Accuracy of the binary classification = {:0.3f}'.format(accuracy))

#Small test to determine whether the classifications are accurate
testMush = x.head(2)
predictedClassification = model.predict(testMush)
print(predictedClassification)



