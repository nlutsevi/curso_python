def factorial(num=10):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1

num = 10
print("El factorial de " + str(num) + " es " + str(factorial()))