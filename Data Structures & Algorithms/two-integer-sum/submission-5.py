class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            pointer = index+1
            while pointer < len(nums):
                if num + nums[pointer] == target:
                    return [index, pointer]
                pointer += 1