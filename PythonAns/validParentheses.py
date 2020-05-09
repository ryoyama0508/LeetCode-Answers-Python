class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)

            else:
                if len(stack) == 0:
                    return False
                if bracket == ")":
                    if stack.pop(len(stack)-1) != "(":
                        return False

                if bracket == "}":
                    if stack.pop(len(stack) - 1) != "{":
                        return False

                if bracket == "]":
                    if stack.pop(len(stack) - 1) != "[":
                        return False

        if len(stack) != 0:
            return False

        return True
