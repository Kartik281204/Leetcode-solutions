class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # answer = set()
        # for num in nums1:
        #     if num in nums2:
        #         answer.add(num)
        # return list(answer)  
        
        set1 = set(nums1)
        set2 = set(nums2) 

        return list(set1 & set2)   
        