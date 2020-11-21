

def solution(nums):
    n = len(nums)
    mval = 0
    if n < 2:
        return 0

    for i in range(n-1):
        ls = nums[i]
        l = i-1
        rs = nums[i+1]
        r = i+2

        while True:
            if ls == rs:
                mval = max(ls, mval)
            if ls <= rs and l >= 0:
                ls += nums[l]
                l -= 1
            elif ls >= rs and r < n:
                rs += nums[r]
                r += 1
            elif l < 0 or r >= n:
                break
    return mval


#print(3 == solution([1, 1, 2, 3]))
#print(0 == solution([1, 2, 4, 5]))