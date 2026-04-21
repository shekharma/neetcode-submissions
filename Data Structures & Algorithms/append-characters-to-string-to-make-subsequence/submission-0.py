class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        if len(s)==1 and s[0] not in t:
            return len(t)

        sp=0
        tp=0
        
        while sp< len(s) and tp < len(t):
            if s[sp]==t[tp]:
                sp+=1
                tp+=1
            else:
                sp+=1
        return len(t)-tp
        