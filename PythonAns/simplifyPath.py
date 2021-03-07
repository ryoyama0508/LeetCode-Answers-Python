class Solution:
    def simplifyPath(self, path: str) -> str:
        i = 0
        stack = []
        while i < len(path):
            if path[i] != "/":
                folder_name = ""
                while path[i] != "/":
                    folder_name += path[i]
                    i += 1
                    if i > len(path) - 1:
                        break

                if folder_name == ".":
                    pass
                elif folder_name == "..":
                    try:
                        stack.pop()
                    except:
                        pass
                else:
                    stack.append(folder_name)
            else:
                i += 1

        ret = ""
        i = 0
        while i < len(stack):
            ret += "/"
            ret += stack[i]
            i += 1

        if ret == "":
            return "/"
        return ret