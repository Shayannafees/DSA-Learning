
class Solution:
    def replaceWords(self, dictionary: list, sentence: str):
        s = sentence.split(' ')
        a = []
        dictionary.sort(key=len) # type: ignore
        

        for i in s:
            for j in dictionary:
                if i[:len(j)] == j:
                    a.append(j)
                    break
            
            else:
                a.append(i)
        return ' '.join(a)           
s = Solution()
print(s.replaceWords(['cat','rat','bat'], 'the cattle was rattled by the bat'))
print(s.replaceWords(["a","b","c"], 'aadsfasf absbs bbab cadsfafs'))