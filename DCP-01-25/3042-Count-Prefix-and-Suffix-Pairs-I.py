'''class Solution:
    def isPrefixAndSuffix(self, str1, str2):
        # Handles both prefix and suffix checks
        if not str1 or not str2:
            return False
        if str1 == str2:
            return True
        return str2.startswith(str1) and str2.endswith(str1)
    
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        v = len(words)
        for i in range(v - 1):
            for j in range(i + 1, v):
                result = self.isPrefixAndSuffix(words[i], words[j])
                print(result)  # Debugging statement
                if result:
                    count += 1
        return count'''
class Solution:
    def countPrefixSuffixPairs(self, words: List[str], ans = 0) -> int:

        for pre_suf, word in combinations(words,2):
            ans+= word.startswith(pre_suf) and word.endswith(pre_suf)

        return  ans
