

func smallestEqual(nums []int) int {
    var res int = -1
    for i, num := range nums {
        if i%10 == num {
            res = i
            break
        }
    }
    
    return res
}