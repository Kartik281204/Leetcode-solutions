class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = 0
        l = 0  
        new_array = []
        new_array.append(nums[0])
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            new_array.append(nums[i])
        # new_array.sort()
        return new_array 
            
            




        