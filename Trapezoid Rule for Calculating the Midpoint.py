def midpoint_rule(f, a, b, n):
    """
    Approximates the integral of f(x) from a to b using the midpoint rule.

    :param f: The function to integrate.
    :param a: The lower limit of integration.
    :param b: The upper limit of integration.
    :param n: The number of subintervals to use.
    :return: The approximate value of the integral.
    """
    h = (b - a) / n
    result = 0
    for i in range(n):
        mid = a + (i + 0.5) * h  # Calculate the midpoint of each subinterval
        result += f(mid)
    result *= h
    return result

# Enter information regarding your problem here:
def f(x):
    return 1/(x*x)   # Define the function to integrate

a = 1  # Lower limit
b = 2  # Upper limit
n = 8  # Number of subintervals

approx_integral = midpoint_rule(f, a, b, n)
print("Approximate integral:", approx_integral)