import math
def find_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

def find_roots(a, b, c):
    D = find_discriminant(a, b, c)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return x1, x2
    elif D == 0:
        x = -b / (2*a)
        return x,
    else:
        return None  

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
roots = find_roots(a, b, c)

if roots:
    if len(roots) == 1:
        print(f"Solution: {roots[0]}")
    else:
        print(f"Solutions: {roots[0]} and {roots[1]}")
else:
    print("No solutions.")
