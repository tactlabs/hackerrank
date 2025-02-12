from sys import stdin



def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


def count_anagram_pairs(s):
    count = 0
    n = len(s)
    
    for i in range(1, n):  # Length of substrings
        substrings = {}
        
        for j in range(n - i + 1):
            sub = "".join(sorted(s[j:j + i]))  # Sort characters for easier comparison
            
            if sub in substrings:
                count += substrings[sub]
                substrings[sub] += 1
            else:
                substrings[sub] = 1

    return count


if __name__ == "__main__":
    t = int(stdin.readline().strip())
    # print(count_anagram_pairs(s))
    
    for _ in range(t):
        s = stdin.readline().strip()
        print(count_anagram_pairs(s))