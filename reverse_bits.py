class Solution:
    def reverseBits(self, n: int) -> int:
        

        # WAY 2: bit-by-bit build - O(32) time and O(1) space
        # if n == 0:
        #     return 0

        # result = 0

        # # run thru 32 bits
        # for i in range(32):
        #     # result << 1: shift to right 1 bit, make room for the new bit
        #     # n & 1: extract the last bit from n (use AND bitwise with 1)
        #     # (result << 1) | (n & 1): the OR bitwise used to insert the extracted bit from n
        #     # to the space has been made for the new bit in result
        #     result = (result << 1) | (n & 1)
        #     n >>= 1
        # # "reading" bits from right-to-left and "writing" them left-to-right.
        # return result

        # WAY 3: dec = binary_digit * 2 + dec (from left to right)
        string_num = ""

        for _ in range(32):
            string_num += str(n % 2)
            n //= 2
        
        result = 0

        for d in string_num:
            result = result * 2 + int(d)
        
        return result