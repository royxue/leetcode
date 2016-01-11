class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = sum(map(operator.eq, secret, guess))
        b = sum([min(secret.count(i), guess.count(i)) for i in '0123456789'])
        
        return str(a)+'A'+str(b-a)+'B'
            