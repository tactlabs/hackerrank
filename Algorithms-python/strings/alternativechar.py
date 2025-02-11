def alternating_characters():
    # Read the number of test cases
    t = int(input())
    
    # Loop through each test case
    for _ in range(t):
        s = input().strip()  # Read and clean input string
        delete = 0  # Initialize deletion count
        
        # Loop through the string starting from the second character
        for i in range(1, len(s)):
            # print(f"s[{i}] = {s[i]}, s[{i-1}] = {s[i-1]}")
            if s[i] == s[i - 1]:  # Check if current character is same as previous
                delete += 1  # Increment deletion count
        
        # Print the number of deletions required
        print(delete)

if __name__ == "__main__":
    alternating_characters()