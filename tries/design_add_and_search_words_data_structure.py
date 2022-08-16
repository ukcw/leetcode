class WordNode:
    def __init__(self):
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.dic = WordNode()

    def addWord(self, word: str) -> None:
        node = self.dic

        for w in word:
            if w not in node.children:
                node.children[w] = WordNode()
            node = node.children[w]
        node.children['-'] = True

    def search(self, word: str) -> bool:
        def fd(node, word):
            if not word:
                return '-' in node.children
            else:
                if word[0] == ".":
                    for child in node.children.keys():
                        if child != '-' and fd(node.children[child], word[1:]):
                            return True
                    return False
                elif word[0] not in node.children:
                    return False
                else:
                    return fd(node.children[word[0]], word[1:])
        return fd(self.dic, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
