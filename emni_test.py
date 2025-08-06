class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            return True
        else:
            return False

       

s1='shakil'
s2 ='khan'
s = Solution()
print(s.isAnagram(s1,s2))
