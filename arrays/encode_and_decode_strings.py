class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encodedStrs = ''.join(map(lambda s: str(len(s)) + "#" + s,strs))
        return encodedStrs

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        i = 0
        strs = []
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1
            strs.append(s[i+1:i+1+int(length)])
            i += int(length) + 1
        return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
