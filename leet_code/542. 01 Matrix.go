

var directions = [4][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}


func updateMatrix(mat [][]int) [][]int {
    rows, cols := len(mat), len(mat[0])
	var queue [][]int
    
    visited := make([][]bool, rows)
    for y := 0; y < rows; y++ {
        visited[y] = make([]bool, cols)
    }
    
	for y := 0; y < rows; y++ {
		for x := 0; x < cols; x++ {
			if mat[y][x] == 0 {
				queue = append(queue, []int{y, x, 0})
                visited[y][x] = true
			} else {
				visited[y][x] = false
			}
		}
	}
    
	for len(queue) > 0 {
        cy, cx, dist := queue[0][0], queue[0][1], queue[0][2]
		queue = queue[1:]
        mat[cy][cx] = dist

		for _, dir := range directions {
			y, x := cy + dir[0], cx + dir[1]
            if !(0 <= y && y < rows && 0 <= x && x < cols) {
                continue
            }
            
            if false == visited[y][x] {
                queue = append(queue, []int{y, x, dist + 1})
                visited[y][x] = true
            }
		}
	}

	return mat
}