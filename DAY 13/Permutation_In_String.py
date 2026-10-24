class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count={}
        for s in s1:
            s1_count[s]=s1_count.get(s,0)+1
        s2_count={}
        for w in s2[:len(s1)]:
            s2_count[w]=s2_count.get(w,0)+1
        if s1_count==s2_count:
            return True

        for i in range(len(s1),len(s2)):
            s2_count[s2[i]]= s2_count.get(s2[i],0)+1
            old=s2[i-len(s1)]
            s2_count[old]-=1
            if s2_count[old]==0:
                del s2_count[old]

            if s1_count==s2_count:
                return True

        return False
