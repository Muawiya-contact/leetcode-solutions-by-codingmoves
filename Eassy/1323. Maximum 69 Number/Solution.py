class Solution:
    def maximum69Number(self,num):
        n = str(num)
        li = []
        for i in range(0,len(n)):
            li.append(n[i])
        for i in range(0,len(li)):
                if li[i] == '6':
                    li[i] = '9'
                    break
        n = ''.join(li)
             
        return int(n)
obj = Solution()
print(obj.maximum69Number(666))
