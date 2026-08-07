# AI-Learning

## Purpose

This repository documents my hands-on path into artificial intelligence and machine learning.

It contains the code, experiments, and written lessons I create while learning how models work from the ground up.

The focus is not on copying frameworks without understanding them. The goal is to build each idea manually first, then use larger tools such as PyTorch with a clear mental model of what they are doing.

## Current Learning Sequence

- A single artificial neuron
- Inputs, weights, and bias
- Predictions and error
- Loss functions
- Multiple training examples
- Gradient descent
- Multiple inputs
- Activation functions
- Hidden layers and feature composition

The structured written lessons currently end with hidden layers, matrix shapes, forward passes, network width and depth, and how several neurons create learned feature representations for later layers.

[View the AI lesson index](lessons/README.md)

## Supporting Foundations

These notes reinforce the computer systems underneath future AI code without changing the numbered AI lesson sequence.

- [CPU Instruction Flow: From Machine Code to Register Update](docs/foundations/cpu_instruction_flow.md)

## Repository Structure

```text
AI-Learning/
├── code/          Python implementations and exercises
├── experiments/   Models, tests, and exploratory work
├── lessons/       Structured AI and machine-learning lessons
├── docs/          Supporting project documentation
├── README.md
└── requirements.txt
```

## Current Technology Stack

- Python 3.12
- NumPy
- Pandas
- Matplotlib
- Jupyter
- PyTorch
- Git and GitHub
- macOS and Terminal

## Completed Foundations

- Built a single neuron from scratch
- Worked with weights and bias
- Calculated prediction error and loss
- Trained with multiple examples
- Implemented gradient descent
- Expanded from one input to multiple inputs
- Built training loops
- Learned how ReLU, Leaky ReLU, sigmoid, and softmax transform neuron outputs
- Connected sigmoid saturation to vanishing gradients and ReLU's negative side to dead neurons
- Distinguished mutually exclusive softmax classes from overlapping sigmoid labels
- Built a four-neuron hidden layer with NumPy
- Traced matrix shapes through a hidden layer and output neuron
- Connected hidden-layer outputs to learned features and feature composition
- Distinguished network width from network depth
- Explored activation functions and multilayer models in experiments
- Practiced backpropagation and autograd concepts
- Explored curiosity, reinforcement learning, sequence learning, memory, and anomaly detection
- Traced a machine-code instruction through registers, buses, decoders, the ALU, and the fetch-decode-execute cycle

## Next Structured Lessons

- A multilayer neural network from scratch
- Backpropagation
- PyTorch fundamentals
- Model evaluation and generalization

## Companion Repositories

- **Atom-to-Intelligence** documents the bottom-up path from atoms, electricity, semiconductors, transistors, and logic gates toward computers and AI.
- **CyberTrail** is a separate cybersecurity product project.

## Key Principle

The goal is not merely to make code run. The goal is to understand why it works.