class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        word_list = []
        answer = []
        
        for words in strs:
            lis = []
            for alphabet in words:
                lis.append(alphabet)
            word_list.append(sorted(lis))
        
        while (len(word_list) > 0):
            if len(strs) < 1: break
            same = []
            same.append(strs.pop())
            a = word_list.pop()
            if word_list.count(a) > 0:
                for i in range(0, word_list.count(a)):
                    # print(len(strs), len(word_list))
                    same.append(strs.pop(word_list.index(a)))
                    word_list.pop(word_list.index(a))
            answer.append(same)
        
        return answer
            