# Lesson 002 – Building My First Artificial Neuron

## Objective

The goal of this lesson was to build the simplest possible machine learning model from scratch.

Rather than using a machine learning library like PyTorch, I wanted to understand exactly what happens inside a neuron.

---

# What is a Neuron?

An artificial neuron receives an input, performs a calculation, and produces an output (prediction).

For this lesson the neuron followed a very simple equation:

Prediction = Input × Weight + Bias

This is called a linear model.

---

# Components

## Input

The value given to the model.

Example:

Input = 5

---

## Weight

The weight determines how strongly the input influences the prediction.

Larger weights make the prediction increase faster.

Smaller weights reduce the prediction.

---

## Bias

The bias shifts every prediction up or down.

It allows the model to fit relationships that do not pass through zero.

Example:

y = 2x

needs no bias.

But

y = 2x + 3

requires a bias of 3.

---

## Prediction

The neuron combines everything together.

Example:

Input = 5

Weight = 2

Bias = 3

Prediction = 5 × 2 + 3 = 13

---

# Measuring Error

The model compares its prediction against the correct answer.

Difference:

Error = Target − Prediction

To prevent positive and negative errors from cancelling each other out, the error is squared.

Loss = (Target − Prediction)²

The loss tells the model how wrong it is.

A loss closer to zero means better predictions.

---

# Learning

The neuron learns by making small adjustments to:

- Weight
- Bias

After every prediction it checks:

"Did this change make the loss smaller?"

If yes, it continues adjusting in that direction.

If not, it adjusts differently.

Repeating this process over many epochs gradually improves the model.

---

# Important Concepts Learned

- Variables
- Functions
- Inputs
- Outputs
- Predictions
- Weight
- Bias
- Loss
- Epochs
- Training loop
- Gradient descent (basic idea)

---

# Key Takeaway

A neuron is not "thinking."

It is repeatedly adjusting mathematical parameters to reduce prediction error.

Learning occurs because each adjustment attempts to move the loss closer to zero.

This simple idea forms the foundation of modern machine learning.
