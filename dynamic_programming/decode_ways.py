class Solution:
    def numDecodings(self, s: str) -> int:
        """
        let i be the current index
        cases:
        if the decoding reaches the end of the string:
            it means that we have found a successful decoding
            len(s) = 1

        if the current number is 0:
            no decodings are available
            this means that we are not able to proceed to the end of the string

        else:
            decodings will be available for at least
            s[i+1]

            if the current number is 1
            and there are at least two characters left:
                decodings will be available for both
                s[i+1]
                s[i+2]

            if the current number is 2
            and there are at least two characters left
            and the s[i+1] number is less than or equal to 6:
                decodings will be available for both
                s[i+1]
                s[i+2]
        """
        memo = {len(s): 1}

        def isValidNumber(num: str) -> bool:
            num = int(num)
            if num == 0:
                return False
            return True

        def isValidPair(num1: str, num2: str) -> bool:
            num1 = int(num1)
            num2 = int(num2)

            if num1 == 1:
                return True
            elif num1 == 2 and num2 < 7:
                return True
            else:
                return False

        for i in range(len(s) - 1, -1, -1):
            if not isValidNumber(s[i]):
                memo[i] = 0
                continue
            # if isValidNumber(s[i]):
            memo[i] = memo[i + 1]

            if i < len(s) - 1 and isValidPair(s[i], s[i + 1]):
                memo[i] += memo[i + 2]

        return memo[0]
