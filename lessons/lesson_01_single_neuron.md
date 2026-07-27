# Lesson 01 - Building a Single Neuron From Scratch

## Goal

Build a simple neural network that can learn the relationship:

y = 2x

The purpose was not to build a useful AI model, but to understand the fundamentals behind machine learning.

---

## What I Learned

A neural network learns by adjusting values called weights and biases.

The basic equation:

prediction = input × weight + bias

---

## Weight

The weight controls how strongly the input affects the output.

Example:

If:

weight = 2

input = 5

then:

prediction = 5 × 2 = 10

---

## Bias

Bias is an additional value added to the prediction.

prediction = input × weight + bias

It allows the model to shift the entire prediction up or down.

---

## Loss

Loss measures how far the prediction is from the correct answer.

In this project:

loss = error²

A larger loss means the prediction is farther away.

---

## Training Process

The model repeats:

1. Make a prediction
2. Compare prediction to the answer
3. Calculate error
4. Adjust the weight
5. Repeat for many epochs

---

## Results

The neuron learned:

weight ≈ 2

bias ≈ 0

Testing:

6 → 12  
7 → 14  
10 → 20  
100 → 200

The model was able to generalize the pattern beyond the training examples.

---

## Next Steps

- Add bias training
- Create reusable functions
- Build a more flexible neuron
- Eventually compare this implementation to PyTorch
