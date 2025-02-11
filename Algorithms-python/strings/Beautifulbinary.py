def beautiful_binary_string(n, B):
    B = list(B) 
    c = 0  
    
    print(f"Original Binary String: {''.join(B)}") 
    for i in range(2, n):  # Start from the third character
        if B[i - 2] == '0' and B[i - 1] == '1' and B[i] == '0':
            print(f"Pattern '010' found at index {i-2}, {i-1}, {i}")  
            B[i] = '1'  # Modify the last '0' in "010"
            c += 1 
            print(f"Modified Binary String: {''.join(B)}") 
    
    return c

n = int(input("Enter the length of the binary string: "))
B = input("Enter the binary string: ")

print("Number of modifications:", beautiful_binary_string(n, B))
