def solution(A):
    roll = {}
    largest = 0
    for ele in A:
        if ele > 0:
            roll[ele] = True
            if ele > largest:
                largest = ele

    counter = 1
    while counter <= largest:
        if counter in roll:
            counter += 1
        else:
            break

    return counter

A = [1, 3, 6, 4, 1, 2]
solution(A)
roll = {}
roll[1] = True