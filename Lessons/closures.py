def autor(a):
    def inner(num1, num2):
        if num1 > num2:
            return (num1 - num2) ** a
        elif num1 < num2:
            return (num2 - num1) ** a
        else:
            return f"{num1} = {num2}"

    return inner


t = autor(10)
print(t(2, 4))
