def solution(A):
    re = 0
    for num in A:
        re ^= num
        print(re)

    return re

solution([3,2,3,2,5])

x = 5
x ^= 3
print(x)
