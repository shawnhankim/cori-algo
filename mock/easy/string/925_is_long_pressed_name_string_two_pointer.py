"""
925. Long Pressed Name

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.

Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.

"""

from collections impåort defaultdict

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_list = self._get_list(name)
        type_list = self._get_list(typed)
        #self._print_list(name_list)
        #self._print_list(type_list)
        
        name_len, type_len = len(name_list), len(type_list)
        if name_len != type_len: return False
        for i in range(name_len):
            nc, nv = name_list[i]
            tc, tv = type_list[i]
            if nc != tc or (nc == tc and nv > tv): return False
        return True
    
    def _print_list(self, l1):
        print("[", end=" ")
        for l in l1:
            c, v = l
            print(f"({c}:{v})", end=" ")
        print("]")
        
    def _get_list(self, string):
        res, hs, prev, last = [], {}, '', ''
        
        for i, c in enumerate(string):
            if c not in hs: hs[c]  = 1
            else          : hs[c] += 1
            if prev != c and i != 0:
                res.append((prev, hs[prev]))
                hs[prev] = 0
            prev = c
        
        if prev not in hs:
            res.append((prev, hs[prev]))
            hs[prev] = 0
        
        return res

"""
"kpufanyrqqmtgxhyycltlnusyeyyqygwupcaagtkuqkwamvdsi"
"kpuufaanyrqqqmttggxxhyyyycclttllnusyeyqqyggwuuppccaaaggtkkuuqkwwamvvddsii"

"kpu fa nyrqq mt g x hyy  c lt l nusyeyy qygwupcaagtkuqkwamvdsi"
"kpuufaanyrqqqmttggxxhyyyycclttllnusyey  qqyggwuuppccaaaggtkkuuqkwwamvvddsii"

"""        
