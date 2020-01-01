def solution(A):
    result = 0
    w_car = 0

    for i in range(len(A)-1, -1, -1):
        if A[i] == 0:
            result += w_car
            if result > 1000000000:
                return -1
        else:
            w_car += 1

    return result

A = [0,1,0,1,1]
solution(A)