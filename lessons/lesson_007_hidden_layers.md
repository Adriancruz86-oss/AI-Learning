# Lesson 007: Hidden Layers and Feature Composition

## From One Neuron to a Layer

A single neuron produces one output. A layer contains several neurons that receive the same input values but use different weights and biases.

```text
same inputs
   ↓
neuron 1 → feature signal 1
neuron 2 → feature signal 2
neuron 3 → feature signal 3
neuron 4 → feature signal 4
```

Because each neuron has its own parameters, each can respond to a different pattern in the input.

## A Small Hidden Layer

Suppose one example has three input features:

```text
inputs = [2, -1, 3]
```

A hidden layer contains four neurons. Its weight matrix therefore has four rows and three columns:

```text
hidden weights shape = 4 × 3
```

Each row belongs to one hidden neuron:

```text
[
  [ 0.8, -0.5,  0.3],
  [-0.2,  0.9,  0.5],
  [ 0.4,  0.1, -0.7],
  [-0.6, -0.3,  0.8]
]
```

The hidden layer calculation is:

```text
hidden raw outputs = hidden weights × inputs + hidden biases
```

For this example, the raw outputs are:

```text
[3.2, 0.1, -0.9, 1.5]
```

After ReLU:

```text
[3.2, 0.1, 0.0, 1.5]
```

The third neuron did not detect a useful positive pattern for this input, so ReLU reduced its signal to zero.

## Why It Is Called a Hidden Layer

The input layer contains the original features supplied to the model. The output layer produces the final prediction.

A layer between them is called hidden because its values are internal representations rather than values directly provided by the user or returned as the final answer.

```text
input layer → hidden layer → output layer
```

The hidden layer transforms the original inputs into a new set of learned features.

## Feature Composition

Imagine the original inputs describe a network event:

```text
failed logins
unusual location score
privilege level
```

Different hidden neurons might eventually become sensitive to combinations such as:

```text
repeated authentication failure
high-privilege access
unusual access pattern
combined account-takeover signal
```

We do not manually assign those meanings to neurons. During training, weight updates make useful detectors emerge.

A later layer can combine simple feature signals into a more complex decision. This is feature composition.

```text
simple features
      ↓
combined hidden representation
      ↓
more complex prediction
```

## The Output Layer Uses Hidden Features

The four hidden outputs become the inputs to the next neuron:

```text
hidden outputs = [3.2, 0.1, 0.0, 1.5]
output weights = [0.6, -0.4, 0.7, 0.3]
output bias = -0.2
```

The final raw output is:

```text
(3.2 × 0.6) +
(0.1 × -0.4) +
(0.0 × 0.7) +
(1.5 × 0.3) - 0.2
= 2.13
```

Notice that the output neuron does not see the original three inputs directly. It sees the transformed feature signals created by the hidden layer.

## Matrix Shape Mental Model

For one example with three input features and four hidden neurons:

```text
inputs:          3 values
hidden weights:  4 × 3
hidden biases:   4 values
hidden outputs:  4 values
```

The next output neuron needs one weight for each hidden output:

```text
output weights:  4 values
final output:    1 value
```

A reliable rule is:

```text
one neuron needs one weight per incoming value
```

## Width Versus Depth

**Width** means how many neurons are in a layer.

```text
4 hidden neurons → hidden-layer width of 4
```

**Depth** means how many trainable layers are stacked.

```text
input → hidden → output
```

The input layer is usually not counted as a trainable layer because it does not contain learned weights.

A wider network can learn more features at the same stage. A deeper network can repeatedly combine earlier features into more abstract representations.

## Forward Pass

The complete movement from inputs to prediction is called a forward pass.

```text
1. Receive input values
2. Calculate hidden raw outputs
3. Apply hidden activation functions
4. Send hidden outputs forward
5. Calculate the final output
```

No learning occurs during the forward pass by itself. It only calculates a prediction using the current weights and biases.

## Core Mental Model

```text
Neuron       → one pattern detector
Layer        → several detectors working in parallel
Hidden layer → transforms inputs into learned features
Deeper layer → combines earlier features
Forward pass → calculates a prediction with current parameters
```

## Comprehension Check

1. If an input has five features and a hidden layer has eight neurons, what shape must the hidden weight matrix have?
2. Why can two neurons receiving the same inputs produce different outputs?
3. After a hidden layer produces four values, how many incoming weights does one neuron in the next layer need?
4. Does a forward pass update the model's weights?
5. In your own words, what does feature composition mean?

## Answers

1. `8 × 5`: one row per hidden neuron and one column per incoming feature.
2. They have different weights and biases.
3. Four weights.
4. No. It only calculates outputs using the current parameters.
5. Later neurons combine simpler learned signals into more complex representations or decisions.

## Next Lesson

**Lesson 008: A Multilayer Neural Network From Scratch**

The next step is to organize these calculations into reusable layer objects and pass a batch of examples through a complete multilayer network.