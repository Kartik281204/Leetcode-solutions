class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:

        left = 0
        right = len(letters)

        while left < right:

            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid

            else:
                left = mid + 1

        return letters[left % len(letters)]


# class Solution:
#     def nextGreatestLetter(self, letters: list[str], target: str) -> str:
#         left = 0
#         right = len(letters) - 1
#         while left <= right:
#             mid = (left + right)//2
#             if letters[mid] == target:
#                 return letters[mid + 1]
#             elif letters[mid] > target:
#                 right = mid 
#             else:
#                 left = mid - 1
#             return letters[left] 