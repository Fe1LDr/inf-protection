n = int(input())
A = [True] * n
i = 2
while i ** 2 <= n - 1:
    if A[i]:
        j = i ** 2
        while j <= n - 1:
            A[j] = False
            j += i
    i += 1

numbers = [i for i in range(2, len(A)) if A[i]]
print(*numbers)
