#INTUITION
# Say if you have two meetings, one which gets over early and another which gets over late. Which one should we choose?  If our meeting lasts longer the room stays occupied and we lose our time. On the other hand, if we choose a meeting that finishes early we can accommodate more meetings. Hence we should choose meetings that end early and utilize the remaining time for more meetings.

#APPROACH
#And so we sort it to get meetings that end early.And keep checking if they overlap
class Meeting:
    def __init__(self, start, stop, pos):
        self.start = start
        self.stop = stop
        self.pos = pos

class Solution:
    def maximumMeetings(self, n, start, end):
        meet = []
        for i in range(n):
            meet.append(Meeting(start[i], end[i], i + 1))
        meet.sort(key=lambda x: (x.stop, x.pos))
        
        ans = []
        limit = meet[0].stop
        ans.append(meet[0].pos)
        
        for i in range(1, len(meet)):
            if limit < meet[i].start:
                limit = meet[i].stop
                ans.append(meet[i].pos)
        return len(ans)
