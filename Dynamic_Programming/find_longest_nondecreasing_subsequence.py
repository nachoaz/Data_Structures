# find_longest_nondecreasing_subsequence.py


def get_len_of_longest_nondecreasing_subseq(A):
    def get_L_i(i):
        candidate_js = [j for j in range(i) if A[j] <= A[i]]
        if not candidate_js:
            return 1
        
        if L[i] is None:
            L[i] = 1 + max([get_L_i(j) for j in candidate_js])

        return L[i]

    L = [None]*len(A)
    return get_L_i(len(A)-1)
