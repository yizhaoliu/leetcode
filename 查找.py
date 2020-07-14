class Solution:
    def search(self, nums, target: int) -> int:
        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[r]: # 右半边有序
                if (nums[mid] < target and nums[r] >= target):
                    l = mid + 1
                else:
                    r = mid - 1
            else:# 左半边有序
                if nums[l] <= target and nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
