# Lesson 006: Activation Functions

## Why Activation Functions Exist

A neuron first calculates a raw value:

```text
raw output = (input₁ × weight₁) + (input₂ × weight₂) + bias
```

An activation function transforms that raw value before it moves to the next layer.

Without nonlinear activation functions, stacking many layers would still behave like one larger linear calculation. The network would be unable to learn many complicated patterns.

## ReLU

ReLU means **Rectified Linear Unit**.

```text
ReLU(x) = max(0, x)
```

Examples:

```text
ReLU(-8) = 0
ReLU(0)  = 0
ReLU(6)  = 6
```

ReLU blocks negative values and preserves positive values. A zero still moves forward mathematically, but contributes nothing to the next neuron's calculation.

```text
next output = (4 × weight₁) + (0 × weight₂) + (7 × weight₃)
```

The middle connection exists, but its current contribution is zero.

### Why ReLU Is Useful

ReLU lets neurons behave like feature detectors. A positive raw output can represent a detected pattern and retain its strength. A negative raw output becomes zero for that input.

### Dead ReLU

For negative inputs, ordinary ReLU has a zero gradient. If a neuron repeatedly stays on that side, it may stop receiving useful weight updates. This is called a **dead ReLU**.

## Leaky ReLU

Leaky ReLU leaves a small slope on the negative side.

Example:

```text
LeakyReLU(-5) = -0.05
```

Because the gradient is small but nonzero, gradient descent can still adjust the weights. This gives the neuron a chance to move back into a useful range.

## Sigmoid

Sigmoid compresses any real input into a value between 0 and 1.

```text
sigmoid(x) = 1 / (1 + e⁻ˣ)
```

Examples:

```text
sigmoid(-5) ≈ 0.007
sigmoid(0)  = 0.5
sigmoid(5)  ≈ 0.993
sigmoid(8)  ≈ 0.9997
sigmoid(2500) ≈ 1
```

Its mathematical output is always greater than 0 and less than 1, although computers may round extreme values to exactly `0.0` or `1.0`.

Sigmoid is useful when one output should behave like an independent probability or confidence score.

## Vanishing Gradients

Sigmoid becomes nearly flat for very positive or very negative inputs. A flat curve has a very small slope, so the gradient becomes tiny.

```text
tiny gradient
→ tiny weight update
→ slow learning
```

Sigmoid learns most strongly near an input of 0, where its output is 0.5 and the curve is steepest. Near outputs of 0 or 1, learning can become much slower.

This helps explain why ReLU is often preferred inside hidden layers.

## Softmax

Softmax is used when several output classes should compete and one class should win.

Suppose a model produces raw scores called **logits**:

```text
Cat:  2
Dog:  5
Bird: 1
```

Softmax turns them into values between 0 and 1 that add up to 1:

```text
Cat:  0.047
Dog:  0.936
Bird: 0.017
```

The model chooses Dog because it has the largest value.

## Sigmoid Versus Softmax

Use **softmax** when the classes are mutually exclusive and the model should choose one answer.

```text
Cat
Dog
Bird
```

Use **sigmoid** when several labels may be true at the same time.

```text
Work-related: 0.95
Urgent:       0.88
Personal:     0.04
```

An email may be both work-related and urgent, so those labels should not be forced to compete.

```text
One mutually exclusive answer → softmax
Multiple overlapping answers  → sigmoid
```

## Core Mental Model

```text
ReLU       → block negatives, preserve positive strength
Leaky ReLU → keep a small learning path for negative inputs
Sigmoid    → compress one independent score between 0 and 1
Softmax    → make several classes compete for one prediction
```

## Current Understanding

- A value of zero still moves forward but contributes nothing to the next calculation.
- ReLU can train efficiently but may create dead neurons.
- Leaky ReLU keeps a nonzero gradient on the negative side.
- Sigmoid can suffer from vanishing gradients at extreme inputs.
- Softmax is for one winner; sigmoid is for overlapping labels.

## Next Lesson

**Lesson 007: Hidden Layers and Feature Composition**

The next step is to see how multiple neurons in one layer detect different patterns and how later layers combine those signals into more complex representations.
