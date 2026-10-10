class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        #print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        j=0
        
        dec = []
        while i<len(s):
            j=i
            while s[j] != "#":
                j = j+1
            length = int(s[i:j])
            dec.append(s[j+1:j+1+length])
            i = j + 1 + length
        return dec




