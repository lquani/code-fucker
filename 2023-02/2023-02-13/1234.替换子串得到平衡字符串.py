# -*- coding: utf-8 -*-
"""
# @Time    : 2023/2/13 9:19 下午
# @Author  : HOY
# @Email   : 893422529@qq.com
# @File    : 1234.替换子串得到平衡字符串.py
"""

"""
超时代码
"""
class Solution:
    def balancedString(self, s: str) -> int:
        avg = len(s)//4
        words = {'Q': s.count('Q'), 'W': s.count('W'), 'E': s.count('E'), 'R': s.count('R')}
        count = 0
        for word in words.keys():
            print(words[word])
            if words[word]>avg:
                count+=words[word]-avg
        if count==0:
            return 0
        cnt = count
        while count<len(s):
            for i in range(len(s)-count+1):
                # print(i)
                tmp = 0
                strings = s[i:i+count]
                for word in words.keys():
                    if words[word] > avg:
                        tmp+=min(strings.count(word),words[word]-avg)
                if tmp>=cnt:
                    print(strings)
                    return count
            count+=1
        return count

print(Solution().balancedString('QWER'))
