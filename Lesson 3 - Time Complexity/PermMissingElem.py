def solution(A):

    sumA = sum(A)
    lenA = len(A) + 1
    cum_sum = 0
    for i in range(lenA):
        cum_sum += i

    return (cum_sum - sumA)