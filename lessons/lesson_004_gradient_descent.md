# Lesson 004 – Gradient Descent

## Objective

The goal of this lesson was to understand how a machine learning model improves itself.

The model starts with incorrect guesses for:

- Weight
- Bias

It then repeatedly adjusts these values to reduce error.

This process is called:

**Gradient Descent**

---

# The Training Problem

The model is trying to learn:

y = 2x + 1

The training examples are:

Input   Target
1         3
2         5
3         7
4         9
5        11

The model is not given the equation.

It must discover the relationship by adjusting its parameters.

---

# The Neuron Equation

The prediction is calculated using:

```python
prediction = input * weight + bias
The weight controls how much influence the input has.
The bias shifts the prediction up or down.
Example:
input = 5
weight = 2
bias = 1
Prediction:
5 * 2 + 1 = 11
Starting Parameters
The model begins with guesses:
weight = 0.5
bias = 0.0
These values are wrong.
The purpose of training is to improve them.
Epochs
An epoch is one complete pass through the training data.
Example:
Epoch 1:

Example 1
Example 2
Example 3
Example 4
Example 5
After every epoch, the model has another chance to improve.
The training loop:
for epoch in range(epochs):
Breakdown:
for
Creates a loop.
epoch
Stores the current training round.
range(epochs)
Creates a sequence of numbers from 0 up to the number of epochs.
Example:
range(5)
creates:
0, 1, 2, 3, 4
Processing Multiple Examples
The model uses:
for input_value, target in zip(inputs, targets):
The zip() function combines matching values.
Example:
inputs = [1,2,3]

targets = [3,5,7]
zip creates:
(1,3)
(2,5)
(3,7)
Each input stays connected to the correct answer.
Prediction
For every example:
prediction = input_value * weight + bias
The model produces a guess.
Example:
Input = 1

Weight = 0.5

Bias = 0
Prediction:
1 * 0.5 + 0 = 0.5
The target is:
3
The model is wrong.
Error Calculation
The error is:
error = prediction - target
Example:
Prediction = 0.5

Target = 3
Error:
0.5 - 3 = -2.5
A negative error means the prediction is too low.
Loss
Loss measures how bad the prediction was.
The model uses:
loss = error ** 2
The ** operator means exponent.
Example:
5 ** 2
means:
5 × 5 = 25
Squaring the error:
Removes negative values
Makes large mistakes more important
Example:
Error = -5

Loss = 25
Gradients
The model needs to know:
Which direction should weight move?
Which direction should bias move?
A gradient provides that information.
Weight gradient:
weight_gradient = error * input
Bias gradient:
bias_gradient = error
The gradient tells the model how much each parameter contributed to the mistake.
Averaging Gradients
The model sees multiple examples.
Each example creates its own gradient.
The model combines them:
average_gradient = total_gradient / number_of_examples
This prevents one example from dominating the update.
The model learns from the entire dataset.
Updating Parameters
The update rule:
weight = weight - learning_rate * weight_gradient
The model moves the weight in the opposite direction of the error.
The learning rate controls the size of the step.
Example:
Large learning rate:
Big adjustments
Fast learning
Higher chance of overshooting
Small learning rate:
Small adjustments
Slower learning
More controlled
Training Results
Starting values:
Weight: 0.5
Bias: 0
Loss: 34.75
After training:
Weight: approximately 2.13
Bias: approximately 0.54
Loss: 0.0396
The model reduced its error dramatically.
It learned a relationship close to:
y = 2x + 1
Key Concepts Learned
Gradient descent
Epochs
Training loops
Error calculation
Loss functions
Gradients
Parameter updates
Learning rate
Optimization
Key Takeaway
Gradient descent is the process that allows a model to learn.
A model:
Makes a prediction
Measures its mistake
Calculates how to improve
Adjusts its parameters
Repeats the process
Large AI systems use much more advanced versions of this same idea.
