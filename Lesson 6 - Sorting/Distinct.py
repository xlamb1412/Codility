def solution(A):
    distinct_set = []
    for i in range(len(A)):
        if A[i] not in distinct_set:
            distinct_set.append(A[i])

    return len(distinct_set)

def solution(A):
    if len(A) == 0:
        distinct = 0
    else:
        distinct = 1
        A.sort()
        for i in list(range(1, len(A))):
            if A[i] == A[i-1]:
                continue
            else:
                distinct += 1

    return distinct

test = [2, 1, 1, 2, 3, 1]
solution(test)