# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/26 2:51 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 1255. 得分最高的单词集合.py
"""
from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        max_score = 0
        text_list = []
        for index, word in enumerate(words):
            text = ''
            i = index
            while i < len(words):
                text += words[i]
                i += 1
                text_list.append(text)
        for texts in text_list:
            s = 0
            for j in texts:
                if texts.count(j) <= letters.count(j):
                    s += score[ord(j)-ord('a')]
                else:
                    s = 0
                    break
            max_score = max(max_score, s)
        return max_score

Solution().maxScoreWords(["dog","cat","dad","good"],["a","a","c","d","d","d","g","o","o"],[1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])