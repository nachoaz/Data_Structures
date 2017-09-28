# count_number_of_moves_to_climb_stairs.py


def get_number_of_ways_to_climb_stairs(n, k):
    def get_ways_to_get_to_step(s, k):
        if s in {0, 1}:
            W[s] = 1
            return W[s]

        if W[s] is None:
            W[s] = sum([get_ways_to_get_to_step(s-i, k) for i in range(1, k+1)])

        return W[s]

    W = [None]*(n+1)
    return get_ways_to_get_to_step(n, k)
