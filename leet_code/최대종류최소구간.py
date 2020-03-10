

def find_min_cover_range(nums):
    unum = len(set(nums))
    uniq = {}
    index = []
    min_diff = 0x7FFFFFFF
    for i in range(len(nums)): 
        if nums[i] not in uniq:
            uniq[nums[i]] = i
            index.append([nums[i], i])
        elif nums[i] == index[0][0]:
            del uniq[nums[i]]
            uniq[nums[i]] = i
            index.pop(0)
            index.append([nums[i], i])
        if unum == len(uniq):
            min_diff = min(min_diff, uniq[index[-1][0]]-uniq[index[0][0]])
            del uniq[index[0][0]]
            index.pop(0)

    return min_diff+1


# print(find_min_cover_range([1, 1, 2, 2, 2]))
print(find_min_cover_range([1, 2, 1, 3, 2]))
print(find_min_cover_range([1, 1, 2, 3, 2]))
print(find_min_cover_range([0, 1, 1, 1, 1, 2, 2, 2, 2]))
# 1, 1, 2, 3, 2 -> [1, 3]
