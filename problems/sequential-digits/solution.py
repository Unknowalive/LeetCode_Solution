class Solution(object):
    def sequentialDigits(self, low, high):
        result = []
        sample = "123456789"
        
        len_low = len(str(low))
        len_high = len(str(high))
        
        for length in range(len_low, len_high + 1):
            for i in range(9 - length + 1):
                num = int(sample[i : i + length])
                if low <= num <= high:
                    result.append(num)
        
        return result
