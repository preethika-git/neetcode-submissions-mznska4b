class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for l in range(len(numbers)-1):
            r = l + 1

            while r < len(numbers) and l < r:
                total = numbers[l] + numbers[r]

                if total == target:
                    return [l+1, r+1]
                
                else:
                    if r < len(numbers)-2 and numbers[r] == numbers[r+1]:
                        r+=1
                    r+=1


