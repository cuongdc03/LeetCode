from bisect import bisect_right
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()  # Sort nums to consider the smallest elements first
        prefixSum = [0] * len(nums)
        
        # Compute prefix sums
        for i in range(len(nums)):
            prefixSum[i] = nums[i] + (prefixSum[i-1] if i > 0 else 0)
        
        ans = []
        for query in queries:
            # Find the maximum index where prefixSum[index] <= query
            maxLength = bisect_right(prefixSum, query)
            ans.append(maxLength)
        
        return ans