# v0_5_multiple_inputs.py
#
# Learning with multiple inputs
# Batch gradient descent
#
# The neuron is learning:
# prediction = input1 * weight1 + input2 * weight2 + bias


# Training data
#
# [hours studied, hours slept], target score

training_data = [
    ([1, 8], 5),
    ([2, 7], 8),
    ([3, 6], 11),
    ([4, 8], 14),
    ([5, 7], 17),
]


# Starting parameters

weight_hours = 0.5
weight_sleep = 0.5

bias = 0.0


# Learning controls

learning_rate = 0.001
epochs = 100


# Training loop

for epoch in range(epochs):

    total_loss = 0

    # Reset gradient storage every epoch

    weight_hours_gradient_total = 0
    weight_sleep_gradient_total = 0
    bias_gradient_total = 0


    # Go through every example

    for inputs, target in training_data:

        hours = inputs[0]
        sleep = inputs[1]


        # Make prediction

        prediction = (
            hours * weight_hours
            + sleep * weight_sleep
            + bias
        )


        # Calculate error

        error = prediction - target


        # Calculate loss

        loss = error ** 2

        total_loss += loss


        # Calculate gradients

        weight_hours_gradient = error * hours

        weight_sleep_gradient = error * sleep

        bias_gradient = error


        # Add gradients together

        weight_hours_gradient_total += weight_hours_gradient

        weight_sleep_gradient_total += weight_sleep_gradient

        bias_gradient_total += bias_gradient


    # Average gradients

    weight_hours_gradient_average = (
        weight_hours_gradient_total / len(training_data)
    )

    weight_sleep_gradient_average = (
        weight_sleep_gradient_total / len(training_data)
    )

    bias_gradient_average = (
        bias_gradient_total / len(training_data)
    )


    # Update parameters once per epoch

    weight_hours -= learning_rate * weight_hours_gradient_average

    weight_sleep -= learning_rate * weight_sleep_gradient_average

    bias -= learning_rate * bias_gradient_average


    # Show progress

    if epoch % 10 == 0:

        average_loss = total_loss / len(training_data)

        print(
            "Epoch:",
            epoch,
            "Loss:",
            average_loss,
            "Weight Hours:",
            weight_hours,
            "Weight Sleep:",
            weight_sleep,
            "Bias:",
            bias
        )


print("\nTraining Complete!")

print("Final Weight Hours:", weight_hours)

print("Final Weight Sleep:", weight_sleep)

print("Final Bias:", bias)
