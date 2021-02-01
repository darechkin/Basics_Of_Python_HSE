a = int(input())
n = map(int, (input().split()))
x = int(input())
print(min(n, key=lambda b: abs(b-x)))
