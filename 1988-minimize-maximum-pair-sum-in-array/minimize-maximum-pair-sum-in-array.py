class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0 
        right = len(nums) - 1 
        maximum = 0 
        while left < right:
            sum = nums[left] + nums[right] 
            maximum = max(maximum,sum)

            left += 1
            right -= 1


        return maximum 
        
        # nums.sort()
        # summed = []
        # left = 0 
        # right = len(nums) - 1  
        # while left < right:
        #     sum = nums[right] + nums[left]
        #     summed.append(sum)
        #     summed.append(sum)
        #     left +=1
        #     right -= 1
        # return max(summed) 
        
        # sum = []
        # nums.sort()
        # while nums:
        #     min_number = min(nums)
        #     max_number = max(nums) 
        #     nums.remove(min_number)
        #     nums.remove(max_number)
        #     number_sum = min_number + max_number
        #     sum.append(number_sum)
        # return max(sum)


         
        

        