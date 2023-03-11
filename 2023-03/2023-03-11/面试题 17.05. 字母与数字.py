# -*- coding: utf-8 -*-
"""
# @Time    : 2023/3/11 12:33 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 面试题 17.05. 字母与数字.py
"""
from typing import List
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        res = 0
        cnt = 0
        index = 0
        hashdict = {0:0}
        for i, s in enumerate(array):
            i += 1
            n = 1 if s.isalpha() else -1
            cnt += n
            if cnt in hashdict.keys():
                if res <= i-hashdict[cnt]:
                    res = i-hashdict[cnt]
                    index = hashdict[cnt]
            else:
                hashdict[cnt] = i
        if index==0:
            index+=1
        return array[index-1:index-1+res]

print(Solution().findLongestSubarray(["42","10","O","t","y","p","g","B","96","H","5","v","P","52","25","96",
                                      "b","L","Y","z","d","52","3","v","71","J","A","0","v","51","E","k","H",
                                      "96","21","W","59","I","V","s","59","w","X","33","29","H","32","51","f",
                                      "i","58","56","66","90","F","10","93","53","85","28","78","d","67","81",
                                      "T","K","S","l","L","Z","j","5","R","b","44","R","h","B","30","63","z",
                                      "75","60","m","61","a","5","S","Z","D","2","A","W","k","84","44","96","96","y","M"]))