# Lesson 005 - Multiple Input Neuron Explained Line by Line

## Goal

In this lesson, we expanded our single-input neuron into a neuron that accepts multiple inputs.

The model learns the relationship:

```
prediction = input1 × weight1 + input2 × weight2 + bias
```

The purpose was to understand:

- Multiple inputs
- Multiple weights
- Bias
- Error calculation
- Loss calculation
- Gradients
- Batch gradient descent
- Parameter updates

---

# Full Code Explanation

## Training Data

```python
training_data = [
    ([1, 8], 5),
    ([2, 7], 8),
    ([3, 6], 11),
    ([4, 8], 14),
    ([5, 7], 17),
]
```

This is the data the model learns from.

Each example contains:

```
([inputs], target)
```

The first list contains the input values.

Example:

```
[1, 8]
```

means:

```
input 1 = 1
input 2 = 8
```

The target is the correct answer the model is trying to learn.

Example:

```
([1,8], 5)
```

means:

```
Given inputs 1 and 8, the correct output is 5.
```

The model does not know the relationship. It must discover it.

---

# Starting Parameters

```python
weight_hours = 0.5
weight_sleep = 0.5

bias = 0.0
```

Weights represent how much influence each input has.

Example:

```
hours × weight_hours
sleep × weight_sleep
```

The model starts with guesses.

Training will adjust these values.

The bias is an additional adjustment added to every prediction.

---

# Learning Controls

```python
learning_rate = 0.001
epochs = 100
```

## Learning Rate

Controls how large each update is.

Small learning rate:

```
small steps
more stable learning
```

Large learning rate:

```
large steps
risk of overshooting
```

---

## Epochs

One epoch means the model has seen the entire dataset once.

Example:

```
5 training examples
1 epoch = all 5 examples processed once
```

100 epochs means the model repeats this process 100 times.

---

# Training Loop

```python
for epoch in range(epochs):
```

Repeats the learning process.

Each cycle:

```
predict
calculate error
calculate gradients
update weights
```

---

# Reset Loss

```python
total_loss = 0
```

Creates a place to store the total error for this epoch.

Each example adds its loss to this value.

---

# Reset Gradient Storage

```python
weight_hours_gradient_total = 0
weight_sleep_gradient_total = 0
bias_gradient_total = 0
```

These store the total corrections from all examples.

The model does not immediately update after every example.

Instead:

```
collect feedback
average feedback
make one update
```

This is batch gradient descent.

---

# Process Each Training Example

```python
for inputs, target in training_data:
```

Takes each example from the dataset.

Example:

```
inputs = [1,8]
target = 5
```

---

# Separate Inputs

```python
hours = inputs[0]
sleep = inputs[1]
```

Extracts individual input values.

Lists use zero-based indexing.

Example:

```
inputs[0] = first value
inputs[1] = second value
```

---

# Make Prediction

```python
prediction = (
    hours * weight_hours
    + sleep * weight_sleep
    + bias
)
```

This is the neuron calculation.

The model combines:

```
input × weight
```

for each input.

Then adds the bias.

Example:

```
prediction =
(hours contribution)
+
(sleep contribution)
+
(bias)
```

---

# Calculate Error

```python
error = prediction - target
```

Measures how wrong the prediction is.

If:

```
prediction < target
```

error is negative.

If:

```
prediction > target
```

error is positive.

The sign tells the model which direction to adjust.

---

# Calculate Loss

```python
loss = error ** 2
```

Squares the error.

Why?

Because negative and positive errors should both count as mistakes.

Example:

```
-5² = 25
5² = 25
```

Loss measures how bad the prediction was.

---

# Add Loss

```python
total_loss += loss
```

Adds this example's mistake to the total error.

At the end of the epoch, we know how well the model performed overall.

---

# Calculate Gradients

```python
weight_hours_gradient = error * hours
```

Calculates how much the hours weight should change.

Large input:

```
larger gradient
```

Small input:

```
smaller gradient
```

---

```python
weight_sleep_gradient = error * sleep
```

Calculates the correction for the sleep weight.

---

```python
bias_gradient = error
```

The bias affects every prediction equally.

Its gradient is simply the error.

---

# Store Gradients

```python
weight_hours_gradient_total += weight_hours_gradient

weight_sleep_gradient_total += weight_sleep_gradient

bias_gradient_total += bias_gradient
```

Instead of updating immediately:

```
example 1 update
example 2 update
example 3 update
```

we collect all feedback first.

---

# Average Gradients

```python
weight_hours_gradient_average = (
    weight_hours_gradient_total / len(training_data)
)
```

Calculates the average correction.

The model gets feedback from all examples instead of reacting to only one.

---

The same happens for:

```python
weight_sleep_gradient_average
```

and:

```python
bias_gradient_average
```

---

# Update Parameters

```python
weight_hours -= learning_rate * weight_hours_gradient_average
```

Adjusts the weight.

The rule:

```
new value =
old value - adjustment
```

If the gradient is negative:

```
subtracting negative increases weight
```

If the gradient is positive:

```
subtracting positive decreases weight
```

---

The same process updates:

```python
weight_sleep
```

and:

```python
bias
```

---

# Display Progress

```python
if epoch % 10 == 0:
```

Every 10 epochs, print progress.

This lets us watch:

- loss decreasing
- weights changing
- model learning

---

# What We Built

This small program contains the foundation of neural network training:

```
Inputs
  ↓
Weights
  ↓
Prediction
  ↓
Error
  ↓
Loss
  ↓
Gradients
  ↓
Weight Updates
  ↓
Improved Prediction
```

The next step is adding activation functions.

Without activation functions, this neuron is only capable of learning linear relationships.

Adding activation functions allows neural networks to learn complex patterns.
