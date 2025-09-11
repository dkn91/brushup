class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        number = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                number = 10 * number + int(abbr[j])
                if number <= 0:
                    break
                j += 1
            else:
                i += number
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
                number = 0
        i += number
        return i == len(word) and j == len(abbr)

obj = Solution()
print(obj.validWordAbbreviation(word = "internationalization", abbr = "i12iz4n"))