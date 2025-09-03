class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def is_digit(a):
            return ord("0") <= ord(a[0]) <= ord("9")
        
        def get_sort_key(a):
            splits = a.split(" ")
            if is_digit(splits[1]):
                return (1,)
            return (0, " ".join(splits[1:]), splits[0])

        logs.sort(key=get_sort_key)
        return logs