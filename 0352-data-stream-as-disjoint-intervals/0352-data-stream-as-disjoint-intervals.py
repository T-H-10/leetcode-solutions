class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        i = bisect.bisect_left([s for s, e in self.intervals], value)

        prev = self.intervals[i-1] if i > 0 else None
        nxt = self.intervals[i] if i < len(self.intervals) else None

        if prev and prev[0] <= value <= prev[1]:
            return

        if nxt and nxt[0] == value:
            return

        touch_left = prev and prev[1] + 1 == value
        touch_right = nxt and nxt[0] == value + 1

        if touch_left and touch_right:
            prev[1] = nxt[1]
            del self.intervals[i]
        elif touch_left:
            prev[1] = value
        elif touch_right:
            nxt[0] = value
        else:
            self.intervals.insert(i, [value, value])
        return
        
    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()