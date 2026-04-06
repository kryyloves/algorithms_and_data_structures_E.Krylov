def smallest_k_element(n, mtx, k):
    left = mtx[0][0]
    right = mtx[n-1][n-1]
    
    while left < right:
        mid = (left + right) // 2
        count = 0
        j = n - 1
        
        for i in range(n):
            while j >= 0 and mtx[i][j] > mid:
                j -= 1
            count += j + 1
        
        if count < k:
            left = mid + 1
        else:
            right = mid
    
    return left

'''  
пример:
входные данные:
n = 3 
1 5 9
10 11 13
12 13 15
k = 8
выходные данные:
13
''' 
assert smallest_k_element(3, [[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13