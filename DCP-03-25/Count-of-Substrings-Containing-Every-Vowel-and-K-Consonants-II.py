class Solution:
    def check_vowel(self,c) :
        return c in ['a','e','i','o','u']

    def helper(self,word,k) :
        finalRes = 0
        left = 0
        right = 0
        hash_map = {}
        n = len(word)
        consonant_count = 0

        while (right < n) :

            new_one = word[right]

            if self.check_vowel(new_one) :
                hash_map[new_one] = hash_map.get(new_one,0) + 1
            else :
                consonant_count += 1
            
            # shrink the window in case of valis substring
            while len(hash_map) == 5 and consonant_count >= k:

                finalRes += n - right
                start_letter = word[left]
                if self.check_vowel(start_letter) :
                    hash_map[start_letter] = hash_map.get(start_letter) - 1
                    if hash_map.get(start_letter) == 0 :
                        hash_map.pop(start_letter) 
                else :
                    consonant_count -= 1
                left = left + 1
            right = right + 1
        return finalRes
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.helper(word,k) - self.helper(word,k+1)
        
        