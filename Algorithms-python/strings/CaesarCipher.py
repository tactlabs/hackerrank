def caesar_cipher():
    size = int(input().strip())  # Read size (not needed in Python, but kept for consistency)
    s = input().strip()  # Read the string
    num = int(input().strip())  # Read shift value

    result = []  # To store the encrypted characters

    for char in s:
        if 'A' <= char <= 'Z':  # Uppercase letters
            k = ord(char) + num
            while k > ord('Z'):
                k -= 26  # Wrap around if it exceeds 'Z'
            result.append(chr(k))
        elif 'a' <= char <= 'z':  # Lowercase letters
            k = ord(char) + num
            while k > ord('z'):
                k -= 26  # Wrap around if it exceeds 'z'
            result.append(chr(k))
        else:
            result.append(char)  # Non-alphabet characters remain the same

    print("".join(result))  # Print the final encrypted text

if __name__ == "__main__":
    caesar_cipher()
