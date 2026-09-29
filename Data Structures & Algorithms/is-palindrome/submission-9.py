class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = "".join(char for char in s.lower() if char.isalnum())
        right = (len(s) - 1);
        left = 0;
        while(right >= left):
            if(s[right] != s[left]):
                return False;
            right = right - 1;
            left = left + 1;
        return True;