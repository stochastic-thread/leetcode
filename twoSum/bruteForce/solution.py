class Solution:
    def __init__(self):
        self = self

    def twoSum(self, nums, target):
        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                    if(x+y==target):
                        if(i != j):
                            return([i,j])
