class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        li = []
        for index, word in enumerate(words):
            if x in word:
                li.append(index)
        return li
