import math

def sum_vs_xor(n):
   
    count = 0
    while n != 0:
        if n % 2 == 0:
            count += 1
        n //= 2
    print(int(math.pow(2, count)))
    


def startpy():
    
    n = int(input())
    
    sum_vs_xor(n)


if __name__ == "__main__":
    startpy()