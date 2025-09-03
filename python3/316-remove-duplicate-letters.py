class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        present = set()
        stack = []
        last_occ = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in present:
                while stack and c < stack[-1] and last_occ[stack[-1]] > i:
                    present.remove(stack.pop())
                
                stack.append(c)
                present.add(c)
        
        return "".join(stack)