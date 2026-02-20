class Solution:
    def rec(self, s: str) -> str:
        if not s:
            return ""
        chunks = []
        count = 0
        start = 0
        for i, ch in enumerate(s):
            count += 1 if ch == '1' else -1
            if count == 0:
                inner = self.rec(s[start + 1:i])
                chunks.append("1" + inner + "0")
                start = i + 1
        chunks.sort(reverse=True)
        return "".join(chunks)

    def makeLargestSpecial(self, s: str) -> str:
        return self.rec(s)
