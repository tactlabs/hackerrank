def is_funny(s):
    l = len(s)
    for i in range(1, l):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[l - i]) - ord(s[l - i - 1])):
            return "Not Funny"
    return "Funny"

# Reading input
t = int(input())
for _ in range(t):
    s = input().strip()
    print(is_funny(s))


# input 

# 2
# acxz
# bcxz


# output


# Funny
# Not Funny

