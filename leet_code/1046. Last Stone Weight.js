/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {
    stones.sort(function(a, b){return a - b})
    
    function bisect_left(nums, num) {
        let l = 0
        let r = nums.length - 1
        
        while (l <= r) {
            var m = parseInt((l + r)/2)    
            if (nums[m] == num)
                return m
            if (nums[m] > num)
                r = m - 1
            else
                l = m + 1
        }
        
        return l
    }
    
    while (stones.length > 2) {
        var item1 = stones.pop()
        var item2 = stones.pop()
        var diff = item1 - item2
        if (diff == 0) {
            continue
        }
        
        var idx = bisect_left(stones, diff)
        stones.splice(idx, 0, diff)
    }
    
    return stones[0]
};


console.log(lastStoneWeight([1,3]))