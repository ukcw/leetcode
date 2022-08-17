from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word):
        node = self
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.word = True

class TLESolution: # this solution hit TLE
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()

        for w in words:
            self.root.addWord(w)

        MAX_ROW_LEN = len(board)
        MAX_COL_LEN = len(board[0])

        res = set()
        visited = set()

        def searchWord(r, c, node, word):
            if r < 0 \
            or r >= MAX_ROW_LEN \
            or c < 0 \
            or c >= MAX_COL_LEN \
            or (r, c) in visited \
            or board[r][c] not in node.children:
                return None

            visited.add((r,c))
            if node.children[board[r][c]].word:
                res.add(word + board[r][c])
            searchWord(r + 1, c, node.children[board[r][c]], word + board[r][c])
            searchWord(r - 1, c, node.children[board[r][c]], word + board[r][c])
            searchWord(r, c + 1, node.children[board[r][c]], word + board[r][c])
            searchWord(r, c - 1, node.children[board[r][c]], word + board[r][c])
            visited.remove((r,c))

        for i in range(MAX_ROW_LEN):
            for j in range(MAX_COL_LEN):
                searchWord(i, j, self.root, "")

        return list(res)

class NoTLESolution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()

        for w in words:
            self.root.addWord(w)

        MAX_ROW_LEN = len(board)
        MAX_COL_LEN = len(board[0])
        MAX_WORDS = len(words)

        res = set()

        def searchWord(r, c, node, word):
            if board[r][c] == '#' or board[r][c] not in node.children or len(res) == MAX_WORDS:
                return None

            tmp = board[r][c]
            board[r][c] = '#'
            if node.children[tmp].word:
                res.add(word + tmp)

            if r + 1 < MAX_ROW_LEN:
                searchWord(r + 1, c, node.children[tmp], word + tmp)
            if r - 1 >= 0:
                searchWord(r - 1, c, node.children[tmp], word + tmp)
            if c + 1 < MAX_COL_LEN:
                searchWord(r, c + 1, node.children[tmp], word + tmp)
            if c - 1 >= 0:
                searchWord(r, c - 1, node.children[tmp], word + tmp)
            board[r][c] = tmp

        for i in range(MAX_ROW_LEN):
            for j in range(MAX_COL_LEN):
                searchWord(i, j, self.root, "")
                if len(res) == MAX_WORDS:
                    return list(res)

        return list(res)
