class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for p in details:    
            age = int(p[11])*10 + int(p[12])
            if age > 60:
                ans+=1
        return ans

