import sys

def xor(a, b):
    return 0 if a == b else 1

def main():
    n, k = map(int, sys.stdin.readline().split())
    c = int(sys.stdin.read(1))
    str_arr = [0] * n
    str_arr[0] = c
    cur = c
    xor_val = cur
    
    for i in range(1, n):
        num = int(sys.stdin.read(1))
        if i < k:
            cur = xor(xor_val, num)
        else:
            xor_val = xor(xor_val, str_arr[i - k])
            cur = xor(xor_val, num)
        xor_val = num
        str_arr[i] = cur
    
    print("".join(map(str, str_arr)))

if __name__ == "__main__":
    main()