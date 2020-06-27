class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        par = ["("]*n
        par += [")"]*n
        oriLen = len(par)
        return self.back(par, 0, "", [], [], oriLen)

    def back(self, par, i, one, ret, stack, oriLen):
        if i == oriLen and len(stack) == 0:
            print("here")
            ret.append(one)
            return

        for j in range(0, len(par)):
            if par[j] == "(":
                stack.append(par[j])
            else:
                if stack:  # if empty_list will evaluate as false.
                    if stack[-1] == "(":
                        stack.pop()
                else:
                    stack.append(par[j])

            one += par[j]
            newPar = []
            if j == 0:
                newPar = par[1:]
            elif j == len(par)-1:
                newPar = par[:-1]
            else:
                newPar = par[:j]+par[j+1:]

            print(one, i, stack)
            self.back(newPar, i+1, one, ret, stack, oriLen)
            one = one[:-1]
            print(one)

        return ret
