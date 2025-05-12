class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        max_len = max(len(word1), len(word2))
        result = ''

        for i in range(0, min_len):
            result += word1[i]
            result += word2[i]

        if min_len != max_len:
            result += word1[min_len:]
            result += word2[min_len:]

        return result

# Runtime 45ms / Beats 13.16%
# Memory 17.79MB / Beats 49.43%