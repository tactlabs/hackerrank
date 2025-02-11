def camelcase(s):
    c = 1  # At least one word is always present
    for char in s:
        if 'A' <= char <= 'Z':  # Checking for uppercase letters
            c += 1
    return c

# Taking input
s = input("Enter the camelCase string: ")
print("Number of words:", camelcase(s))
