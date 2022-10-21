class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        result = []
        for s in strs:
            tmp = ""
            tmp += str(len(s)) + " " + s
            result.append(tmp)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        result = []
        idx = 0
        while idx < len(s):
            nextStrLen = ""
            while s[idx] != " ":
                nextStrLen += s[idx]
                idx += 1
            nextStrLen = int(nextStrLen)
            tmp = idx
            idx += 1 + nextStrLen
            result.append(s[tmp + 1 : idx])
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
