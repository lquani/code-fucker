# 时间复杂度应该是O(n)，空间复杂度应该也是O(n),用了一个nums
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n<10:
            return -1
        nums = [] # nums记录n里从后遍历的数字，单调递增 如321 ->nums = [1,2,3]
        count = 0
        ans = 0
        head = n
        while head:
            res = head%10
            head //= 10
            count += 1
            if head==0 and res>=nums[-1]: # head为0但是res比nums里的数都大，则终止，比如321
                return -1
            if nums and res<nums[-1]: 
                # 是否比nums中最大值小，小就停止，然后寻找nums里比res大的数中的最小值，并跟其还位置，作为后count个数的头，剩余nums里的数从小到大排列为后count-1的数
                nums.append(res)
                m = len(nums)
                for i in range(m-1):
                    if nums[i]>nums[-1]:
                        nums[i],nums[-1] = nums[-1],nums[i] # 交换位置，找到nums中比res大的数中的最小值
                        break   
                break 
            nums.append(res)
        cur = nums.pop()
        for num in nums:
            cur = cur*10+num 
        ans = head*(10**count)+cur
        return ans if ans<=2**31-1 else -1 # 限制不超过32位整数