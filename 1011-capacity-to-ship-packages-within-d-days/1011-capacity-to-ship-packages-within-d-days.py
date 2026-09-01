def canship(weights : List[int] , dayshave: int , k:int) -> bool :  
    daysneeded = 0
    currentsum = 0 
    for weight in weights :
        if currentsum + weight <=  k:
            currentsum += weight
        else:
            currentsum = weight
            daysneeded += 1
    if currentsum != 0 :
        daysneeded += 1
    return daysneeded <= dayshave
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) ->  int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            print(low,high)
            mid = (low+high)//2 
            if canship(weights,days,mid):
                high = mid 
            else:
                low = mid + 1
        return low
            