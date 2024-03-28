# Group:
# Sapir Natanov 322378068
# Dor Maudi 207055138
# Noa Yasharzadeh 208595157
# Segev Isaac 207938085
def f(x):
    return x ** 3 - 2 * x - 5


def df(x):
    return 3 * x ** 2 - 2


def false_position(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("The method may not converge.")
        return None, 0
    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(b - a) < tol:
            return c, i + 1
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    print("The method did not converge.")
    return None, max_iter


def newton_raphson(x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_next = x - f(x) / df(x)
        if abs(x_next - x) < tol:
            return x_next, i + 1
        x = x_next
    return None, max_iter


def good_example():
    # Example of using Newton-Raphson method
    root, iterations = newton_raphson(2, 1e-6, 100)
    if root is not None:
        print("Root found at:", root)
        print("Iterations:", iterations)
    else:
        print("Root not found within maximum iterations.")


def bad_example():
    # Example where false position method may not converge
    root, iterations = false_position(1, 3, 1e-6, 100)
    if root is not None:
        print("Root found at:", root)
        print("Iterations:", iterations)
    else:
        print("Root not found within maximum iterations.")


if __name__ == '__main__':
    print("Running good example:")
    good_example()

    print("\nRunning bad example:")
    bad_example()
