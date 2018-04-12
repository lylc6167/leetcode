class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for x in range(i+1,len(nums)):
                if i!=x and target==nums[i]+nums[x]:
                    return [i,x]