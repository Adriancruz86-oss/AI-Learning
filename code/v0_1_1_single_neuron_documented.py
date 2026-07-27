# v0.1 - Single Neuron Learning From Scratch
# Goal: Teach a simple neuron to learn the pattern y = 2x


# Training data
# Inputs are the examples we show the neuron
# Targets are the correct answers we want it to learn
inputs = [1, 2, 3, 4, 5]
targets = [2, 4, 6, 8, 10]


# Starting guesses
# The neuron does not know the answer yet, so we give it random starting values
weight = 0.5
bias = 0.0


# Controls how large each correction is during learning
learning_rate = 0.01


# Training loop
# An epoch is one complete pass through all training examples
for epoch in range(100):

    total_loss = 0


    # Go through each input and its matching target answer
    for input_value, target in zip(inputs, targets):


        # Forward pass:
        # The neuron makes a prediction using:
        # prediction = input × weight + bias
        prediction = (input_value * weight) + bias


        # Calculate how wrong the prediction was
        # Positive error means prediction was too low
        # Negative error means prediction was too high
        error = target - prediction


        # Loss measures how far away the prediction was
        # Squaring removes negative values and emphasizes larger mistakes
        loss = error ** 2


        # Add this example's mistake to the total training loss
        total_loss += loss


        # Update the weight based on the error
        # The neuron adjusts itself slightly toward a better answer
        weight = weight + (error * learning_rate)


    # Display progress every 10 epochs
    if epoch % 10 == 0:
        print(
            f"Epoch {epoch:3} | Loss: {total_loss:.4f} | Weight: {weight:.4f}"
        )


# After training, test if the neuron learned the pattern
print("\nTraining Complete!")
print(f"Final Weight: {weight:.4f}")
print(f"Final Bias: {bias:.4f}")


# Test with numbers the neuron has never seen before
# This checks if it learned the pattern instead of memorizing examples
test_inputs = [6, 7, 10, 100]


for value in test_inputs:

    # Make a prediction using the learned weight
    prediction = (value * weight) + bias

    print(f"Input: {value:3} -> Prediction: {prediction:.2f}")
