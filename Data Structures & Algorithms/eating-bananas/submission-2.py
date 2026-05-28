class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force
        # max_rate = max(piles)
        # min_rate = 1
        
        # for i in range(min_rate, max_rate + 1):
        #     sum = 0
        #     for j in range(len(piles)):
        #         sum += math.ceil(piles[j] / i)
        #     if sum <= h:
        #         return i
        # return max_rate

        # efficient    
        left = 1
        right = max(piles)
        
        while left <= right:
            sum = 0
            mid = (left + right) // 2
            for i in range(len(piles)):
                sum += math.ceil(piles[i] / mid)  # Fixed: use / instead of //
            if sum <= h:  # Also note: should be <= not 
                right = mid - 1
            else:
                left = mid + 1
        return left