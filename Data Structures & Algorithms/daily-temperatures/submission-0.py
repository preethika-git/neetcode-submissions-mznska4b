class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        
        if len(temperatures) == 1: return [0]

        for i in range(len(temperatures)-1):
            r = i+1
            while r < len(temperatures):
                if temperatures[i] < temperatures[r]:
                    a = r-i
                    ans.append(a)
                    break
                elif r == len(temperatures)-1:
                    ans.append(0)
                    break
                else:
                    r+=1

        ans.append(0)
        return ans

            
