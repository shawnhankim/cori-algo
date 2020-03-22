"""
208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

Expected Results:

1. Test Case: {'func': ['Trie', 'insert', 'search', 'search', 'startsWith', 'insert', 'search'], 'data': [[], ['apple'], ['apple'], ['app'], ['app'], ['app'], ['app']], 'expectation': ['null', 'null', 'true', 'false', 'true', 'null', 'true']}
   - Result : ['null', 'null', 'true', 'false', 'true', 'null', 'true']
   - Assert expectation == results: True
   - Trie :
           0:a (0)   1:p (0)   2:p (1)   3:l (0)   4:e (1)

2. Test Case: {'func': ['Trie', 'insert', 'insert', 'insert', 'insert', 'insert', 'insert', 'search', 'search', 'search', 'search', 'search', 'search', 'search', 'search', 'search', 'startsWith', 'startsWith', 'startsWith', 'startsWith', 'startsWith', 'startsWith', 'startsWith', 'startsWith', 'startsWith'], 'data': [[], ['app'], ['apple'], ['beer'], ['add'], ['jam'], ['rental'], ['apps'], ['app'], ['ad'], ['applepie'], ['rest'], ['jan'], ['rent'], ['beer'], ['jam'], ['apps'], ['app'], ['ad'], ['applepie'], ['rest'], ['jan'], ['rent'], ['beer'], ['jam']], 'expectation': ['null', 'null', 'null', 'null', 'null', 'null', 'null', 'false', 'true', 'false', 'false', 'false', 'false', 'false', 'true', 'true', 'false', 'true', 'true', 'false', 'false', 'false', 'true', 'true', 'true']}
   - Result : ['null', 'null', 'null', 'null', 'null', 'null', 'null', 'false', 'true', 'false', 'false', 'false', 'false', 'false', 'true', 'true', 'false', 'true', 'true', 'false', 'false', 'false', 'true', 'true', 'true']
   - Assert expectation == results: True
   - Trie :
           0:a (0)   1:p (0)   2:p (1)   3:l (0)   4:e (1)   1:d (0)   2:d (1)
           0:b (0)   1:e (0)   2:e (0)   3:r (1)
           0:j (0)   1:a (0)   2:m (1)
           0:r (0)   1:e (0)   2:n (0)   3:t (0)   4:a (0)   5:l (1)

"""

from collections import defaultdict

class TreeNode:
    def __init__(self):
        self.child = defaultdict(TreeNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.child[c]
        node.is_word = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.child: return False
            node = node.child[c]
        return node.is_word

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.child: return False
            node = node.child[c]
        return True


def print_trie(trie, depth=0):
    root = trie.root
    print_trie_helper(root, depth)


def print_trie_helper(root, depth=0):
    if depth == 0: print("   - Trie :")
    for c in root.child:
        node = root.child[c]
        if depth == 0: print("\n     ", end="")
        print(f"{depth}:{c} ({node.is_word:1})  ", end="")
        print_trie_helper(node, depth+1)


class Trie1: # 14/15 test cases are passed

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children, self.exist = defaultdict(), False
 
       
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        word_len = len(word)
        if word_len == 0: return
        c = word[0]

        if c not in self.children:
            self.children[c] = Trie()
        if word_len == 1: self.exist = True
        else: self.children[c].insert(word[1:])


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.find(word)
    
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.find(prefix, is_prefix=True)


    def find(self, word, is_prefix=False):
        word_len = len(word)
        if word_len > 0:
            c = word[0]
            if c not in self.children: return False
            if word_len == 1:
                if   is_prefix : return True
                elif self.exist: return True
            else:
                return self.children[c].find(word[1:], is_prefix)
        return False


def print_trie1(trie, depth=0):
    if depth == 0: print("   - Trie : ", end="")
    for c in trie.children:
        if depth == 0: print("\n           ", end="")
        print(f"{depth}:{c} ({trie.exist:1})", end="   ")
        if trie.children[c]: print_trie(trie.children[c], depth+1)


def test():
    test_cases = [
        {
          "func": ["Trie","insert","search","search","startsWith","insert","search"],
          "data": [[],["apple"],["apple"],["app"],["app"],["app"],["app"]],
          "expectation": ["null","null","true","false","true","null","true"]
        },
        { "func": ["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"],
          "data": [[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]],
          "expectation": ["null","null","null","null","null","null","null","false","true","false","false","false","false","false","true","true","false","true","true","false","false","false","true","true","true"]
        }
    ]
    for i, test_case in enumerate(test_cases, 1):
        trie = Trie()
        func, data, expectation = test_case["func"], test_case["data"], test_case["expectation"]
        results = []
        print(f"\n{i}. Test Case: {test_case}")
        for j in range(len(func)):
            ret, word = None, data[j][0] if data[j] else ''
            
            if   func[j] == "insert"    :       trie.insert(word)
            elif func[j] == "search"    : ret = trie.search(word)
            elif func[j] == "startsWith": ret = trie.startsWith(word)
            #print(f"{func[j]} : {word}")
            if ret is None: results.append("null")
            else          : results.append("true" if ret else "false")
        print(f"   - Result : {results}")
        print(f"   - Assert expectation == results: {expectation == results}")
        print_trie(trie)
        print()


if __name__ == '__main__':
    test()


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

"""
["Trie","insert","insert","search","search","search","insert","search","insert","insert","insert","insert","search","search","search","search","search","search","insert","search","search","insert","search","search","insert","search","insert","insert","insert","search","insert","search","insert","search","insert","search","insert","insert","search","search","search","search","insert","insert","insert","insert","search","insert","search","insert","insert","search","insert","insert","search","search","insert","search","insert","search","insert","insert","search","search","search","insert","search","search","search","search","search","insert","insert","insert","search","search","insert","search","search","insert","insert","search","search","insert","search","insert","search","insert","search","search","search","insert","search","insert","search","search","search","search","search","insert","insert","search","search","search","search","search","insert","insert","insert","search","insert","i
[[],["nemathelminth"],["entracte"],["nemathelminth"],["entracte"],["spittlestaff"],["spittlestaff"],["hematocrit"],["hematocrit"],["inachid"],["phthalan"],["mev"],["inachid"],["phthalan"],["mev"],["hematoid"],["kingmaking"],["brent"],["hematoid"],["epollicate"],["allegiant"],["kingmaking"],["zomotherapeutic"],["disinvolve"],["brent"],["prefashion"],["epollicate"],["allegiant"],["zomotherapeutic"],["vangeli"],["disinvolve"],["pucklike"],["prefashion"],["lysidine"],["vangeli"],["stingily"],["pucklike"],["lysidine"],["morong"],["counterclockwise"],["deemstership"],["turban"],["stingily"],["morong"],["counterclockwise"],["deemstership"],["impermeableness"],["turban"],["inattentively"],["impermeableness"],["inattentively"],["bonewort"],["bonewort"],["zincographer"],["zincographer"],["ultrasubtle"],["ultrasubtle"],["facingly"],["facingly"],["forchase"],["forchase"],["featherwing"],["featherwing"],["production"],["misesteem"],["production"],["chrysoaristocracy"],["nidorosity"],["shurf"],["gau
"""
