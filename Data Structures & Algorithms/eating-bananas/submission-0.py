import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for i in range (len(piles)):
                hours += math.ceil( piles[i]/k )

            return hours <= h

        low = 1
        high = max(piles)
        least_k = high
        while(low <= high):
            mid = (low + high)//2

            if ( k_works(mid)):
                least_k = min(least_k , mid)
                high = mid - 1
            else:
                low = mid + 1
        return least_k   