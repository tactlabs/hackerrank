def anagram_changes():
    t = int(input())  # Read the number of test cases
    for _ in range(t):  # Loop through each test case
        s = input().strip()  # Read the input string and remove extra spaces
        l = len(s)  # Get length of string
        
        if l % 2 != 0:  # If the length is odd, return -1
            print(-1)
        else:
            s1, s2 = s[:l//2], s[l//2:]  # Split into two halves
            count1, count2 = [0] * 26, [0] * 26  # Initialize frequency arrays
            
            # Count frequency of characters in first half
            for char in s1:
                count1[ord(char) - 97] += 1  # 'a' has ASCII 97
                print('count1[ord(char) - 97] += 1: ', count1)
                
            # Count frequency of characters in second half
            for char in s2:
                count2[ord(char) - 97] += 1  
            
            # Compute the total number of differences
            c = sum(abs(count1[i] - count2[i]) for i in range(26))  
            print(c // 2)  # Since each change fixes two mismatched characters

if __name__ == "__main__":
    anagram_changes()
