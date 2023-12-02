class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = {}
        for i in chars:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        
        count = 0
        for i in words:
            check = True
            dic2 = dic.copy()
            for j in i:
                if j in dic2:
                    if dic2[j] <=0:
                        check = False
                        break
                    else:
                        dic2[j] -=1
                else:
                    check = False
                    break
            if check:
                count += len(i)
        return count

