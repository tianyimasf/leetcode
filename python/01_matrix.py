"""
Pesudo-code

Scan the matrix from the top left. If element = 0, distance = 0. 
If element = 1, add the element surrounding it that hasn't been 
computed to the queue. (aka start BFS) If reaches an element that
has been computed before, simply finalize dist by adding computed
dist to curr dist. Keep a matrix for if reached, and keep a matrix
for computed dist. 

"""

def updateMatrix(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    m = len(mat)
    n = len(mat[0])
    mat_res, mat_reached = [[-1 for _ in range(n)] for _ in range(m)], [[False for _ in range(n)] for _ in range(m)]
    for i, row in enumerate(mat):
        for j, e in enumerate(row):
            if e == 0: mat_res[i][j] = 0
            elif e == 1: 
                res = BFS(mat, mat_res, mat_reached, i, j)
                mat_res[i][j] = res
    return mat_res
    
def BFS(mat, mat_res, mat_reached, i_e, j_e):
    import copy

    mat_reached_e = copy.deepcopy(mat_reached)
    queue = [[i_e, j_e]]
    dist, computed = 0, False
    while not computed:
        curr = queue.pop()
        i, j = curr[0], curr[1]
        # if reached 0, return dist
        if mat[i][j] == 0: return dist
        elif mat[i][j] == 1:
            dist += 1
        mat_reached_e[i][j] = True
        candidates = []
        # try to add the four possible directions, if they're not reached yet,
        # or they're within the boundary of the matrix
        try:
            if not mat_reached_e[i-1][j]: candidates.append([i - 1, j])
        except: pass
        try:
            if not mat_reached_e[i+1][j]: candidates.append([i + 1, j])
        except: pass
        try:
            if not mat_reached_e[i][j-1]: candidates.append([i, j - 1])
        except: pass
        try:
            if not mat_reached_e[i][j+1]: candidates.append([i, j + 1])
        except: pass
        # if any of the candidate has a corresponding distance in the
        # result matrix, the search is over
        for c in candidates:
            if mat[c[0]][c[1]] == 0: 
                return dist
            elif mat_res[c[0]][c[1]] != -1:
                return dist + mat_res[c[0]][c[1]]
        if not computed: queue.extend(candidates)
        # if there's no candidate in queue, return dist
        if len(queue) == 0: return dist
            

# Test 1
mat = [[0,0,0],[0,1,0],[0,0,0]]
new_mat = updateMatrix(mat)
print("Question: ", mat, "\nAnswer", new_mat) # [[0, 0, 0], [0, 1, 0], [0, 0, 0]]


# Test 2
mat = [[0,0,0],[0,1,0],[1,1,1]]
new_mat = updateMatrix(mat)
print("Question: ", mat, "\nAnswer", new_mat) # [[0,0,0],[0,1,0],[1,2,1]]

