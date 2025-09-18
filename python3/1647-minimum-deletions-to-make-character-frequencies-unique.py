from collections import Counter, defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)

        freq_count = defaultdict(int)
        for c in count:
            freq_count[count[c]] += 1
        
        freqs = list(freq_count.keys())
        freqs.sort(reverse = True)

        rem = []
        res = 0
        prev_freq = None
        for freq in freqs:
            if prev_freq != None:
                prev_freq -= 1
                while prev_freq > freq and rem:
                    res += (rem.pop() - prev_freq)
                    prev_freq -= 1
            rem.extend([freq] * (freq_count[freq] - 1))
            prev_freq = freq
        
        prev_freq -= 1
        while prev_freq > 0 and rem:
            res += (rem.pop() - prev_freq)
            prev_freq -= 1
        
        res += sum(rem)

        return res


