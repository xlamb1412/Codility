def solution(N):
    crr_gap = 0
    max_gap = 0
    n_bin = bin(N)[2:]

    for i in range(len(n_bin)):
        if n_bin[i] == '0':
            crr_gap += 1
        if n_bin[i] == '1':
            if max_gap < crr_gap:
                max_gap = crr_gap

            crr_gap = 0

    return max_gap

solution(1)
