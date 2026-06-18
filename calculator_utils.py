import math

ALLOWED_NAMES = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
ALLOWED_NAMES.update({
    "abs": abs,
    "pow": pow,
    "max": max,
    "min": min,
})


def safe_eval(expression, x):
    variables = {"x": x, **ALLOWED_NAMES}
    return eval(expression, {"__builtins__": None}, variables)


def integrate(expression, lower, upper, steps=1000):
    if lower == upper:
        return 0.0
    if lower > upper:
        return -integrate(expression, upper, lower, steps)

    def f(x):
        return safe_eval(expression, x)

    h = (upper - lower) / steps
    total = f(lower) + f(upper)
    for i in range(1, steps):
        x = lower + i * h
        total += 4 * f(x) if i % 2 else 2 * f(x)
    return total * h / 3
