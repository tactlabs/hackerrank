# def is_pangram(s):
#     s = s.lower()
#     alphabet = set("abcdefghijklmnopqrstuvwxyz")
#     return "pangram" if set(s) >= alphabet else "not pangram"

# def main():
#     s = input().strip()
#     print(is_pangram(s))

# if __name__ == "__main__":
#     main()

import os

def sockMerchant(n, ar):
    # Write your code here    
    sock_count = {}
    count = 0
    
    for sock in ar:
        if sock in sock_count:
            sock_count[sock] += 1
        else:
            sock_count[sock] = 1
            
    for sock_value in sock_count.values():
        print('sock_value: ', sock_value)
        count += sock_value // 2
        
    return count
         

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()