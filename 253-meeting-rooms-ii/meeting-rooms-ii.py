class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        n = len(intervals)
        used_rooms = 0
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        end_pointer = 0
        start_pointer = 0
        while start_pointer < n:
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -= 1
                end_pointer += 1
            used_rooms += 1    
            start_pointer += 1   
        return used_rooms
        