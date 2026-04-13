class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        fq = count.most_common()

        fqList = []
        for i in range(k):
            x = fq[i][0]
            fqList.append(x)

        return fqList

        

                
            
