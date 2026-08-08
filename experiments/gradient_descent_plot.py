import matplotlib.pyplot as plt


def run_gradient_descent(start_x, learning_rate, steps):
    x = start_x
    losses = [x ** 2]

    for _ in range(steps):
        gradient = 2 * x
        x = x - learning_rate * gradient
        losses.append(x ** 2)

    return losses


steps = 20

slow = run_gradient_descent(10, 0.05, steps)
healthy = run_gradient_descent(10, 0.25, steps)
unstable = run_gradient_descent(10, 1.10, steps)

plt.plot(slow, label="learning rate = 0.05")
plt.plot(healthy, label="learning rate = 0.25")
plt.plot(unstable, label="learning rate = 1.10")

plt.xlabel("Training step")
plt.ylabel("Loss")
plt.title("Learning Rate vs Gradient Descent")
plt.legend()
plt.show()
