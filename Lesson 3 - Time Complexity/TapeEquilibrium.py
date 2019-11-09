def solution(A):

    sum_A = sum(A)
    result = float('inf')
    left_sum = 0

    for i in A[:-1]:
        left_sum += i
        result = min(abs(sum_A - 2*left_sum), result)

    return result
