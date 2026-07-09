from collections import defaultdict
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        e = defaultdict(int)
        
        for email in emails:
            local, domain = email.split("@",1)
            local = local.split("+",1)[0].replace(".","")
            e[tuple(local+domain)]+=1
        
        return len(e.keys())
