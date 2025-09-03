class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        for i in range(len(searchWord)):
            pre = searchWord[:i+1]
            res.append(list(filter(lambda a: a.startswith(pre), products))[:3])
        return res