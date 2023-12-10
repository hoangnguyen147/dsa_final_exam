def longest_substring(s1, s2):
    n1, n2 = len(s1), len(s2)

    dp = [[0] * (n2+1) for _ in range(n1+1)]

    max_length = 0

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

                if dp[i][j] > max_length:
                    max_length = dp[i][j]
            else:
                dp[i][j] = 0

    return max_length


print(longest_substring("www.google.com/explore", "google.com/edpresso"))
