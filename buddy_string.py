class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool: # type: ignore
        if s[0] == goal[0] and s[0] == goal[1]:
            return True
        if s[0] == goal[0] and s[1] == goal[1]:
            return False

        if len(s) > 2:
            return False

        swapped = s[1] + s[0]
        print(swapped)
        if swapped[0] == goal[0]  and swapped[1] == goal[1]:
            # print("swapped")
            return True
        
        else:
            return False # type: ignore
            print("False")

s = Solution()
print(s.buddyStrings('ab', 'ba'))
print(s.buddyStrings('ab', 'ab'))
print(s.buddyStrings('aa', 'aa'))
print(s.buddyStrings('abcd', 'bacd'))
print(s.buddyStrings('abab', 'abab'))










#testcase1 -> ab,ba -> true done
#testcase2 -> ab,ab -> false done
#testcase3 -> aa,aa -> true done
#testcase4 -> abcd,badc -> false done
#testcase5 -> abab,abab -> True

# abab , abab -> baab != abab