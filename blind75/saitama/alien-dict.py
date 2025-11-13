from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #each word lookup and build a numbering of each char
        # hello -> [1,8,2,2,15]
        # leetcode -> [2,8,8,]
        # alpa_dict = {'h': 0, 'l': 1...}
        alpha_dict = {ch: i for i, ch in enumerate(order)}

        #compare for order
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]

            #check each char
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    #check for char rank
                    if alpha_dict[w1[j]] > alpha_dict[w2[j]]:
                        return False
                    break
            if len(w1) > len(w2): #canned, can
                return False
        
        return True
    

#input:
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(Solution().isAlienSorted(words, order))