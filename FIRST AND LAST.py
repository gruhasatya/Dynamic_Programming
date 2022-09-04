
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return [-1, -1]
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return [left, right]








def searchRange(self, nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]
    low =0
    high = len(nums) -1
    while low < high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.searchRange(nums, low, mid - 1, target)
        else:
            retrun self.searchRange(nums, mid + 1, high, target)
    return low if nums[low] == target else [-1, -1]



def searchRange(self, nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low if nums[low] == target else [-1, -1]




