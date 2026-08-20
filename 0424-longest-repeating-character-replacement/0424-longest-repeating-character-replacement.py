class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
         count ={}
         max_frequency = 0
         i = 0
         max_length = 0
         for j in range(len(s)):
            count[s[j]] = count.get(s[j],0) + 1
            max_frequency = max(max_frequency , count[s[j]])
            window_length = j - i+ 1
            if window_length - max_frequency > k:
                count[s[i]] -= 1
                i += 1

            max_length = max(max_length, j - i + 1)

         return max_length