class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s.lower()) # 대문자 소문자 구분 없이 진행을 위해 전부 소문자로 변경
        
        # list 3개 생성 
        # -> 1. 입력받은 값 정리해서 넣음(비교군) 2. 1과 동일한 값이나 reverse위해 pop하기 위해 생성 3. reverse된 값 넣을 list
        check = [] # 기준에 맞는 값만 list에 넣어서 사용
        copy = [] 
        
        for i in s :
            i = str(i) # 입력값이 unicode 값이라 str로 변경필요
            if ((i >= 'a' and i <= 'z') or (i >= '0' and i <= '9')) : # 알파벳, 숫자 제외 값 제거를 위한 조건
                check.append(i)
                copy.append(i)
        compare = []
        
        for i in range(0, len(check)):
            compare.append(check.pop()) #pop의 빅오값은 O(1)

        if(copy == compare):
            return True
        else:
            return False