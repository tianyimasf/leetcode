class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphanumeric = list("abcdefghijklmnopqrstuvwxyz1234567890")
        l = [i.lower() for i in list(s) if i.lower() in alphanumeric]
        for i in range(int(len(l)/2)):
            if l[i] != l[-i-1]:
                return False
        return True