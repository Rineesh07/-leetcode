class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        trip = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        trip.append((i,j,k))
        print(trip)
        triplets_cnt = 0 
        triplets_cnt = len(trip)
        return triplets_cnt