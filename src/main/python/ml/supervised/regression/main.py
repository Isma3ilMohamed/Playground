import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

### Generate random data of 200 samples for linear regression
x = np.random.rand(200, 1)

### Randomly generate samples, shift them to have a mean of 5
### and a standard deviation of -3
y = - 3 * x + 5 + np.random.rand(200, 1)

### Initialize linear regression model and use it for training
### by specifying input and output variables
regress_model = LinearRegression()

### Fit the data (train the model)
regress_model.fit(x, y)

### Predict the output values from the input x to assess the performance of the trained model
y_predicted = regress_model.predict(x)

### Model evaluation by calculating root mean squared error
rmse = np.sqrt(mean_squared_error(y, y_predicted))

### Display the learned parameters, plot the learned model, and print the values of the model
print('Slope:', regress_model.coef_,
      '\nIntercept:', regress_model.intercept_,
      '\nRoot mean squared error:', rmse)
### plotting data points
plt.scatter(x, y, color='r')
plt.xlabel('x'), plt.ylabel('y')
### plotting predicted values
plt.plot(x, y_predicted, color='b')
plt.legend(['Model', 'Data points'])
plt.show()
