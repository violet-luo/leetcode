def construct(self, grid: List[List[int]]) -> 'Node':
    # take in top left and bottom right coordinates
    # check if everything inbetween is the same
    def allsame(startx,starty,endx,endy): 
        ori_val = grid[startx][starty]
        for x in range(startx,endx+1):
            for y in range(starty, endy+1):
                if grid[x][y] != ori_val:
                    return False
        return True


    def helper(startx, starty, endx, endy):
        if allsame(startx,starty, endx, endy):
            # make it a leaf
            return Node(grid[startx][starty], True, None, None, None, None)

        midx = (startx + endx) // 2
        midy = (starty + endy) // 2
        return Node(
            True, 
            False,
             helper(startx, starty, midx,midy), 
             helper(startx, midy+1, midx, endy), 
             helper(midx+1, starty, endx, midy), 
             helper(midx+1,midy+1, endx, endy)
             )
             
    return helper(0,0,len(grid)-1,len(grid[0])-1)
