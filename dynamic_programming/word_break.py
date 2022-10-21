class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache()
        def dfs(word):
            if not word:
                return True
            for i in wordDict:
                if word.startswith(i):
                    if dfs(word[len(i) :]):
                        return True
            return False

        return dfs(s)
