class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {2: "abc" , 3: "def" , 4: "ghi" , 5: "jkl" , 6: "mno" , 7: "pqrs", 8: "tuv" , 9: "wxyz"}
        res = []
        digits = [int(_) for _ in digits] 
        i = 0
        while i < len(digits):
            if i == 0:
                res.extend([_ for _ in dict[digits[i]]])
                i += 1
                continue
            dummy = []
            for j in res:
                dummy.extend([j + _ for _ in dict[digits[i]]])
            res = dummy
            i+=1
        return res
            
