class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            current = target - num
            if current in num_map:
                return [num_map[current], i]
            num_map[num] = i
        return []