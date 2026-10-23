class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left=0
        best=0
        basket={}
        for right in range(len(fruits)):
            basket[fruits[right]]=basket.get(fruits[right],0)+1

            while len(basket)>2:
                basket[fruits[left]]-=1
                if basket[fruits[left]]==0:
                    del basket[fruits[left]]
            
                left+=1
            best=max(best,right-left+1)


        return best    

        
        
