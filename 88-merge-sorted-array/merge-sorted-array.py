class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums3 = nums1[:m]
        result = nums3 + nums2
        result.sort()
        nums1[:] = result 
