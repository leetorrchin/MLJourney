class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if (len(strs) == 0):
            return prefix

        for i in xrange(len(min(strs))):
            letter = strs[0][i]
            if all(word[i] == letter for word in strs):
                prefix += letter
            else:
                break
        return prefix
            

                

