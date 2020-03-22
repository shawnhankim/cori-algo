"""
763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.

Expected Results:

1. Test Case: ababcbacadefegdehijhklij
   - Result 1 : [9, 7, 8]
   - Result 2 : [9, 7, 8]
   - Assert res1 == res2 : True

2. Test Case: aabbaccd
   - Result 1 : [5, 2, 1]
   - Result 2 : [5, 2, 1]
   - Assert res1 == res2 : True

3. Test Case: aabbbccd
   - Result 1 : [2, 3, 2, 1]
   - Result 2 : [2, 3, 2, 1]
   - Assert res1 == res2 : True

4. Test Case:
   - Result 1 : []
   - Result 2 : []
   - Assert res1 == res2 : True

5. Test Case: a
   - Result 1 : [1]
   - Result 2 : [1]
   - Assert res1 == res2 : True

6. Test Case: ab
   - Result 1 : [1, 1]
   - Result 2 : [1, 1]
   - Assert res1 == res2 : True

"""

class Solution:
    def partitionLabels1(self, S):
        res, hs, max_idx, temp = [], set(), 0, 0
        for i, c in enumerate(S):
            if c not in hs: 
                hs.add(c)
                max_idx = max(max_idx, S.rindex(c))
            if i == max_idx:
                res.append(i - temp)
                temp = i
        if len(res) > 0:
            res[0] += 1
        return res


    def partitionLabels2(self, S):
        res, hs, max_idx, prev_idx = [], {}, 0, 0
        for i, c in enumerate(S):
            if c not in hs:
                hs[c] = 1
                max_idx = max(max_idx, S.rindex(c))
            if i == max_idx:
                partition_len = i+1 if len(res) == 0 else i-prev_idx
                res.append(partition_len)
                prev_idx = i
        return res

                
    def test(self):
        test_cases = [
            "ababcbacadefegdehijhklij",
            "aabbaccd",
            "aabbbccd",
            "",
            "a",
            "ab"
        ]
        for i, S in enumerate(test_cases, 1):
            print(f"\n{i}. Test Case: {S}")
            res1 = self.partitionLabels1(S)
            res2 = self.partitionLabels2(S)
            print(f"   - Result 1 : {res1}")
            print(f"   - Result 2 : {res2}")
            print(f"   - Assert res1 == res2 : {res1 == res2}")


if __name__ == '__main__':
    Solution().test()

                     
        

