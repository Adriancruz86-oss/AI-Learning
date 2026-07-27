# v0_4_gradient_descent.py
#
# Understanding gradient descent manually
# The model learns by reducing error


# Training data
# The model is trying to learn:
# y = 2x + 1

inputs = [1, 2, 3, 4, 5]
targets = [3, 5, 7, 9, 11]


# Initial guesses
# The model starts with incorrect values

weight = 0.5
bias = 0.0


# Controls how big each correction is

learning_rate = 0.01


# Number of training rounds

epochs = 100


for epoch in range(epochs):

    total_loss = 0

    weight_gradient = 0
    bias_gradient = 0


    for input_value, target in zip(inputs, targets):

        # Forward pass
        # The model makes a prediction

        prediction = input_value * weight + bias


        # Calculate how wrong the prediction was

        error = prediction - target


        # Squared error
        # Removes negative values and increases penalty for large mistakes

        loss = error ** 2


        total_loss += loss


        # Calculate how much each parameter contributed to error

        weight_gradient += error * input_value

        bias_gradient += error


    # Average across all examples

    weight_gradient = weight_gradient / len(inputs)

    bias_gradient = bias_gradient / len(inputs)


    average_loss = total_loss / len(inputs)


    # Gradient descent update

    weight = weight - learning_rate * weight_gradient

    bias = bias - learning_rate * bias_gradient


    if epoch % 10 == 0:

        print(
            f"Epoch: {epoch} "
            f"Loss: {average_loss:.4f} "
            f"Weight: {weight:.4f} "
            f"Bias: {bias:.4f}"
        )


print("\nTraining Complete!")

print("Final Weight:", weight)

print("Final Bias:", bias)
