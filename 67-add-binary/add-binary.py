class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]
        #[2:] is used to remove 0b at the starting
        
        