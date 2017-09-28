# pick_up_coins_for_max_gain.py


def get_max_gain_starting_player(coins):
    def rev(a, b):
        if a > b:
            return 0

        if max_gain_for_range[a][b] == 0:
            gain_l = coins[a] + min(rev(a+2, b), rev(a+1, b-1))
            gain_r = coins[b] + min(rev(a+1, b-1), rev(a, b-2))
            max_gain_for_range[a][b] = max(gain_l, gain_r)

        return max_gain_for_range[a][b]

    max_gain_for_range = [[0]*len(coins) for _ in coins]
    return rev(0, len(coins)-1)
