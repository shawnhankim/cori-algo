"""
68. Text Justification

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Expected Results:

Test Case 1. maxwidth:16, words:['This', 'is', 'an', 'example', 'of', 'text', 'justification.']
word_length: [4, 2, 2, 7, 2, 4, 14]
lines : [[0, 1, 2], [3, 4, 5], [6]]
spaces: [8, 3, 2]
word_spaces: [[4, 4, 0], [2, 1, 0], [2]]
  - Result 1: ['This    is    an', 'example  of text', 'justification.  ']
  - Expected: ['This    is    an', 'example  of text', 'justification.  ']
  - Assert 1: True

Test Case 2. maxwidth:16, words:['What', 'must', 'be', 'acknowledgment', 'shall', 'be']
word_length: [4, 4, 2, 14, 5, 2]
lines : [[0, 1, 2], [3], [4, 5]]
spaces: [6, 2, 9]
word_spaces: [[3, 3, 0], [2], [1, 8]]
  - Result 1: ['What   must   be', 'acknowledgment  ', 'shall be        ']
  - Expected: ['What   must   be', 'acknowledgment  ', 'shall be        ']
  - Assert 1: True

Test Case 3. maxwidth:20, words:['Science', 'is', 'what', 'we', 'understand', 'well', 'enough', 'to', 'explain', 'to', 'a', 'computer.', 'Art', 'is', 'everything', 'else', 'we', 'do']
word_length: [7, 2, 4, 2, 10, 4, 6, 2, 7, 2, 1, 9, 3, 2, 10, 4, 2, 2]
lines : [[0, 1, 2, 3], [4, 5], [6, 7, 8, 9], [10, 11, 12, 13], [14, 15, 16], [17]]
spaces: [5, 6, 3, 5, 4, 18]
word_spaces: [[2, 2, 1, 0], [6, 0], [1, 1, 1, 0], [2, 2, 1, 0], [2, 2, 0], [18]]
  - Result 1: ['Science  is  what we', 'understand      well', 'enough to explain to', 'a  computer.  Art is', 'everything  else  we', 'do                  ']
  - Expected: ['Science  is  what we', 'understand      well', 'enough to explain to', 'a  computer.  Art is', 'everything  else  we', 'do                  ']
  - Assert 1: True

Test Case 4. maxwidth:16, words:['ask', 'not', 'what', 'your', 'country', 'can', 'do', 'for', 'you', 'ask', 'what', 'you', 'can', 'do', 'for', 'your', 'country']
word_length: [3, 3, 4, 4, 7, 3, 2, 3, 3, 3, 4, 3, 3, 2, 3, 4, 7]
lines : [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13], [14, 15, 16]]
spaces: [6, 2, 5, 4, 2]
word_spaces: [[3, 3, 0], [1, 1, 0], [2, 2, 1, 0], [2, 1, 1, 0], [1, 1, 0]]
  - Result 1: ['ask   not   what', 'your country can', 'do  for  you ask', 'what  you can do', 'for your country']
  - Expected: ['ask   not   what', 'your country can', 'do  for  you ask', 'what  you can do', 'for your country']
  - Assert 1: True

Test Case 5. maxwidth:30, words:["Don't", 'go', 'around', 'saying', 'the', 'world', 'owes', 'you', 'a', 'living;', 'the', 'world', 'owes', 'you', 'nothing;', 'it', 'was', 'here', 'first.']
word_length: [5, 2, 6, 6, 3, 5, 4, 3, 1, 7, 3, 5, 4, 3, 8, 2, 3, 4, 6]
lines : [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16], [17, 18]]
spaces: [8, 7, 5, 20]
word_spaces: [[2, 2, 2, 2, 0], [2, 2, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0], [1, 19]]
  - Result 1: ["Don't  go  around  saying  the", 'world  owes  you a living; the', 'world owes you nothing; it was', 'here first.                   ']
  - Expected: ["Don't  go  around  saying  the", 'world  owes  you a living; the', 'world owes you nothing; it was', 'here first.                   ']
  - Assert 1: True
"""

class Solution:
 
    def fullJustify1(self, words, maxWidth):

        # get list of each word len
        word_lengths = [len(word) for word in words]

        # get list of words index per each line
        lines, spaces = self.get_lines_spaces(word_lengths, maxWidth)

        # get list of space per each word per each line
        word_spaces = self.get_word_space(lines, spaces, words)

        # generate return value
        res = []
        for i, line in enumerate(lines):
            tmp = []
            for j, word_idx in enumerate(line):
                s = ' ' * word_spaces[i][j]
                tmp.append(f"{words[word_idx]}{s}")
            res.append("".join(tmp))
        return res

    def get_lines_spaces(self, word_lengths, maxWidth):
        lines, line, spaces, space, width = [], [], [], maxWidth, 0
        for i, wlen in enumerate(word_lengths):
            width += (wlen+1)
            if width > maxWidth+1:
                lines.append(line)
                spaces.append(space)
                space, width, line = maxWidth, wlen+1, []
            space -= wlen
            line.append(i)
        if line: 
            lines.append(line)
            spaces.append(space)

        return lines, spaces

    def get_word_space(self, lines, spaces, words):
        last_idx = len(lines)-1
        word_spaces = []
        for i, line in enumerate(lines):
            word_cnt   = len(line)
            space      = spaces[i]

            if i == last_idx:
                space_list = [1]*word_cnt
                space_list[-1] = space - word_cnt + 1
            else:
                k = word_cnt - 1
                space_list = [0]*word_cnt
                for i in range(word_cnt-1, -1, -1):
                    if i == word_cnt-1: continue
                    w = space // k if k > 0 else space
                    space_list[i] = w
                    space -= w
                    k     -= 1
                if word_cnt == 1: space_list[0] = space
            word_spaces.append(space_list)
        return word_spaces


    # 19/27 passed
    def fullJustify2(self, words, maxWidth):
        """
        - res : []
        - get list of each word length: l[]
        - get list of words per each line: s[]
          * len(word) <= maxWidth
          * prev len(word) + 1 + cur len(word) <= maxWidth
          * get list of space per each line : space
        - generate res
          * not last line
            - calculate each space // len(s)
          * last line
            - f"{w:maxWidth}"
        
        """
        # Get list of each word length
        word_lengths = [len(w) for w in words]
        
        # Get list of words and space per each line
        width, line, space = 0, [], maxWidth
        lines, spaces = [], []
        for i, word_len in enumerate(word_lengths):
            width += word_len+1
            if width-1 > maxWidth:
                spaces.append(space)
                lines.append(line)
                line = []
                width, space = word_len+1, maxWidth
            space -= word_len
            line.append(i)
        if width > 0:
            spaces.append(space)
            lines.append(line)

        # Generate res
        res, last_idx = [], len(lines)-1
        for i, line in enumerate(lines):
            sline, n = [], len(line)
            space = spaces[i]
            if i == last_idx or n == 1:
                for j, word_idx in enumerate(line):
                    if   j == n-1:  # last   index
                        sline.append(f"{words[word_idx]}{' '*space}")
                    else:
                        space -= 1
                        sline.append(f"{words[word_idx]} ")
            else:
                #print(f"word_cnt:{n}, space:{space}")
                mspace, rspace = self.get_space(space, n)
                for j, word_idx in enumerate(line):
                    if   j == n-1:  # last   index
                        sline.append(f"{words[word_idx]}")
                    elif j == n-2:  # last-2 index
                        sline.append(f"{words[word_idx]}{rspace}")
                    else:
                        sline.append(f"{words[word_idx]}{mspace}")
            res.append("".join(sline))
        return res
                                     
    def get_space(self, space, word_cnt):
        m, r = 0, 0
        if word_cnt <= 2: return space * " ", space * " "
        
        n = word_cnt - 1
        mod = space % n
        
        if mod == 0:
            m = r = space // n
        else:
            r = space // n
            m = (space-r) // (n-1)
        return m*" ", r*" "


    def test(self):
        test_cases = [
            { "maxWidth"   : 16,
              "words"      : ["This", "is", "an", "example", "of", "text", "justification."],
              "expectation": ["This    is    an","example  of text","justification.  "]
            },
            { "maxWidth"   : 16,
              "words"      : ["What","must","be","acknowledgment","shall","be"],
              "expectation": ["What   must   be","acknowledgment  ","shall be        "]
            },
            { "maxWidth"   : 20,
              "words"      : ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
              "expectation": ["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "]
            },
            { "maxWidth"   : 16,
              "words"      : ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"],
              "expectation": ["ask   not   what","your country can","do  for  you ask","what  you can do","for your country"]
            },
            { "maxWidth"   : 30,
              "words"      : ["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."],
              "expectation": ["Don't  go  around  saying  the","world  owes  you a living; the","world owes you nothing; it was","here first.                   "]
            }
        ]
        for i, t in enumerate(test_cases, 1): 
            maxWidth, words, expectation = t['maxWidth'], t['words'], t['expectation']
            print(f"\nTest Case {i}. maxwidth:{maxWidth}, words:{words}")
            res1 = self.fullJustify1(words, maxWidth)
            #res2 = self.fullJustify2(words, maxWidth)
            print(f"  - Result 1: {res1}")
            #print(f"  - Result 2: {res2}")
            print(f"  - Expected: {expectation}")
            print(f"  - Assert 1: {res1 == expectation}")
            #print(f"  - Assert 2: {res2 == expectation}")


if __name__ == '__main__':
    Solution().test()

