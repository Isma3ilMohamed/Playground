class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        mapping = defaultdict(list)
        for name, time, web in zip(username, timestamp, website):
            mapping[name].append((time, web))
        print(mapping)

        counter = Counter()
        for name in mapping:
            mapping[name].sort(key=lambda x:x[0])
            arr = []
            for i in mapping[name]:
                arr.append(i[1])
            for a, b, c in set(combinations(arr, 3)):
                counter[(a, b, c)] += 1
            
        pattern, count = "", 0
        for item, c in counter.items():
            if c > count:
                pattern = item
                count = c
            if count == c and pattern > item:
                pattern = item
        return pattern
