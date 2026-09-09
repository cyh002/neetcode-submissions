from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.key_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # Binary Search
        # get the key
        key_list = self.key_map[key]
        if not key_list:
            return ""
        # find the exact match, with cache
        left = 0 
        right = len(key_list) - 1
        cache = ""
        while right >= left:
            mid = left + (right - left) // 2
            if timestamp == key_list[mid][0]:
                return key_list[mid][1]
            if key_list[mid][0] <= timestamp:
                # move left
                cache = key_list[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return cache
    

    # [1, 3, 6, 9, 11, 13]
    # find 4
    # 