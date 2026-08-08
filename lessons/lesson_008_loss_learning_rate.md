# Lesson 008 — Loss, Gradient Descent, and Learning Rate

## Core Idea

A neural network needs a numerical way to measure how wrong a prediction is.

That measurement is called **loss**.

Training repeatedly tries to reduce loss by changing the model's weights.

The basic loop is:

prediction
→ loss
→ gradient
→ weight update
→ new prediction
→ repeat

## Loss

Loss measures the size of the model's error.

A model that is confidently wrong should generally receive a larger loss than a model that is only slightly wrong.

Example:

- Correct class: cat
- Prediction A: 90% dog, 10% cat
- Prediction B: 55% dog, 45% cat

Prediction A should receive the larger loss because it is much more confidently wrong.

## Gradient Descent

Gradient descent is an optimization process used to reduce loss.

The gradient tells us the direction in which the loss changes most rapidly.

Training moves in the opposite direction of the gradient so that loss decreases.

For the experiment, the loss function was:

    loss = x^2

The minimum occurs at:

    x = 0

The derivative is:

    gradient = 2x

The update rule is:

    x_new = x - learning_rate * gradient

## Learning Rate

The learning rate controls the size of each update.

If the learning rate is too small:

- Training moves toward the minimum
- Progress can be very slow

If the learning rate is reasonable:

- Training converges efficiently
- Loss decreases quickly and smoothly

If the learning rate is too large:

- Updates overshoot the minimum
- Training can oscillate
- Loss can increase instead of decrease
- The process can diverge

## Python Experiment

Files:

- experiments/gradient_descent_learning_rate.py
- experiments/gradient_descent_plot.py
- experiments/gradient_descent_plot_good_rates.py

The experiment began at:

    x = 10

with:

    loss = 100

Three learning rates were tested:

### Learning rate 0.05

Observed behavior:

- Loss decreased
- Convergence was slow
- The model moved in the correct direction but took small steps

### Learning rate 0.25

Observed behavior:

- Loss decreased quickly
- Convergence was stable
- This was the healthiest of the tested learning rates

### Learning rate 1.10

Observed behavior:

- The model repeatedly overshot the minimum
- The sign of x flipped back and forth
- The magnitude of x increased
- Loss grew rapidly
- Training diverged

For this experiment:

    x_new = x - 1.10(2x)

which simplifies to:

    x_new = -1.2x

This means every update flips x to the opposite side of zero while increasing its distance from zero by 20%.

Example:

    10
    -12
    14.4
    -17.28
    20.736

Because loss is x^2, the growing distance from zero causes loss to increase rapidly.

## Plotting Observation

When all three learning rates were plotted together, the diverging 1.10 run pushed the graph's y-axis extremely high.

That compressed the successful 0.05 and 0.25 curves near the bottom and made them appear almost flat.

After plotting only the two successful learning rates, their difference became obvious:

- 0.05 decreased slowly
- 0.25 decreased much faster

This demonstrates that visualization scale can affect how training behavior appears.

## Takeaway

The gradient can point in the correct direction while training still fails if the learning rate is inappropriate.

A useful mental model is:

- Gradient = which direction to move
- Learning rate = how large a step to take
- Loss = how wrong the model currently is

Successful training requires both a useful gradient and appropriately sized updates.
