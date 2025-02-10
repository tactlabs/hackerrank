def max_xor(l, r):
    max_val = 0
    for a in range(l, r + 1):
        for b in range(a, r + 1):
            max_val = max(max_val, a ^ b)  # Update max XOR value
    return max_val

# Read input values
l = int(input().strip())
r = int(input().strip())

# Compute and print the maximum XOR value
print(max_xor(l, r))
