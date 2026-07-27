# Lesson 003 – Learning From Multiple Examples

## Objective

The goal of this lesson was to teach a neuron using multiple examples instead of a single input/output pair.

In the previous lesson, the model learned:

5 → 13

This proved that the model could adjust its parameters.

However, real machine learning models do not learn from one example. They learn from datasets containing many examples.

---

# Training Data

The model was given:

Input   Target
1         3
2         5
3         7
4         9
5        11

The hidden relationship was:

y = 2x + 1

The model was not told this equation.

It had to discover the pattern by adjusting:

- Weight
- Bias

---

# Moving From One Example to Many

Previously:

Input
  |
  v
Neuron
  |
  v
Prediction
  |
  v
Loss
  |
  v
Update parameters

The model learned after one example.

With multiple examples:

Example 1
Example 2
Example 3
Example 4
Example 5
    |
    v
Calculate predictions
    |
    v
Calculate losses
    |
    v
Average the error
    |
    v
Update parameters

The model now learns from the overall pattern.

---

# Using Lists

Python lists were used to store training data:

```python
inputs = [1, 2, 3, 4, 5]

targets = [3, 5, 7, 9, 11]
Lists allow the model to work with many examples instead of only one.
Using zip()
The zip() function allows Python to connect matching inputs and targets.
Example:
for input_value, target in zip(inputs, targets):
This creates pairs:
(1,3)
(2,5)
(3,7)
(4,9)
(5,11)
Each input stays connected to its correct target.
Average Loss
Each example produces its own error.
The model combines all errors:
Total Loss = Loss1 + Loss2 + Loss3 + ...
Then calculates:
Average Loss = Total Loss / Number of Examples
The average tells the model how well it performs across the entire dataset.
Batch Gradient Descent
This version uses batch gradient descent.
The process:
Model sees every training example
Model calculates each loss
Losses are averaged
Gradients are calculated
Weight and bias are updated
The model updates once after seeing the full dataset.
Gradients
A gradient tells the model:
Which direction should the parameter move?
How much should it change?
For weight:
weight gradient = error × input
For bias:
bias gradient = error
The model uses these values to adjust itself.
Learning Rate
The learning rate controls the size of each adjustment.
Example:
Large learning rate:

Large steps
Faster learning
Higher chance of overshooting


Small learning rate:

Small steps
Slower learning
More controlled
The model needs a balance between speed and stability.
Results
The model started with:
Weight = 0.5
Bias = 0
After training:
Weight ≈ 2
Bias ≈ 1
The model discovered the relationship:
y = 2x + 1
without being given the equation.
Key Concepts Learned
Training datasets
Multiple examples
Python lists
zip()
Batch gradient descent
Average loss
Gradients
Learning rate
Pattern recognition
Generalization
Key Takeaway
Machine learning is not about memorizing examples.
A model learns by adjusting parameters until it discovers patterns that allow it to make predictions on new data.
This lesson was the first step from a simple mathematical experiment toward a real machine learning system.
