class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(list(s.split())) == 0:
            return 0
        return len(list(s.split())[-1])
