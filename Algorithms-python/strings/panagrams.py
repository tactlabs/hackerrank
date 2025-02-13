def is_pangram(s):
    s = s.lower()
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return "pangram" if set(s) >= alphabet else "not pangram"

def main():
    s = input().strip()
    print(is_pangram(s))

if __name__ == "__main__":
    main()
