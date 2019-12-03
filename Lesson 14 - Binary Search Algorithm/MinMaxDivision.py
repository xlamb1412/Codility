def blocksNo(A, maxBlock):

    blocksNumber = 1
    preBlockSum = A[0]
    for ele in A[1:]:
        if preBlockSum + ele > maxBlock:
            preBlockSum = ele
            blocksNumber += 1
        else:
            preBlockSum += ele
    return blocksNumber

def solution(K, A):

    blocksNeeded = 0

    resultLowerBoud = max(A)
    resultUpperBoud = sum(A)
    result = 0

    if K == 1:      return resultUpperBoud
    if K >= len(A): return resultLowerBoud

    while resultLowerBoud <= resultUpperBoud:
        resultMaxMid = (resultLowerBoud + resultUpperBoud)/2
        blocksNeeded = blocksNo(A, resultMaxMid)
        if blocksNeeded <= K:
            resultUpperBoud = resultMaxMid - 1
            result = resultMaxMid
        else:
            resultLowerBoud = resultMaxMid + 1

    return result