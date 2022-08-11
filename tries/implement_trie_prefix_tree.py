class TrieNode:
    def __init__(self):
        self.tree = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.tree:
                node.tree[w] = TrieNode()
            node = node.tree[w]
        node.tree['-'] = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.tree:
                return False
            node = node.tree[w]
        return '-' in node.tree

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w not in node.tree:
                return False
            node = node.tree[w]
        return True

class RecursiveImplTrie:

    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        def ins(root, word):
            if not word:
                return None
            elif not word[1:]:
                if word[0] not in root.tree:
                     root.tree[word[0]] = TrieNode()
                root.tree[word[0]].tree['-'] = True
                return None
            else:
                if word[0] not in root.tree:
                     root.tree[word[0]] = TrieNode()
                ins(root.tree[word[0]], word[1:])
        return ins(self.root, word)

    def search(self, word: str) -> bool:
        def fd(root, word):
            if not word:
                return '-' in root.tree
            elif word[0] in root.tree:
                return fd(root.tree[word[0]], word[1:])
            else:
                return False
        return fd(self.root, word)

    def startsWith(self, prefix: str) -> bool:
        def sw(root, sub):
            if not root:
                return False
            if not sub:
                return True
            if sub[0] not in root.tree:
                return False
            else:
                return sw(root.tree[sub[0]], sub[1:])
        return sw(self.root, prefix)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
