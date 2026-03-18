def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    def f(x):
        return (a * x**2) + (b * x) + c

    def grad(x):
        return (2 * a * x0) + b

    for _ in range(steps):
        x0 = x0 - (lr * grad(x0))
        
    return x0
        
        