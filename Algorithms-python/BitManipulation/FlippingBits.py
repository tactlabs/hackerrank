def flipping_bits():
    t = int(input())  # Read the number of test cases
    max_int = (2**32) - 1  # Maximum 32-bit unsigned integer

    for _ in range(t):
        num = int(input())  # Read input number
        print(max_int - num)  # Flip the bits and print result

# Run the function
flipping_bits()
