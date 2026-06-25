class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "[]"
        encoded_string = ""
        for i in strs:
            encoded_string+= i + " _n"
        return encoded_string[:-3]
    def decode(self, s: str) -> List[str]:
        if s=="[]":
            return []
        return s.split(" _n") 