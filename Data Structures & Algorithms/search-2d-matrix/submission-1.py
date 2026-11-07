class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        h= len(matrix) -1

        while ( l<= h) :
            mid = (l+h)//2

            if target < matrix[mid][0]:
                h = mid - 1
            elif target > matrix[mid][-1]: #last element index: -1
                l = mid + 1
            else:
                #target is in the mid row 
                inner_l = 0
                inner_h = len(matrix[mid]) -1

                while(inner_l<= inner_h):
                    inner_mid = (inner_l + inner_h)//2

                    if target == matrix[mid][inner_mid]:
                        return True
                    elif target < matrix[mid][inner_mid]:
                        inner_h = inner_mid - 1
                    else: 
                        inner_l = inner_mid + 1
                return False
        return False
                    
                        