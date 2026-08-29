class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
                word_length = len(word)
                transform = f"{word_length}#{word}"
                encoded.append(transform)
        transform_str = "".join(encoded)
        return transform_str


    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
                pos = s.find('#', i)
                pos_len = int(s[i:pos])
                word = s[pos + 1:pos+pos_len + 1]
                decoded.append(word)
                i = pos + pos_len + 1
        return decoded
                
