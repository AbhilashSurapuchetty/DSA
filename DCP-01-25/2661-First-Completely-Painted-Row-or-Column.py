class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        hash_map = {} # hash_map to store the positions of each value in form of (i,j)
        m = len(mat)
        n = len(mat[0])
        x = len(arr)

        for i in range(0,m) :
            for j in range(0,n) :
                hash_map[mat[i][j]] = (i,j)  # here we store positions of all values in our hash map

        row_freq = {} # This hash_map stores the count of each row appearance in array arr
        col_freq = {} # Same as above it stores column

        # Stopping condition if any element in row_freq equals no of columns total or viceversa we can return 
        for i in range(0,x) :
            v = hash_map[arr[i]]
            if v[0] in row_freq :
                row_freq[v[0]] += 1
            else :
                row_freq[v[0]] = 1
            if v[1] in col_freq :
                col_freq[v[1]] += 1
            else :
                col_freq[v[1]] = 1
            
            if row_freq[v[0]] == n :
                return i
            if col_freq[v[1]] == m :
                return i
            
        

        