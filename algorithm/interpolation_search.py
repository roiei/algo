
def find(a, n, key):
    left = 0
    right = n - 1
    while right >= left:
        if a[right] != a[left]:
            mid = left + (value - a[left])*(right - left) // (a[right] - a[left])
            if mid < left:      # when finding 1 from [10, 11, 11, 20], 
                mid = left      # mid could have negative value
            if mid > right:
                mid = right
        else:
            mid = left          # all values between left and right are same

        if value = a[mid]:
            return mid
        if value > a[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False
