def is_subsequence(s, t):
    # i = pointer to s, and j = pointer to t
    def helper(i, j):
        if i == len(s):
            return True
        elif j == len(t):
            return False
        elif (s[i] == t[j]):
            return helper(i + 1, j + 1)

        return helper(i, j + 1)

    return helper(0, 0)


