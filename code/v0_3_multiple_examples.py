# v0_3_multiple_examples.py
#
# Learning from multiple examples
# Building gradient descent manually


# Training data
# The model is trying to discover:
# y = 2x + 1

inputs = [1, 2, 3, 4, 5]
targets = [3, 5, 7, 9, 11]


# Starting parameters
# The model does not know the correct values yet

weight = 0.5
bias = 0.0


# Controls how large each adjustment is

learning_rate = 0.001


# Number of times the model sees the entire dataset

epochs = 100


for epoch in range(epochs):

    total_loss = 0

    weight_gradient = 0
    bias_gradient = 0


    # Go through every training example

    for input_value, target in zip(inputs, targets):

        # Make prediction
        prediction = input_value * weight + bias


        # Calculate error
        error = prediction - target


        # Calculate loss
        loss = error ** 2

        total_loss += loss


        # Calculate gradients
        weight_gradient += error * input_value
        bias_gradient += error


    # Average the loss and gradients

    average_loss = total_loss / len(inputs)

    weight_gradient = weight_gradient / len(inputs)
    bias_gradient = bias_gradient / len(inputs)


    # Update parameters

    weight = weight - learning_rate * weight_gradient
    bias = bias - learning_rate * bias_gradient


    if epoch % 10 == 0:
        print(
            f"Epoch {epoch} | "
            f"Loss: {average_loss:.4f} | "
            f"Weight: {weight:.4f} | "
            f"Bias: {bias:.4f}"
        )


print("\nTraining Complete!")

print(f"Final Weight: {weight:.4f}")
print(f"Final Bias: {bias:.4f}")


# Test the model

print("\nTesting:")

test_inputs = [6, 7, 10]

for value in test_inputs:

    prediction = value * weight + bias

    print(
        f"Input: {value} -> Prediction: {prediction:.2f}"
    )
