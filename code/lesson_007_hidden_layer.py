"""Lesson 007: build a small hidden layer with NumPy.

Run from the repository root with:
    python code/lesson_007_hidden_layer.py
"""

import numpy as np


def relu(values: np.ndarray) -> np.ndarray:
    """Return ReLU activation values."""
    return np.maximum(0.0, values)


def main() -> None:
    # One example with three input features.
    inputs = np.array([2.0, -1.0, 3.0])

    # Four hidden neurons. Each neuron needs one weight per input feature.
    hidden_weights = np.array(
        [
            [0.8, -0.5, 0.3],
            [-0.2, 0.9, 0.5],
            [0.4, 0.1, -0.7],
            [-0.6, -0.3, 0.8],
        ]
    )
    hidden_biases = np.array([0.2, -0.1, 0.5, 0.0])

    # Matrix-vector multiplication calculates all four neurons at once.
    hidden_raw_outputs = hidden_weights @ inputs + hidden_biases
    hidden_outputs = relu(hidden_raw_outputs)

    # One output neuron receives the four hidden-layer feature signals.
    output_weights = np.array([0.6, -0.4, 0.7, 0.3])
    output_bias = -0.2
    final_raw_output = output_weights @ hidden_outputs + output_bias

    print("Input shape:", inputs.shape)
    print("Hidden weight shape:", hidden_weights.shape)
    print("Inputs:", inputs)
    print("Hidden raw outputs:", hidden_raw_outputs)
    print("Hidden outputs after ReLU:", hidden_outputs)
    print("Final raw output:", round(float(final_raw_output), 2))

    # Guardrails make the example fail loudly if its dimensions or arithmetic change.
    assert hidden_weights.shape == (4, 3)
    assert hidden_outputs.shape == (4,)
    assert np.allclose(hidden_raw_outputs, [3.2, 0.1, -0.9, 1.5])
    assert np.allclose(hidden_outputs, [3.2, 0.1, 0.0, 1.5])
    assert np.isclose(final_raw_output, 2.13)


if __name__ == "__main__":
    main()
