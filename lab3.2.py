arr = [int(i) for i in input().split()]
M = int(input())
K = int(input())
P = int(input())

if M >= 0:
    arr[K:M + K], arr[P:M + P] = arr[P:M + P], arr[K:M + K]
print(arr)
