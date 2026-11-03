class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        current_sum = 0
        count = 0
        prefix_count = {0: 1}

        for num in nums:
            current_sum += num

            needed = current_sum - k

            if needed in prefix_count:
                count += prefix_count[needed]

            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return count