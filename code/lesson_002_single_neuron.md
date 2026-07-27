# Lesson 002: Building a Single Neuron

## Goal

Create a neuron that can predict an output and adjust itself.

---

## The Formula

prediction = input * weight + bias

---

## Weight

Weight controls how much influence the input has.

Example:

Input = 5
Weight = 2

5 × 2 = 10

---

## Bias

Bias shifts the prediction up or down.

Example:

Weight = 2
Bias = 3

5 × 2 + 3 = 13

---

## Loss

Loss measures how far the prediction is from the target.

Loss = (target - prediction)^2

---

## Gradient Descent

The model uses the loss to decide:
- which direction to adjust
- how much to adjust

Then it repeats over many epochs.
