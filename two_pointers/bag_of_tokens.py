from collections import deque

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = deque(sorted(tokens))
        score = 0
        while tokens:
            if power >= tokens[0]:
                score += 1
                power -= tokens[0]
                tokens.popleft()
            elif score > 0 and len(tokens) > 1:
                power += tokens.pop()
                score -= 1
            else:
                break
        return score
