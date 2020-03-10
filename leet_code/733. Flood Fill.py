class Solution:
    def fill(self, image, rows, cols, r, c, cclr, nclr):
        if nclr == image[r][c]:
            return
        image[r][c] = nclr
        if r > 0 and image[r-1][c] == cclr:
            self.fill(image, rows, cols, r-1, c, cclr, nclr)
        if r < rows-1 and image[r+1][c] == cclr:
            self.fill(image, rows, cols, r+1, c, cclr, nclr)
        if c > 0 and image[r][c-1] == cclr:
            self.fill(image, rows, cols, r, c-1, cclr, nclr)
        if c < cols-1 and image[r][c+1] == cclr:
            self.fill(image, rows, cols, r, c+1, cclr, nclr)

    def floodFill(self, image, sr, sc, newColor):
        cclr = image[sr][sc]
        if cclr == newColor:
            return image
        self.fill(image, len(image), len(image[0]), sr, sc, cclr, newColor)
        return image


    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])
        clr = image[sr][sc]
        
        def dfs(y, x):
            if image[y][x] != clr or image[y][x] == newColor:
                return
        
            image[y][x] = newColor
            
            for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue
                
                dfs(ny, nx)
        
        dfs(sr, sc)
        return image


image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1

stime = time.time()
sol = Solution()
ret = sol.floodFill(image, sr, sc, newColor)
print('elapse time: {} sec'.format(time.time() - stime))
print(ret)