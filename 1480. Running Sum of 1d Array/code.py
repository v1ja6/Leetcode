class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
       
        new = [0]
        for a in nums:
            value = a + new[-1]
            new.append(value)
        new.pop(0)
        return new
