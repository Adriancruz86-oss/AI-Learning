# v0.1 - Single Neuron Learning From Scratch (Multiple Training Examples)

# Training data
inputs = [1, 2, 3, 4, 5]
targets = [2, 4, 6, 8, 10]

# Initial guesses
weight = 0.5
bias = 0.0

learning_rate = 0.01

# Train the neuron
for epoch in range(100):

    total_loss = 0

    # Loop through every training example
    for input_value, target in zip(inputs, targets):

        # Forward pass
        prediction = (input_value * weight) + bias

        # Calculate error
        error = target - prediction

        # Calculate loss
        loss = error ** 2

        # Keep track of total loss for this epoch
        total_loss += loss

        # Update the weight
        weight = weight + (error * learning_rate)

    # Print progress every 10 epochs
    if epoch % 10 == 0 or epoch == 99:
        print(
            f"Epoch {epoch:3} | "
            f"Loss: {total_loss:.4f} | "
            f"Weight: {weight:.4f}"
        )

print("\nTraining Complete!")
print(f"Final Weight: {weight:.4f}")
print(f"Final Bias: {bias:.4f}")

# Test the trained neuron
print("\nTesting the model:")

test_inputs = [6, 7, 10, 100]

for value in test_inputs:
    prediction = (value * weight) + bias
    print(f"Input: {value:3} -> Prediction: {prediction:.2f}")
