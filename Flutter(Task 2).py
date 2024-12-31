class Solution:
    def isPalindrome(self, x):
        
        if x < 0:
            return False
        
        
        original_value = x
        reversed_num = 0
        
        
        while x > 0:
            digit = x % 10  
            reversed_num = reversed_num * 10 + digit  
            x //= 10  
        
        
        return original_value == reversed_num


case_1 = 121  
solution = Solution()
output = solution.isPalindrome(case_1)
print(output)  
