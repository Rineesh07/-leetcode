class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        a = [0] *( n + 1)
        print(a)
        for l , r , v in bookings:
            a[l-1] += v
            a[r] -= v
        print(a)
        prefix = []
        rs = 0 
        for i in range(len(a)):
            rs += a[i]
            prefix.append(rs)
        return prefix[:n]