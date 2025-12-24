class Solution
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hmap = {}
        max_freq = 0
        max_freq_elements = []

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

            if hmap[num] > max_freq:
                max_freq = hmap[num]
                max_freq_elements = [num]
            elif hmap[num] == max_freq:
                max_freq_elements.append(num)

        return len(list(set(max_freq_elements)))*hmap[max_freq_elements[0]]
