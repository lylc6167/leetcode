'''
class F:
    def f1(self,a):
        print( a*a)

F().f1(23)
'''

class Solution:

    def b_search(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

    def twoSum(self,nums,target):  # f返回[i,result]，
        nums1 = nums.copy()
        i=0
        while i <= len(nums):  # 此处切片
            nums2 = nums1[i+1:]
            target1 = target - nums[i]
            j = self.b_search(nums2,target1)
            if j is None:
                i+=1
            else:
                return [i,i+j+1]


