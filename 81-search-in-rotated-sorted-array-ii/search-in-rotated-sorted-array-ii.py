class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        for i in range(len(nums)):
            if nums[i] < nums[i - 1]:
                mid = i
                break
        array1 = nums[0:i]
        array2 = nums[i:]
        new_array = array2 + array1 
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if new_array[mid] == target:
                return True
            else:
                if new_array[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False 

            
