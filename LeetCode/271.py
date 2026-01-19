class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        # delimeter = sps
        encodedStrs = []
        for s in strs:
            es = s.replace("p", "pp")
            encodedStrs.append(es)
        return "sps".join(encodedStrs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        encodedStrs = s.split("sps")
        decodedStrs = []
        for s in encodedStrs:
            decodedStrs.append(s.replace("pp", "p"))
        return decodedStrs


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
