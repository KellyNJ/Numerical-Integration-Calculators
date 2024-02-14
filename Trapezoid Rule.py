def trapezoidal_rule(f, a, b, n):
    """
    Approximates the integral of f(x) from a to b using the trapezoidal rule.

    :param f: The function to integrate.
    :param a: The lower limit of integration.
    :param b: The upper limit of integration.
    :param n: The number of subintervals to use.
    :return: The approximate value of the integral.
    """
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))  # Add the endpoints
    for i in range(1, n):
        result += f(a + i * h)  # Add the midpoint of each subinterval
    result *= h
    return result

# Use this section of the code to insert your inputs
def f(x):
    return 1/(x*x)  # Define the function to integrate

a = 1  # Lower limit
b = 2  # Upper limit
n = 8  # Number of subintervals

approx_integral = trapezoidal_rule(f, a, b, n)
print("Approximate integral:", approx_integral)