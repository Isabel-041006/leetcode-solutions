class Solution(object):
    def mergeAlternately(self, word1, word2):
        min_len = min(len(word1), len(word2))
        l_rlt = []

        for i in range(min_len):
            l_rlt.extend([word1[i], word2[i]])

        l_rlt.append(word1[min_len:])
        l_rlt.append(word2[min_len:])

        return "".join(l_rlt)