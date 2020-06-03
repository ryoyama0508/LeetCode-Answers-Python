class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        A = B = ''
        if len(a) < len(b):
            A += '0' * (len(b) - len(a))
        else:
            B += '0' * (len(a) - len(b))

        A += a
        B += b

        i = len(A)-1
        c = '0'
        l = [0] * (len(A))
        while i > -1:
            if A[i] == '0' and B[i] == '0':
                if c == '1':
                    l[i] = '1'
                else:
                    l[i] = '0'
                c = '0'
            elif (A[i] == '0' and B[i] == '1') or (A[i] == '1' and B[i] == '0'):
                if c == '1':
                    l[i] = '0'
                    c = '1'
                else:
                    l[i] = '1'
                    c = 0
            else:
                if c == '1':
                    l[i] = '1'
                else:
                    l[i] = '0'
                c = '1'
            i -= 1

        if c == '1':
            l.insert(0, '1')

        ret = ''
        for c in l:
            ret += c

        return ret
