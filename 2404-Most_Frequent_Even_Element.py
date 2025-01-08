class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num % 2 ==0:
                map[num] = 1 if num not in map else map[num] + 1
        maxx = 0    
        output = -1        
        for num, count in map.items():
            if count > maxx:
                maxx, output = count, num
            elif count == maxx:
                output = min(num,output)
        return output