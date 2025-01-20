def liner_search(nums, num):
    for i in range(len(nums)):
        if nums[i] == num:
            return i

def binary_search(nums, num):
    cnt = 0
    low = 0
    hight = len(nums)-1
    while low <= hight:
        mid = (low + hight) // 2
        guess = nums[mid]
        cnt += 1
        if guess == num:
            return mid, cnt
        elif guess < num:
            low = mid + 1
        else:
            hight = mid - 1

nums = [23,43,43,12,57,34,134]
nums.sort()
print(liner_search(nums,43))
print(binary_search(nums,43))
