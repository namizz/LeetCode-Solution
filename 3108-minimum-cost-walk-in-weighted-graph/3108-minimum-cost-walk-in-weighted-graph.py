class Solution:
    def findRoot(self, node, parent):
        if parent[node] != node:
            parent[node] = self.findRoot(parent[node], parent)  # Path compression
        return parent[node]

    def minimumCost(self, n, edges, queries):
        parent = list(range(n))
        minPathCost = [-1] * n

        for source, target, weight in edges:
            sourceRoot = self.findRoot(source, parent)
            targetRoot = self.findRoot(target, parent)

            minPathCost[sourceRoot] = weight if minPathCost[sourceRoot] == -1 else minPathCost[sourceRoot] & weight
            minPathCost[targetRoot] = weight if minPathCost[targetRoot] == -1 else minPathCost[targetRoot] & weight

            if sourceRoot != targetRoot:
                parent[sourceRoot] = targetRoot
                minPathCost[targetRoot] &= minPathCost[sourceRoot]

        result = []
        for start, end in queries:
            if start == end:
                result.append(0)
            elif self.findRoot(start, parent) != self.findRoot(end, parent):
                result.append(-1)
            else:
                result.append(minPathCost[self.findRoot(start, parent)])

        return result