def solution(A, K):
    len_a = len(A)
    k = K % len_a
    if k == 0:
        return A
    else:
        A = A[-k:] + A[:(len_a - k)]
        return A

A = [3, 8, 9, 7, 6]
K = 3
solution(A, K)