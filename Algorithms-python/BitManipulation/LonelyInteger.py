def lonely_integer(arr):
    count = [0] * 101  # Array to count occurrences
    for num in arr:
        count[num] += 1
    
    for i in range(101):
        if count[i] % 2 != 0:
            return i
    return 0

# Read input
n = int(input())  # Read the size of the array
arr = list(map(int, input().split()))  # Read the space-separated integers

# Find and print the lonely integer
print(lonely_integer(arr))
