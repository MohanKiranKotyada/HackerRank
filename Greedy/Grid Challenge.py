'''	Submissions	Leaderboard	Discussions	Editorial
Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. 
Return YES if they are or NO if they are not.'''

def gridChallenge(grid):
    grid=["".join(sorted(i)) for i in grid]
    
    
    for i in range(len(grid)-1):      #Transposing and comparing the vertical two elements each time
        for j in range(len(grid[i])):
            if grid[i][j] > grid[i+1][j]:
                return "NO"
    return "YES"
    