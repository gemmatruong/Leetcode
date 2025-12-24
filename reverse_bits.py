class Solution:
    def reverseBits(self, n: int) -> int:


        # WAY 3: dec = binary_digit * 2 + dec (from left to right)
        string_num = ""

        for _ in range(32):
            string_num += str(n % 2)
            n //= 2
        
        result = 0

        for d in string_num:
            result = result * 2 + int(d)
        
        return result