"""
Lesson 006: Activation Functions

A neuron first calculates a raw output:

    raw_output = (input_1 * weight_1) + (input_2 * weight_2) + bias

An activation function transforms that raw output before it moves to the
next layer.

This experiment demonstrates:

1. ReLU
2. Leaky ReLU
3. Sigmoid
4. Softmax
5. Single-label classification
6. Multi-label classification
"""

import math


# ---------------------------------------------------------
# ReLU
# ---------------------------------------------------------
# ReLU means Rectified Linear Unit.
#
# Negative values become 0.
# Positive values remain unchanged.
#
# ReLU(x) = max(0, x)
#
# ReLU is commonly used inside hidden layers because it is
# simple and usually allows strong gradients to move backward.
#
# Weakness:
# A neuron that repeatedly receives negative values may remain
# at 0 and stop learning. This is called a dead ReLU.


def relu(x):
    return max(0, x)


# ---------------------------------------------------------
# Leaky ReLU
# ---------------------------------------------------------
# Leaky ReLU behaves like ordinary ReLU for positive values.
#
# For negative values, it allows a small amount through instead
# of replacing the value with exactly 0.
#
# This small negative slope allows a gradient to continue moving
# backward, which may help prevent a dead neuron.


def leaky_relu(x, alpha=0.01):
    if x >= 0:
        return x

    return alpha * x


# ---------------------------------------------------------
# Sigmoid
# ---------------------------------------------------------
# Sigmoid compresses any input into a value between 0 and 1.
#
# Large negative inputs produce values close to 0.
# An input of 0 produces exactly 0.5.
# Large positive inputs produce values close to 1.
#
# Sigmoid is useful when an output should act like an independent
# probability or confidence score.
#
# Weakness:
# At values close to 0 or 1, the sigmoid curve becomes almost flat.
# That produces very small gradients and can cause slow learning.
# This is part of the vanishing-gradient problem.


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# ---------------------------------------------------------
# Softmax
# ---------------------------------------------------------
# Softmax takes several raw scores, called logits, and converts
# them into probabilities.
#
# The resulting probabilities:
#
# 1. Are between 0 and 1
# 2. Add up to approximately 1
# 3. Compete against one another
#
# Softmax is useful when exactly one class should win.
#
# Example:
# An image should be classified as Cat, Dog, or Bird.


def softmax(values):
    exponentials = [math.exp(value) for value in values]
    total = sum(exponentials)

    return [value / total for value in exponentials]


# ---------------------------------------------------------
# ReLU examples
# ---------------------------------------------------------

print("ReLU examples")

for value in [-8, 0, 6]:
    print(f"ReLU({value}) = {relu(value)}")


# Expected idea:
#
# -8 becomes 0 because negative values are blocked.
#  0 remains 0.
#  6 remains 6 because positive strength is preserved.


# ---------------------------------------------------------
# Leaky ReLU examples
# ---------------------------------------------------------

print("\nLeaky ReLU examples")

for value in [-8, 0, 6]:
    print(f"Leaky ReLU({value}) = {leaky_relu(value)}")


# Expected idea:
#
# -8 becomes -0.08 rather than becoming exactly 0.
#
# This small negative output means the neuron still has a small
# path through which learning can occur.


# ---------------------------------------------------------
# Sigmoid examples
# ---------------------------------------------------------

print("\nSigmoid examples")

for value in [-8, 0, 8]:
    print(f"Sigmoid({value}) = {sigmoid(value):.4f}")


# Expected idea:
#
# Sigmoid(-8) is close to 0.
# Sigmoid(0) is exactly 0.5.
# Sigmoid(8) is close to 1.
#
# Sigmoid does not preserve the original number.
# It compresses the number into a bounded score.


# ---------------------------------------------------------
# Softmax single-label example
# ---------------------------------------------------------

print("\nSoftmax example")

# These are raw output scores from a hypothetical final layer.
# Raw scores used before softmax are called logits.

logits = [2, 5, 1]

labels = ["Cat", "Dog", "Bird"]

probabilities = softmax(logits)

for label, probability in zip(labels, probabilities):
    print(f"{label}: {probability:.4f}")


# Softmax probabilities should add up to approximately 1.

print(f"Total: {sum(probabilities):.4f}")


# Find the index of the largest probability.

predicted_index = probabilities.index(max(probabilities))

# Use that index to retrieve the matching label.

predicted_label = labels[predicted_index]

print(f"Prediction: {predicted_label}")


# Expected idea:
#
# Dog has the largest original logit, so Dog receives the highest
# probability and becomes the prediction.
#
# Softmax is appropriate because Cat, Dog, and Bird are being
# treated as mutually exclusive choices.


# ---------------------------------------------------------
# Sigmoid multi-label example
# ---------------------------------------------------------

print("\nSigmoid multi-label example")

# Each label receives its own independent logit.
#
# Unlike softmax, these labels do not compete against one another.
# Several labels may be true at the same time.

email_logits = {
    "Work-related": 3.0,
    "Urgent": 2.0,
    "Personal": -3.0,
}

# Any probability at or above this threshold is selected.

threshold = 0.5

for label, logit in email_logits.items():
    probability = sigmoid(logit)
    selected = probability >= threshold

    print(
        f"{label}: probability={probability:.4f}, "
        f"selected={selected}"
    )


# Expected idea:
#
# Work-related and Urgent can both be selected.
# Personal can remain unselected.
#
# This is why sigmoid works well for multi-label classification:
# each answer is evaluated independently.
#
# Clean rule:
#
# One mutually exclusive answer -> Softmax
# Multiple overlapping answers  -> Sigmoid
