def is_palindrome(num):
    def helper(i, j):
        if i >= j:
            return True

        if num[i] != num[j]:
            return False

        return helper(i + 1, j - 1)

    return helper(0, len(num) - 1)
