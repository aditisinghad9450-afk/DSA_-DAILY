class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        count={}
        for c in p:
            count[c]=count.get(c,0)+1
        result=[]
        w_count={}
        for w in s[:len(p)]:
            w_count[w]=w_count.get(w,0)+1
        if count==w_count:
            result.append(0)
        for i in range(len(p),len(s)):
            w_count[s[i]]= w_count.get(s[i],0)+1
            old=s[i-len(p)]
            w_count[old]-=1
            if w_count[old]==0:
                del w_count[old]

            if count== w_count:
                result.append(i-len(p)+1)

        return result    









        
