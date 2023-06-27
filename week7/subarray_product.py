"""https://leetcode.com/problems/subarray-product-less-than-k/"""

# First attempt: Brute force (Time limit exceeded :( )
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n_subarrays = 0
        n = len(nums)
        
        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                if product < k:
                    n_subarrays += 1
        
        return n_subarrays


# Second attempt: Two pointers - like solution
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        n_subarrays = 0
        prod = 1

        i = 0
        j = 0

        for j, num in enumerate(nums):
            prod *= num
            while (prod >= k) and (i <= j):
                prod /= nums[i]
                i += 1
            n_subarrays += 1 + (j - i)
            
        return n_subarrays
