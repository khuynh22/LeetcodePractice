class Solution:
    def missingElement(self, nums, k: int) -> int:
        l = 0
        r = len(nums)-1
        missing = lambda idx: nums[idx] - nums[0] - idx
        if k > missing(r) : return nums[-1]+k - missing(r)
        
        while r-l>1 :
            mid = l + (r-l)//2
            x = missing(mid) 
            if x>=k:
                r = mid
            elif x<k:
                l = mid
       
        return nums[l] + k - missing(l)
    
s = Solution()
print(s.missingElement([4,7,9,10], 1))
print(s.missingElement([4,7,9,10], 3))
print(s.missingElement([1,2,4], 3))