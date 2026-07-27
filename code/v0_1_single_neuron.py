# v0.1 - Single Neuron Learning From Scratch

# Training example
input_value = 5
target = 20

# Starting guesses
weight = 0.5
bias = 0

# Make a prediction
prediction = (input_value * weight) + bias

print("Prediction:", prediction)# v0.1 - Single Neuron Learning From Scratch

input_value = 5
target = 20

weight = 0.5
bias = 0

learning_rate = 0.01

for epoch in range(100):

    # Forward pass
    prediction = (input_value * weight) + bias

    # Calculate error
    error = target - prediction

    # Calculate loss
    loss = error ** 2

    # Update weight
    weight = weight + (error * learning_rate)

    print(
        "Epoch:", epoch,
        "Prediction:", prediction,
        "Loss:", loss,
        "Weight:", weight
    )
