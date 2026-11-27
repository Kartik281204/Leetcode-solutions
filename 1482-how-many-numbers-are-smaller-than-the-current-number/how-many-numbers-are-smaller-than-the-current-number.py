class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        count = {}

        for i,num in enumerate(sorted_nums):
            if num not in count:
                count[num] = i 
        
        answer = []

        for num in nums:
            answer.append(count[num])

        return answer

