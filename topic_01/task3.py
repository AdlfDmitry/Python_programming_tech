def find_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
D = find_discriminant(a, b, c)
print(f"Discriminant: {D}")