

func kthDistinct(arr []string, k int) string {
    freq := make(map[string]int)
    
    for _, val := range arr {
        freq[val] += 1
    }
    
    for _, val := range arr {
        if freq[val] == 1 {
            if k - 1 == 0 {
                return val
            }
            k -= 1
        }
    }
    
    return ""
}