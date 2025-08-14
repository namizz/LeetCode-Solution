class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0]*(n+1)
        for st, end, seat in bookings:
            arr[st-1] += seat
            arr[end] -= seat
        for i in range(1, n+1):
            arr[i] += arr[i-1]
        return arr[:-1]
        