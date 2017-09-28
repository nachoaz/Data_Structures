# count_score_combinations.py


def count_score_combinations(score, point_vals):
    """Given a score and a set points that are possible, returns the number of
    combinations of plays that could have led to that particular score.

    Note: These are *combinations* (not permutations), so order does not matter
    (i.e. <2, 2, 3, 2> is the same as <2, 2, 2, 3>).

    Expects points to be a list sorted in ascending order.
    """
    W = [[1 if j % point_vals[0] == 0 else 0 for j in range(score+1)]] \
      + [[0]*(score + 1) for _ in range(1, len(point_vals))]

    i = 1
    for point_val in point_vals[1:]:
        for j in range(point_val):
            W[i][j] = W[i-1][j]
        for j in range(point_val, len(W[i])):
            W[i][j] = W[i-1][j] + W[i][j-point_val]
        i += 1

    return W[-1, -1]


def count_score_combinations_memory_efficient(score, point_vals):
    """Given a score and a set points that are possible, returns the number of
    combinations of plays that could have led to that particular score.

    Note: These are *combinations* (not permutations), so order does not matter
    (i.e. <2, 2, 3, 2> is the same as <2, 2, 2, 3>).

    Expects points to be a list sorted in ascending order.
    """
    W = [1 if j % point_vals[0] == 0 else 0 for j in range(score+1)]
    
    for point_val in point_vals[1:]:
        for j in range(point_val, len(W)):
            W[j] += W[j-point_val]

    return W[score]
