# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         memory = {} #dictionary
#         for i,value in enumerate(nums):
#             memory[value] = i;

#         for value in nums:
#             if (target - value) in memory:
#                 return [ memory[value],(memory[target - value]) ]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {} #dictionary
        for i,value in enumerate(nums):
            if (target-value) in memory:
                return [ memory[(target-value)], i]
            memory[value] = i;

