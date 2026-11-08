class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bin_search(l, h):
            while(l<=h):
                mid = (l+h)//2

                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    l = mid +1
                else:
                    h = mid -1
            return -1


        l=0
        r= len(nums) - 1

        while(l <r):

            m = (l+r)//2

            if nums[m]>nums[r]:
                l = m+1
            else:
                r=m
        
        min_index = r
        #in case  no rotation
        if min_index == 0:
            return bin_search(0, len(nums) - 1)
       
        if target >= nums[0] and target <= nums[ min_index-1]:
            return bin_search(0, min_index-1)
        else:
            return bin_search(min_index, len(nums)-1)
