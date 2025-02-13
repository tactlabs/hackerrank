def is_palindrome(s):
    return s == s[::-1]

def palindrome_index(s):
    l = len(s)
    for i in range(l // 2):
        print('l // 2: ', l // 2)
        if s[i] != s[l - 1 - i]:
            if is_palindrome(s[i+1:l-i]):
                return i
            elif is_palindrome(s[i:l-1-i]):
                return l - 1 - i
            break
    return -1

def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        print(palindrome_index(s))

if __name__ == "__main__":
    main()
