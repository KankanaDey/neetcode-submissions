class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low=0
        r= len(nums) - 1

        while(low <r):

            m = (low+r)//2

            if nums[m]>nums[r]:
                low = m+1
            else:
                r=m
        
        min_index = r
        #in case  no rotation
        if min_index == 0:
            l,h=0, (len(nums) - 1)
       
        elif target >= nums[0] and target <= nums[ min_index-1]:
            l,h = 0, min_index-1
        else:
            l,h = min_index, (len(nums)-1)

        while(l<=h):
            mid = (l+h)//2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid +1
            else:
                h = mid -1
        return -1
