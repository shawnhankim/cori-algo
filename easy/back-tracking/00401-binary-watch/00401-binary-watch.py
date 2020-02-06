"""
401. Binary Watch

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:

The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

Expected Example:

1. num:0, res1: ['0:00']
          res2: ['0:00']

2. num:1, res1: ['0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00', '8:00']
          res2: ['0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00', '8:00']

3. num:2, res1: ['0:03', '0:05', '0:06', '0:09', '0:10', '0:12', '0:17', '0:18', '0:20', '0:24', '0:33', '0:34', '0:36', '0:40', '0:48', '1:01', '1:02', '1:04', '1:08', '1:16', '1:32', '2:01', '2:02', '2:04', '2:08', '2:16', '2:32', '3:00', '4:01', '4:02', '4:04', '4:08', '4:16', '4:32', '5:00', '6:00', '8:01', '8:02', '8:04', '8:08', '8:16', '8:32', '9:00', '10:00']
          res2: ['0:03', '0:05', '0:06', '0:09', '0:10', '0:12', '0:17', '0:18', '0:20', '0:24', '0:33', '0:34', '0:36', '0:40', '0:48', '1:01', '1:02', '1:04', '1:08', '1:16', '1:32', '2:01', '2:02', '2:04', '2:08', '2:16', '2:32', '3:00', '4:01', '4:02', '4:04', '4:08', '4:16', '4:32', '5:00', '6:00', '8:01', '8:02', '8:04', '8:08', '8:16', '8:32', '9:00', '10:00']

"""

import math

class Solution(object):
    def __init__(self):
        self.max_h = 12
        self.max_m = 60
        self.bits  = self.max_m * [None]
        for i in range(self.max_m):
            self.bits[i] = self._bits(i)


    def read_binary_watch(self, num):
        if not num: return ["0:00"]
        res = []
        for h in range(self.max_h):
            for m in range(self.max_m):
                self._add_res(res, num, h, m)
        return res


    def read_binary_watch2(self, num):
        if not num: return ["0:00"]
        res = []
        for h in range(self.max_h):
            self._helper(res, num, h)
        return res


    def _helper(self, res, num, h, m=0):
        if m == self.max_m: return
        self._add_res(res, num, h, m)
        self._helper(res, num, h, m+1)


    def _bits(self, num):
        if num == 0: return 0
        max_bits = int(math.log(num, 2)) + 1
        num_bits = 0
        for i in range(max_bits):
            if num & 1: num_bits += 1
            num >>= 1
        return num_bits

 
    def _add_res(self, res, num, h, m):
        sum_bits = self.bits[h] + self.bits[m]
        if sum_bits == num: res.append(f"{h}:{m:02}")


    def test(self):
        test_cases = {0, 1, 2, 3, 4, 5}
        for i, num in enumerate(test_cases, 1):
            res1 = self.read_binary_watch(num)
            res2 = self.read_binary_watch2(num)
            print(f"\n{i}. num:{num}, res1: {res1}")
            print(f"          res2: {res2}")


def main():
    Solution().test()


if __name__ == '__main__':
    main()

