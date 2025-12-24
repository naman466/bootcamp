from collections import Counter, defaultdict

def topKFrequent(nums, k):
    freq = Counter(nums)  
    
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]
    for num, f in freq.items():
        buckets[f].append(num)
    
    res = []
    for i in range(n, 0, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))  
