Logistic Regression
Definition: Logistic regression is a model to predict the probability of a binary event. It can be used to analyze trends and predict values in a given dataset.

Sigmoid function:
In logistic regression the predicted value is converted to a categorical value using the sigmoid function. The sigmoid function is chosen because of it property to return values between 0 and 1. The larger the value of x, the closer the output will be to 1. The lower the values of x (negative), the closer the output is to 0.

y =1(1+(e^-z))

where
z = input value
e = euler's constant

Gradient Descent and Cost function
The function z = b0 + b1x1 + b2x2... depending on the number of dependent variables. To find the most accurate values of b0, b1 ... we must minimize the cost function. Stochastic gradient descent can be used to calculate and update the coefficient for every iteration.

Cost function = J = 1/m(∑ ylog(h(x)) + (1-y)log(1-h(x)))

where
m = number of data points
h(x) = sigmoid function
y = output

The goal is to make the derivative of the cost function = 0

Updating the coefficients

b = b - alpha∑((1/(1+e^z))-y)x

Another way to update the coefficients

b = b + alpha * (y-prediction) * prediction * (1-prediction) * x

After many iterations, the coefficients will tend to their optimal values which allows us to use them to predict the probability of a certain event. We receive a binary number as output.