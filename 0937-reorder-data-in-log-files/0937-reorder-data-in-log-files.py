class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig = []
        let = []
        let_check = ()
        ans = []
        
        for i in logs:
            temp = i.split(' ')
            try : 
                x = int(temp[1])
                dig.append(i)
            except:
                let.append(temp)
        
        let.sort(key = lambda x: (x[1:] , x[0]))
        
        for i in let:
            ans.append(" ".join(i))
        
        for i in dig:
            ans.append(i)
            
        return ans