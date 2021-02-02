import string


class Solution:
    def numDecodings(self, s):
        a_zdict = {}
        i = 1
        for ch in string.ascii_uppercase:
            a_zdict[str(i)] = ch
            i += 1

        if len(s) == 1:
            if s == '0':
                return 0
            return 1

        """
        len is greater than 2
        """
        note = []
        if s[0] == '0':
            return 0
        else:
            if s[0:2] == "10" or int(s[0:2]) > 26:
                note = [1, 1]
            else:
                note = [1, 2]

        print(note)
        if len(s) > 2:
            for i in range(2, len(s)):
                print(s[i-1:i+1])
                if s[i-1:i+1] in a_zdict:
                    if s[i:i+1] == '0':
                        note.append(note[i-2])
                    else:
                        note.append(note[i-1] + note[i-2])
                else:
                    if s[i-1:i+1] == '00' or (int(s[i-1:i+1]) > 26 and s[i:i+1]) == '0':
                        return 0
                    else:
                        note.append(note[i-1])
        print(note)
        return note[-1]


obj = Solution()

print(obj.numDecodings('1201234'))
