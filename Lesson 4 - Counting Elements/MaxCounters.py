def solution(N, A):
    result = [0]*N
    max_counter = 0
    current_max = 0
    for value in A:
        if 1 <= value <= N:

            if max_counter > result[value -1]:
                result[value-1] = max_counter
            max_counter += 1
            if
            result = [max(result)]*N
        else:
            result[value-1] +=1

    return result

solution(5, [3, 4, 4, 6, 1, 4, 4])