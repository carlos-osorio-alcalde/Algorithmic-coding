# Solution 1
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        popped_elements = 0

        for i in range(len(nums)):
            new_index = i - popped_elements
            if nums[new_index] == val:
                nums.remove(nums[new_index])
                popped_elements += 1

        return len(nums)
