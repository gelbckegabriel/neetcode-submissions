class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = {}
        for number in nums:
            if values.get(number) is None:
                values[number] = 1
            else:
                return True
        return False