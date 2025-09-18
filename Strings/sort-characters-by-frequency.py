class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        result = ""
        for c in s:
            freq[c] = freq.get(c,0)+1
        sorted_ch = sorted(freq.items(),key =lambda x:x[1],reverse = True)
        for ch ,count in sorted_ch:
            result = result+ch*count
        return result