

nums = [-1, 0, 3, 5, 9, 12]
target = 9

class Solution(object):
    def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        # print(left)
        # print(right)

        while left <= right:
            mid = (left+right)//2

            if target==nums[mid]:
                print(mid)
                return mid
            elif target>nums[mid]:
                left = mid+1
            else:
                right = mid-1
        
        return -1



Solution.search(nums,target)
