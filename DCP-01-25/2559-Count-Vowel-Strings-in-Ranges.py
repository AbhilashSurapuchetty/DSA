class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        l = []

        v1 = len(queries)
        v2 = len(words)
        new = [0] * v2
        
        # Precompute prefix sums
        for i in range(v2):
            x = words[i]
            if (x[0] in "aeiou") and (x[-1] in "aeiou"):
                new[i] = new[i - 1] + 1 if i > 0 else 1
            else:
                new[i] = new[i - 1] if i > 0 else 0
        
        print(new)  # Debugging output for prefix sums
        
        # Process queries
        for q1, q2 in queries:
            if q1 == 0:
                l.append(new[q2])
            else:
                l.append(new[q2] - new[q1 - 1])
        
        return l
