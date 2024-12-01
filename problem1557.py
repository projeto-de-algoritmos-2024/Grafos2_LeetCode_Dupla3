from collections import defaultdict

class Solution:
    def calculateSCC(self, n, edges):
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            reverse_graph[v].append(u)

        def dfs(v, graph, visited, stack):
            visited[v] = True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    dfs(neighbor, graph, visited, stack)
            stack.append(v)

        def dfs_transposed(v, reverse_graph, visited, scc):
            visited[v] = True
            scc.append(v)
            for neighbor in reverse_graph[v]:
                if not visited[neighbor]:
                    dfs_transposed(neighbor, reverse_graph, visited, scc)

        stack = []
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                dfs(i, graph, visited, stack)

        visited = [False] * n
        sccs = []
        while stack:
            node = stack.pop()
            if not visited[node]:
                scc = []
                dfs_transposed(node, reverse_graph, visited, scc)
                sccs.append(scc)

        return sccs

    def findSmallestSetOfVertices(self, n, edges):
        sccs = self.calculateSCC(n, edges)

        scc_index = {}
        for idx, scc in enumerate(sccs):
            for node in scc:
                scc_index[node] = idx

        scc_indegree = defaultdict(int)
        for u, v in edges:
            u_scc = scc_index[u]
            v_scc = scc_index[v]
            if u_scc != v_scc:
                scc_indegree[v_scc] += 1

        result = [scc[0] for idx, scc in enumerate(sccs) if scc_indegree[idx] == 0]
        
        return result
