import math

print("🟰Quadratic Equation Intercept Finder🟰")
def quadratic_equation_intercept_finder(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return "No intercepts exist"

    else:
        intercept_1 = (-b + discriminant ** 0.5) / (2 * a)
        intercept_2 = (-b - discriminant ** 0.5) / (2 * a)

        return (intercept_1, intercept_2)


print(quadratic_equation_intercept_finder(2, -2, 22))
print(quadratic_equation_intercept_finder(1, -3, 2))

