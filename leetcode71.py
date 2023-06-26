class Solution:
    def simplifyPath(self, path: str) -> str:
        pathElements = path.split('/')
        res = []
        for i in range(len(pathElements)):
            if res and pathElements[i] == "..":
                res.pop()
            elif pathElements[i] not in ["", ".", ".."]:
                res.append(pathElements[i])
        return "/" + "/".join(res)
