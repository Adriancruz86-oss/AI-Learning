def run_gradient_descent(start_x, learning_rate, steps):
    x = start_x

    print(f"\nLearning rate: {learning_rate}")
    print(f"Start: x={x:.4f}, loss={x**2:.4f}")

    for step in range(1, steps + 1):
        gradient = 2 * x
        x = x - learning_rate * gradient
        loss = x ** 2

        print(f"Step {step:2d}: x={x:9.4f}, loss={loss:12.4f}")


start_x = 10
steps = 10

run_gradient_descent(start_x, 0.05, steps)
run_gradient_descent(start_x, 0.25, steps)
run_gradient_descent(start_x, 1.10, steps)
