class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        count = {0: 1}
        prefix = 0
        answer = 0

        for num in nums:

            if num % 2 != 0:
                prefix += 1

            if prefix - k in count:
                answer += count[prefix - k]

            count[prefix] = count.get(prefix, 0) + 1

        return answer
# class Solution:
#     def numberOfSubarrays(self, nums: list[int], k: int) -> int:
#         result = []
#         left = 0 
#         right = left + 1 
#         count = 0
#         for num in nums:
#             if num%2 == 0:
#                 result.append(1)
#             else:
#                 result.append(0)
#         while left:
            
            
            

        