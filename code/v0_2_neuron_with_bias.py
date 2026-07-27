# v0.2 - Single neuron with weight, bias, and training loop

weight = 0.5
bias = 0

input_value = 5
target = 13

learning_rate = 0.01

# Training loop
for epoch in range(100):

    # Make prediction
    prediction = input_value * weight + bias

    # Calculate loss
    loss = (target - prediction) ** 2

    # Calculate gradients
    weight_gradient = -2 * input_value * (target - prediction)
    bias_gradient = -2 * (target - prediction)

    # Update weight and bias
    weight = weight - learning_rate * weight_gradient
    bias = bias - learning_rate * bias_gradient

    # Show progress every 10 epochs
    if epoch % 10 == 0:
        print(
            "Epoch:",
            epoch,
            "Prediction:",
            round(prediction, 2),
            "Loss:",
            round(loss, 2),
            "Weight:",
            round(weight, 2),
            "Bias:",
            round(bias, 2)
        )

print("\nTraining Complete!")
print("Final Weight:", round(weight, 2))
print("Final Bias:", round(bias, 2))
