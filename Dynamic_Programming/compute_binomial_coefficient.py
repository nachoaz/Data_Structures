# compute_binomial_coefficient.py


def n_choose_k(n, k):
    """Uses O(nk) time and O(nk) space."""
    C = [[0]+[1]*n for _ in range(k+1)]  # include 0s for easy indexing
    C[0][0] = 1

    for i in range(1, k+1):
        for j in range(1, n+1):
            C[i][j] = C[i][j-1] + C[i-1][j-1]

    return C[k][n]


def n_choose_k_memory_efficient(n, k):
    """Uses O(nk) time and O(k) space."""
    C = [0 if i != 0 else 1 for i in range(k+1)]
 
    for j in range(1, n + 1):
        i = min(j, k)
        while (i > 0):
            C[i] += C[i-1]
            i -= 1
 
    return C[k]
