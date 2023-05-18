# Solution 1: First try: two nested-loops, not the best.
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum_unique = 0

        for num_1 in nums:
            n_matches = 0
            for num_2 in nums:
                if num_1 == num_2:
                    n_matches += 1
                    continue

            if n_matches == 1:
                sum_unique += num_1

        return sum_unique


# Solution 2: Cleaner, but still O(n2)
class Solution2:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique_numbers = 0

        for num in nums:
            if nums.count(num) == 1:
                unique_numbers += num

        return unique_numbers


# Solution 3: Using a dictionary to store the occurrences of each number
class Solution3:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique_numbers = 0
        occurrences = {}

        for num in nums:
            if num in occurrences:
                occurrences[num] += 1
            else:
                occurrences[num] = 1

        for num in occurrences:
            if occurrences[num] == 1:
                unique_numbers += num

        return unique_numbers
