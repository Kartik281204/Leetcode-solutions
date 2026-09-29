class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:

        left = 0
        right = len(nums) - 1

        while left < right:

            # Find an odd number from the left
            while left < right and nums[left] % 2 == 0:
                left += 1

            
            while left < right and nums[right] % 2 == 1:
                right -= 1

            
            nums[left], nums[right] = nums[right], nums[left]

        return nums
        # while left < right:
           
        #     while left < right and nums[left]%2 == 0:
        #         left += 1
            
        #     while left < right and nums[right]%2 == 1:
        #         right -= 1
        
        #     nums[left],nums[right] == nums[right],nums[left]

        # return nums    
        # new_nums = []
        # for i in range(len(nums)):
        #     if nums[i]%2 == 0:
        #         new_nums.append(nums[i])
        # for j in range(len(nums)):
        #     if nums[j]%2 == 1:
        #         new_nums.append(nums[j])
        # return new_nums
            