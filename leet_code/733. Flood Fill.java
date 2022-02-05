import java.util.Queue;
import java.util.Arrays;
import java.util.LinkedList;


class Solution {
    class Coord {
        public int y;
        public int x;
        
        Coord(int y, int x) {
            y = y;
            x = x;
        }
    }

    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int rows = image.length;
        int cols = image[0].length;
        int clr = image[sr][sc];
        
        Queue<Coord> q = new LinkedList<>();        
        q.add(new Coord(sr, sc));
        boolean [][] visited = new boolean[rows][cols];
        for(int i = 0; i < visited.length; i++) {
            Arrays.fill(visited[i], false);
        }
        
        int ycoords[] = {1, -1, 0, 0};
        int xcoords[] = {0, 0, 1, -1};
        
        while (!q.isEmpty()) {
            Coord res = q.poll();
            int y = res.y;
            int x = res.x;
            
            if ((image[y][x] != clr) || (image[y][x] == newColor) || (true == visited[y][x]))
                continue;
            
            image[y][x] = newColor;
            visited[y][x] = true;
            
            for (int i = 0; i < 4; i++) {
                int ny = y + ycoords[i];
                int nx = x + xcoords[i];
                
                if (!(0 <= ny && ny < rows && 0 <= nx && nx < cols))
                    continue;
            
                q.add(new Coord(ny, nx));
            }
        }
        
        return image;
    }

    void dfs(int[][] image, int y, int x, int clr, int newColor) {
        if (image[y][x] != clr || image[y][x] == newColor)
            return;
    
        image[y][x] = newColor;

        int ycoords[] = {1, -1, 0, 0};
        int xcoords[] = {0, 0, 1, -1};
        
        for (int i = 0; i < 4; i++) {
            int ny = y + ycoords[i];
            int nx = x + xcoords[i];
            if (!(0 <= ny && ny < rows && 0 <= nx && nx < cols))
                continue
            
            dfs(ny, nx);
        }
    }

    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int rows = image.length;
        int cols = image[0].length;
        int clr = image[sr][sc];

        
        dfs(image, sr, sc, clr, newColor);
    }

    public static void main(String[] args) {
    }
}