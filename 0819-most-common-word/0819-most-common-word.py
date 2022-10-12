class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        check = []
        dic = {}
        
        paragraph = paragraph.lower()
        
        for a in paragraph:
            if(a<'a' or a>'z'):
                if(a!=' '):
                    paragraph = paragraph.replace(a, ' ')
        
        check = paragraph.split(' ')
        
        print(check)
                
        for a in check:
            try:
                x = banned.index(a)
                continue
            except:
                if(a!=""):
                    dic[a] = check.count(a)
        
        return max(dic, key = dic.get)
            