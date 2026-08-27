import bisect
class TimeMap:

    def __init__(self):
        self.keystore = defaultdict(list)
        '''
        {
            "alice": [(time1, happy)]
            "bonnie": [(time1, happy)]
        }
        '''

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort_left(self.keystore[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keystore:
            return ""
        
        values = self.keystore[key]
        index = bisect.bisect_right(values, (timestamp, chr(255)))

        if index == 0:
            return ""
        
        return values[index - 1][1]
        
