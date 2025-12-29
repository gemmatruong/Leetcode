class Solution:
    def reverseBits(self, n: int) -> int:
        # WAY 1
        # if n == 0:
        #     return 0
            
        # # convert decimal number to binary number (but in reversed order)
        # binary_num = ""
        # while n > 0:
        #     binary_num += chr(ord('0') + int(n%2))
        #     n = n // 2
        
        # # if length of binary number is less than 32 bit
        # # size extend with 0s
        # if len(binary_num) < 32:
        #     for _ in range(32-len(binary_num)):
        #         binary_num += '0' 

        # # convert binary to decimal
        # i = 0
        # result = 0
        # length = len(binary_num) - 1
        # while length >= 0:
        #     result += int(binary_num[length]) * (2**i)
        #     length -= 1
        #     i += 1
        
        # return result

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