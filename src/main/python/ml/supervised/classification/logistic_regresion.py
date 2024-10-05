import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# One-dimensional data generation
# Mostly sklearn expects x data in 2D form, and output y in 1D
# np.arange() produces a 1D x data, we have to reshape it in 2D using reshape(-1,1)
# where -1 means that the dimension 0 (number of rows) can have any number of samples (generally unknown to us)
x = np.arange(10).reshape(-1, 1)

# Class, response, or output variable corresponding to input x
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

model = LogisticRegression(solver='liblinear', random_state=0, max_iter=100)

# Fit (train) the model using x, y pair of values
model.fit(x, y)

# The attribute .classes_ represents the array of distinct values that y takes
print('Classes:', model.classes_,
      '\nIntercept:', model.intercept_,
      '\nCoefficient:',model.coef_,
      '\nPredicted values:', model.predict(x),
      '\nScore:', model.score(x, y),
      '\nClassification report:\n',classification_report(y, model.predict(x)))

#Get the confusion matrix
cf_mat = confusion_matrix(y, model.predict(x))
print('Confusion matrix with rows (true labels) and columns (predicted labels) of class 0 and class 1: \n', cf_mat)