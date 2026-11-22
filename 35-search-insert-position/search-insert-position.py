class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left
# class Solution:
#     def searchInsert(self, nums: list[int], target: int) -> int:
#         left = 0
#         right = len(nums) - 1 
#         mid = (left + right)//2
#         for num in nums:
#             if target > nums[mid]:
#                 left = mid 
#             elif target < nums[mid]:
#                 right= mid + 1 
#             else:
#                 return mid 
                
                
            