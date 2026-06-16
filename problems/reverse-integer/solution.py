class Solution(object):
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        
        rev = int(str(x_abs)[::-1]) * sign
        
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev
