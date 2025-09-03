class Solution:
    def simplifyPath(self, path: str) -> str:
        eles = path.split("/")
        new_eles = []
        for ele in eles:
            if ele == "" or ele == ".":
                continue
            if ele == "..":
                if len(new_eles):
                    new_eles.pop()    
                continue
            new_eles.append(ele)
    
        return "/" + "/".join(new_eles)
